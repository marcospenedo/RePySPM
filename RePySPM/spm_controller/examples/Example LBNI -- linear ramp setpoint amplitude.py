import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)
    
    afm.utils.linear_ramp_setpoint_exc_amplitude(final_setpoint = -2, final_exc_amplitude = 5, duration_ms = 2550)
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()


