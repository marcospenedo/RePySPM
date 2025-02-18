from .commands import OHCcommands

import os

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
    """
    
    def __init__(self, controller):
        """
        Initializes the Utils class with the given controller.
        
        Args:
            controller: An instance of the AFMController handling communication.
        """
        
        self.controller = controller  # Store reference to AFMController
        
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)[15]   

    def set_hys_corr(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Hys Correct:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_hys_corr(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)[8]

    def set_res_corr(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:Resonance:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_res_corr(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
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
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)
    
    def set_hyst_corr_Y_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Hysteresis correction Y:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_hyst_corr_Y_path(self):
        
        control = "Hysteresis correction Y"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)    
 
    def set_custom_waveform_X_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Custom X waveform file:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_waveform_X_path(self):
        
        control = "Custom X waveform file"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)
        
    def set_custom_wav_X(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}From file X:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_wav_X(self):
        
        control = "From file X"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_custom_waveform_Y_path(self, value: str):
                
        if not isinstance(value, str) or not os.path.isfile(value):
            raise ValueError(f"Invalid file path: {value}. The file must exist.")
               
        command = f"{OHCcommands.w_wav}Custom Y waveform file:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_waveform_Y_path(self):
        
        control = "Custom Y waveform file"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_custom_wav_Y(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}From file Y:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_custom_wav_Y(self):
        
        control = "From file Y"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)    
    
    def set_uni_bi_dir(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}Uni/Bidir:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_uni_bi_dir(self):
        
        control = "Uni/Bidir"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)        
    
    def set_skip_lines(self, value: bool):
        
        if not isinstance(value, bool):
            raise ValueError(f"Invalid value: {value}. Must be a boolean (True or False).")
               
        command = f"{OHCcommands.w_wav}Skip lines:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_skip_lines(self):
        
        control = "Skip lines"
        command = f"{OHCcommands.w_wav}{control}"
        
        return self.controller.read_control(command, control)       
    
    def __repr__(self):
        pass
