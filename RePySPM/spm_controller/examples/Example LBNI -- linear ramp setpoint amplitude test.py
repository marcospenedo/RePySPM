import nifpga
import sys
import os
import time

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

def set_setpoint_FPGA(fpga_session, set_point_val):
    """Set the setpoint value (in V) on the FPGA using floats."""
    params = fpga_session.registers['fb.p.params'].read()
    # Assume the register accepts a float value for setPoint
    params['setPoint'] = float(set_point_val)
    fpga_session.registers['fb.p.params'].write(params)

def set_excitation_amplitude_FPGA(fpga_session, amplitude_val):
    """
    Set the excitation amplitude on the FPGA.
    The FPGA expects an integer value.
    We scale the float amplitude (in V, for example) by 32768/10, then convert to int.
    """
    scaling_factor = 32768 / 10.0  # float scaling factor
    fpga_amplitude = scaling_factor * amplitude_val
    fpga_amplitude_int = int(fpga_amplitude)
    fpga_session.registers['lia.exc.dds.amplitude'].write(fpga_amplitude_int)

def linear_ramp_setpoint_exc_amplitude(afm, fpga_session, final_setpoint, final_exc_amplitude, duration_ms):
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
    params_zcontrol = fpga_session.registers['fb.p.params'].read()
    init_setpoint = float(params_zcontrol['setPoint'])
    init_exc_amplitude = float(fpga_session.registers['lia.exc.dds.amplitude'].read()) * (10.0 / 32768.0)
    
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
        set_setpoint_FPGA(fpga_session, current_setpoint)
        set_excitation_amplitude_FPGA(fpga_session, current_exc_amplitude)
    
    # Ensure final values are set exactly
    set_setpoint_FPGA(fpga_session, final_setpoint)
    set_excitation_amplitude_FPGA(fpga_session, final_exc_amplitude)
    
    # Update any related software state if needed
    afm.afmmode.am.set_exc_amplitude(final_exc_amplitude)
    afm.z_control.set_setpoint(final_setpoint)
    
    return 0

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)
    
    # Path to the bitfile
    bitfile_name = r"lbniAFMController_usbRIO_controllerFPGA_testboard.lvbitx"

    bitfile_folder = os.path.join(project_path, "FPGA Bitfiles")  # Automatically add "pythonAPI\"
    bitfile_path = os.path.join(bitfile_folder, bitfile_name)
    
    # Specify your FPGA resource name (adjust based on your hardware)
    resource_name = "RIO0"  # For example, use the correct resource from NI MAX

    fpga_session = nifpga.Session(bitfile_path, resource_name)
    
    linear_ramp_setpoint_exc_amplitude(afm, fpga_session, 0.2, 2, 5000)
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()


