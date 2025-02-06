import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import AFMController
from afm_controller import AFMController
from afm_controller.afm_modes import AFMModes

# Step 1: Initialize the AFM Controller
afm = AFMController()

# Step 2: Connect to the AFM system
afm.connect()

afm.afmmode.get_mode()

afm.afmmode.set_mode(AFMModes.AM)

afm.afmmode.get_mode()

afm.afmmode.am.get_exc_type()

# Step N: Disconnect from the AFM system
afm.disconnect()


def main():
    # Path to the VI
    Python_LV_Bridge_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-branch\OpenSPM-source\pythonAPI\PythonLVExternalBridge.vi"
    Run_Python_LV_Bridge_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-branch\OpenSPM-source\pythonAPI\AsynRunPythonLVExternalBridge.vi"
    
    LBNI_controller = AFMController(Python_LV_Bridge_path, Run_Python_LV_Bridge_path)
    
    LBNI_controller.ZControlPID.set_feedback(True)
    
    LBNI_controller.write_control("Timeout::20")
    
if __name__ == "__main__":
    main()