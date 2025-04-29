from .commands import OHCcommands

import os
import nifpga
import time
import xml.etree.ElementTree as ET

class Utils:
    """
    A class containing useful functions to control the LBNI OHC.

    Attributes:
        controller: An instance of the AFMController responsible for communication.

    Methods:
        update_waveform_FPGA():
            Sends a command to update the waveform parameters in the FPGA.
        set_waveform_params():
            Sets the parameters for slow and fast waveforms with validation.
        get_waveform_params():
            Retrieves the waveform parameters from the controller.
        set/get_slowwave_N_poits():
            Sets or retrieves the number of points for the slow wave.
        set/get_slowwave_type():
            Sets or retrieves the type of slow wave.
        set/get_slowwave_roundN_poits():
            Sets or retrieves the number of rounding points for the slow wave.
        set/get_fastwave_N_poits():
            Sets or retrieves the number of points for the fast wave.
        set/get_fastwave_type():
            Sets or retrieves the type of fast wave.
        set/get_fastwave_roundN_poits():
            Sets or retrieves the number of rounding points for the fast wave.
        set/get_hysX_type():
            Sets or retrieves the type of hysteresis correction for the X-axis.
        set/get_hysY_type():
            Sets or retrieves the type of hysteresis correction for the Y-axis.
        set/get_hys_corr():
            Sets or retrieves whether hysteresis correction is enabled.
        set/get_res_corr():
            Sets or retrieves whether resonance correction is enabled.
        set/get_hyst_corr_X_path():
            Sets or retrieves the file path for hysteresis correction on the X-axis.
        set/get_hyst_corr_Y_path():
            Sets or retrieves the file path for hysteresis correction on the Y-axis.
        set/get_custom_waveform_X_path():
            Sets or retrieves the file path for a custom waveform on the X-axis.
        set/get_custom_waveform_Y_path():
            Sets or retrieves the file path for a custom waveform on the Y-axis.
        set/get_custom_wav_X():
            Sets or retrieves whether a custom waveform is used for the X-axis.
        set/get_custom_wav_Y():
            Sets or retrieves whether a custom waveform is used for the Y-axis.
        set/get_uni_bi_dir():
            Sets or retrieves whether the scanning is unidirectional or bidirectional.
        set/get_skip_lines():
            Sets or retrieves whether lines are skipped in the scan.
        set/get_feedback_after_ramp():
            Sets the feedback on/off after a ramp.
        set_timeout():
            Sets timeout of the loop that keeps listening the messages.
        set_setpoint_FPGA: Set the setpoint value (in V) on the FPGA using floats.
        set_excitation_amplitude_FPGA: Set the excitation amplitude on the FPGA.
        linear_ramp_setpoint_exc_amplitude: Gradually change the setpoint and excitation amplitude over a specified duration (in milliseconds)
            using float arithmetic
    """
    
    # Dictionary: controller_type -> bitfile filename
    CONTROLLER_BITFILES = {
        "lbni_afm_v2":            "lbniAFMController_usbRio80MHz_controllerFPGA.lvbitx",
        "lbni_sicm_v2":           "lbniAFMController_usbRio80MHz_controllerFPGA_lbniSICM_v2.lvbitx",
        "lbni_fred_v2":           "lbniAFMController_usbRio80MHz_controllerFPGA_Fred.lvbitx",
        "lbni_afsem_v2":          "lbniAFMController_usbRio80MHz_controllerFPGA_AFSEM.lvbitx",
        "driveAFM_afm_oem_v2":    "lbniAFMController_usbRio80MHz_controllerFPGA_DriveAFM_OEM.lvbitx",
        "qd_afsem_v2":            "lbniAFMController_usbRio80MHz_controllerFPGA_AFSEM_QD.lvbitx",
        "lbni_afm_oem_v2":        "lbniAFMController_usbRIO_controllerFPGA_OEMv2.lvbitx",
        "lbni_afm_oem_NOT2C_v2":  "lbniAFMController_usbRIO_controllerFPGA_OEMv2_NOT2C.lvbitx",
        "lbni_afm_v1_testboard":  "lbniAFMController_usbRIO_controllerFPGA_testboard.lvbitx",
        "lbni_afm_v1_OEM":        "lbniAFMController_usbRIO_controllerFPGA_OEM.lvbitx",
        "lbni_snom_v1":           "lbniAFMController_usbRIO_controllerFPGA_SNOM.lvbitx",
        "lbni_stm_v1":            "lbniAFMController_usbRIO_controllerFPGA_STM.lvbitx",
        "lbni_sicm_v1":           "lbniAFMController_usbRIO_controllerFPGA_SICM.lvbitx",
    }
    
    def get_controller_type_from_init(self, init_xml_path):
        """
        Parses the Init.xml file to extract the value of <Val> where <Name> is 'controller_type'.
        Returns that string or None if not found.
        """
        # Namespace used by LabVIEW XML
        ns = {'lv': 'http://www.ni.com/LVData'}
        
        tree = ET.parse(init_xml_path)
        root = tree.getroot()
        
        # Find the <Cluster> element under the <LVData> root
        cluster_elem = root.find('lv:Cluster', ns)
        if cluster_elem is None:
            return None
        
        # Within <Cluster>, look for all <String> elements
        string_elems = cluster_elem.findall('lv:String', ns)
        for s in string_elems:
            name_elem = s.find('lv:Name', ns)
            val_elem  = s.find('lv:Val', ns)
            if name_elem is not None and name_elem.text == "controller_type":
                return val_elem.text  # The controller_type value
        
        return None
    
    def get_bitfile_name(self, init_xml_path):
        """
        Reads the controller_type from Init.xml and returns the matching .lvbitx filename.
        Returns None if the controller_type isn't found or isn't in the dictionary.
        """
        controller_type = self.get_controller_type_from_init(init_xml_path)
        if controller_type is None:
            print("Could not find 'controller_type' in Init.xml.")
            return None
        
        bitfile = self.CONTROLLER_BITFILES.get(controller_type)
        if bitfile is None:
            print(f"Unknown controller_type: {controller_type}")
        return bitfile
    
    def __init__(self, controller, root_path):
        """
        Initializes the Utils class with the given controller.
        
        Args:
            controller: An instance of the AFMController handling communication.
        """
        
        self.controller = controller  # Store reference to AFMController
        
        # Path to the bitfile
        xml_folder = os.path.join(root_path, "config") 
        init_xml_path = os.path.join(xml_folder, "Init.xml")
        
        bitfile_folder = os.path.join(root_path, "FPGA Bitfiles")  # Automatically add "pythonAPI\"
        bitfile_name = self.get_bitfile_name(init_xml_path)
        
        if not bitfile_name:
            raise ValueError(f"No valid bitfile {bitfile_name} found.")
        
        bitfile_path = os.path.join(bitfile_folder, bitfile_name)
        
        # Specify your FPGA resource name (adjust based on your hardware)
        resource_name = "RIO0"  # For example, use the correct resource from NI MAX

        self.fpga_session = nifpga.Session(bitfile_path, resource_name)
        
    def update_waveform_FPGA(self):
        
        # To send it to the FPGA
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Update FPGA:True"
        self.controller.write_control(command)
        
        return 0
    
    def set_waveform_params(self, slowN: int, slowType: str, slowroundN: int, 
                            fastN: int, fastType: str, fastroundN: int):
        """Set parameters for slow and fast waveforms with validation."""
        
        # Define valid waveform types
        valid_values = {"Triangle", "Rounded", "Sine"}
        
        # Validate integer values (must be > 2)
        int_params = {
            "slowWavePts": slowN,
            "slowRoundPts": slowroundN,
            "fastWavePts": fastN,
            "fastRoundPts": fastroundN
        }
    
        for param, value in int_params.items():
            if not isinstance(value, int) or value <= 2:
                raise ValueError(f"Invalid number of points for {param}: {value}. Must be an integer greater than 2.")
            
            command = f"{OHCcommands.w_wav}scanWaveFormCtl:{param}:{value}"
            self.controller.write_control(command)
    
        # Validate slow and fast waveform types
        type_params = {
            "slowWaveType": slowType,
            "fastWaveType": fastType
        }
    
        for param, value in type_params.items():
            if value not in valid_values:
                raise ValueError(f"Invalid waveform type for {param}: {value}. Must be one of {valid_values}.")
            
            command = f"{OHCcommands.w_wav}scanWaveFormCtl:{param}:{value}"
            self.controller.write_control(command)
    
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0
   
    def get_waveform_params(self):
        """Retrieve waveform parameters from the controller."""
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        # Fetch the control values once
        response = self.controller.read_control(command, control)
    
        # Return values in the desired order
        return [response[0], response[2], response[4], response[1], response[3], response[5]]
   
    def set_slowwave_N_points(self, value: int):
        """Set the number of points for the slow wave, ensuring it is greater than 2."""
        if not isinstance(value, int) or value <= 2:
            raise ValueError(f"Invalid number of slow wave points: {value}. Must be an integer greater than 2.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:slowWavePts:{value}"
        self.controller.write_control(command)
        
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_slowwave_N_poits(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[0]
    
    def set_slowwave_type(self, value: str):
        """Set the slow wave type, ensuring it is a valid option."""
        
        valid_values = {"Triangle", "Rounded", "Sine"}
    
        if value not in valid_values:
            raise ValueError(f"Invalid slow wave type: {value}. Must be one of {valid_values}.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:slowWaveType:{value}"
        self.controller.write_control(command)
    
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_slowwave_type(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[2]
    
    def set_slowwave_roundN_poits(self, value: int):
        
        if not isinstance(value, int) or value <= 2:
            raise ValueError(f"Invalid number of slow wave round points: {value}. Must be an integer greater than 2.")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:slowRoundPts:{value}"
        self.controller.write_control(command)
        
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_slowwave_roundN_poits(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[4]    
        
    def set_fastwave_N_points(self, value: int):
        """Set the number of points for the slow wave, ensuring it is greater than 2."""
        if not isinstance(value, int) or value <= 2:
            raise ValueError(f"Invalid number of fast wave points: {value}. Must be an integer greater than 2.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:fastWavePts:{value}"
        self.controller.write_control(command)
    
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_fastwave_N_poits(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[1]
    
    def set_fastwave_type(self, value: str):
        """Set the slow wave type, ensuring it is a valid option."""
        
        valid_values = {"Triangle", "Rounded", "Sine"}
    
        if value not in valid_values:
            raise ValueError(f"Invalid fast wave type: {value}. Must be one of {valid_values}.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:fastWaveType:{value}"
        self.controller.write_control(command)
    
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_fastwave_type(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[3]
    
    def set_fastwave_roundN_poits(self, value: int):
        
        if not isinstance(value, int) or value <= 2:
            raise ValueError(f"Invalid number of fast wave round points: {value}. Must be an integer greater than 2.")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:fastRoundPts:{value}"
        self.controller.write_control(command)
        
        # To send it to the FPGA
        self.update_waveform_FPGA()
    
        return 0

    def get_fastwave_roundN_poits(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[5]        

    def set_hysX_type(self, value: str):
        valid_values = {"Config", "Scan", "None"}
    
        if value not in valid_values:
            raise ValueError(f"Invalid hysteresis X source type: {value}. Must be one of {valid_values}.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:HysX Source:{value}"
        self.controller.write_control(command)
    
        return 0
    
    def get_hysX_type(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[11]    

    def set_hysY_type(self, value: str):
        valid_values = {"Config", "Scan", "None"}
    
        if value not in valid_values:
            raise ValueError(f"Invalid hysteresis Y source type: {value}. Must be one of {valid_values}.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:HysY Source:{value}"
        self.controller.write_control(command)
    
        return 0
    
    def get_hysY_type(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[15]   

    def set_hys_corr(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Hys Correct:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_hys_corr(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[8]

    def set_res_corr(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Resonance:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_res_corr(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[9]

    def update_shift(self):
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Shift:True"
        self.controller.write_control(command)
        
        return 0
    
    def set_N_shift(self, value: int):
        if not isinstance(value, int):
            raise ValueError(f"Invalid number of shift wave: {value}. Must be an integer.")
    
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Percent:{value}"
        self.controller.write_control(command)
    
        return 0

    def get_N_shift(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[13]

    def set_hyst_corr_X_path(self, value: str):
        """Set the hysteresis correction X file path, ensuring it exists."""
        
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
    
        command = f"{OHCcommands.w_wav}Hysteresis correction X:{value}"
        self.controller.write_control(command)
    
        return 0

    def get_hyst_corr_X_path(self):
        
        control = "Hysteresis correction X"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)
    
    def set_hyst_corr_Y_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Hysteresis correction Y:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_hyst_corr_Y_path(self):
        
        control = "Hysteresis correction Y"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)    
 
    def set_custom_waveform_X_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Custom X waveform file:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_waveform_X_path(self):
        
        control = "Custom X waveform file"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)
        
    def set_custom_wav_X(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}From file X:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_wav_X(self):
        
        control = "From file X"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_custom_waveform_Y_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Custom Y waveform file:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_waveform_Y_path(self):
        
        control = "Custom Y waveform file"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_custom_wav_Y(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}From file Y:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_wav_Y(self):
        
        control = "From file Y"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_uni_bi_dir(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}Uni/Bidir:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_uni_bi_dir(self):
        
        control = "Uni/Bidir"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)        
    
    def set_skip_lines(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}Skip lines:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_skip_lines(self):
        
        control = "Skip lines"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)       
    
    def set_feedback_after_ramp(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_ram}Reenable Feedback:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_feedback_after_ramp(self):
        
        control = "Reenable Feedback"
        command = f"{OHCcommands.r_ram}{control}"
        
        return self.controller.read_control(command, control)     
    
    def set_excitation(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_exc}Excitation enable?:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_excitation(self):
        
        control = "Excitation enable?"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)        
    
    def set_timeout(self, value: int):
        """Sets timeout of the loop that keeps listening the messages.

        Args:
            value (int): time in ms.
        """
        if not isinstance(value, (int)) or not (0 <= value):
            raise ValueError(f"Invalid timeout: {value}. Must be a non-negative float.")
        
        command = f"Timeout::{value}"
        self.controller.write_control(command)
        
        return 0
    
    def set_setpoint_FPGA(self, set_point_val):
        """Set the setpoint value (in V) on the FPGA using floats."""
        scaling_factor = 0.1  # float scaling factor
        params = self.fpga_session.registers['fb.p.params'].read()
        # Assume the register accepts a float value for setPoint
        params['setPoint'] = scaling_factor * float(set_point_val)
        self.fpga_session.registers['fb.p.params'].write(params)
        
        return 0
    
    def set_excitation_amplitude_FPGA(self, amplitude_val):
        """
        Set the excitation amplitude on the FPGA.
        The FPGA expects an integer value.
        We scale the float amplitude (in V, for example) by 32768/10, then convert to int.
        """
        scaling_factor = 32768 / 10.0  # float scaling factor
        fpga_amplitude = scaling_factor * amplitude_val
        fpga_amplitude_int = int(fpga_amplitude)
        self.fpga_session.registers['lia.exc.dds.amplitude'].write(fpga_amplitude_int)
        
        return 0
    
    def linear_ramp_setpoint_exc_amplitude(self, final_setpoint, final_exc_amplitude, duration_ms):
        """
        Gradually change the setpoint and excitation amplitude over a specified duration (in milliseconds)
        using float arithmetic.
        
        :param final_setpoint: Final setpoint value (float)
        :param final_exc_amplitude: Final excitation amplitude (float)
        :param duration_ms: Duration for the ramp in milliseconds (float/int)
        """
        duration = duration_ms / 1000.0  # Convert ms to seconds
        start_time = time.perf_counter()
        
        # Read initial values from the FPGA
        params_zcontrol = self.fpga_session.registers['fb.p.params'].read()
        init_setpoint = float(params_zcontrol['setPoint']) * 10 # Multiplied by 10, the positive range of the FPGA output
        init_exc_amplitude = float(self.fpga_session.registers['lia.exc.dds.amplitude'].read()) * (10.0 / 32768.0)
        
        while True:
            now = time.perf_counter()
            elapsed = now - start_time
            
            if elapsed >= duration:
                break  # Exit loop once duration is reached
            
            # Calculate the normalized time (0 to 1)
            t = elapsed / duration
            current_setpoint = init_setpoint + (final_setpoint - init_setpoint) * t 
            current_exc_amplitude = init_exc_amplitude + (final_exc_amplitude - init_exc_amplitude) * t
            
            # Update FPGA registers
            self.set_setpoint_FPGA(current_setpoint)
            self.set_excitation_amplitude_FPGA(current_exc_amplitude)
        
        # Ensure final values are set exactly
        self.set_setpoint_FPGA(final_setpoint)
        self.set_excitation_amplitude_FPGA(final_exc_amplitude)
        
        # Update any related software state if needed
        self.controller.afmmode.am.set_exc_amplitude(final_exc_amplitude)
        self.controller.z_control.set_setpoint(final_setpoint)
        
        return 0     
   
    def __repr__(self):
        pass
