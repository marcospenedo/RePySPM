import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController, AFMModes

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)
    
    # Set the scan parameters for the exploration
    # Please skip this step if you prefer setting the initial parameters manually 
    print("\n--- Setting Sweep ---")
    
    afm.afmmode.set_mode(AFMModes.AM)
    
    freq_init = 15000
    freq_end = 35000
    num_points = 110

    curve = afm.afmmode.am.do_sweep(freq_init, freq_end, num_points)

    print(curve)
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()