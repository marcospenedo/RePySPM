import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nanosurf_controller import AFMController

def main():
    # Connect to Nanosurf software running on this machine
    afm = AFMController()

    # Set the scan parameters for the exploration
    # Please skip this step if you prefer setting the initial parameters manually
    print("\n--- Setting Scan Parameters ---")

    afm.scan_parameters.set_width(2.52e-6)
    afm.scan_parameters.set_offset_x(10.52e-6)
    afm.scan_parameters.set_offset_y(12e-6)
    afm.scan_parameters.set_scan_speed(1)

    print("\n--- Scan Parameters set ---")

    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")

if __name__ == "__main__":
    main()
