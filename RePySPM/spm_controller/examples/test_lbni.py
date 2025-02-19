import sys
import os
import time

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import AFMController
from lbni_controller import AFMController
from lbni_controller.afm_modes import AFMModes

def main():
    # Path to the VI
    Python_LV_Bridge_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source\pythonAPI\PythonLVExternalBridge.vi"
    Run_Python_LV_Bridge_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source\pythonAPI\AsynRunPythonLVExternalBridge.vi"
    Stop_Python_LV_Bridge_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source\pythonAPI\AsynStopPythonLVExternalBridge.vi"
    
    LBNI_controller = AFMController(Python_LV_Bridge_path, Run_Python_LV_Bridge_path, Stop_Python_LV_Bridge_path)

    LBNI_controller.z_control.set_zcontrolpid_parameters(0.00002, 0.000003, 0, 0.112, 'V', True, 'AM Mode')
    
    value = LBNI_controller.z_control.get_zcontrolpid_parameters()
    print(value)
    
    LBNI_controller.scan_control.scan_down()
    
    time.sleep(5)
    
    LBNI_controller.scan_control.scan_stop()
    
    # Step N: Disconnect from the AFM system
    LBNI_controller.disconnect()
    
if __name__ == "__main__":
    main()