import sys
import os
import time

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

import shutil

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)
    
    # Set the scan parameters for the exploration
    # Please skip this step if you prefer setting the initial parameters manually 
    print("\n--- Setting Scan Parameters ---")
    afm.scan_parameters.set_scan_parameters(
        width = 10e-6,  # 10 µm
        height = 10e-6, # 10 µm
        rotation = 0, # 0 deg
        offset_x = 0, # 0 µm
        offset_y = 0, # 0 µm
        scan_speed = 3,    # 1 Hz
        pixels_x = 128,
        pixels_y = 128,
        tilt_x = 0,
        tilt_y = 0,
        close_loopXY = False,
        close_loopZ = False
    )
    print("Scan parameters set.")
    
    # Define the grid-size
    # Assume this is a 1D exploration along the x-axis with a total distance L
    L = 100e-6  # 10 µm
    # displacement = [L, 0]
    num_points = 10
    
    # Initial sample height
    # This is the sample surface height across the exploration distance, D
    # If the values here are incorrect, the probe will crash into the sample surface or it takes forever to approach!
    # sample_height = [1.8e-3] * num_points # Currently, no motor stage on this system
    
    # offset = 150e-6 # the pre-engage height is 150 um from the sample surface # Currently, no motor stage on this system
    
    #Start at -half of the L displayament
    afm.scan_parameters.set_offset_x(-L/2)
    
    # Set the new sample height
    # afm.motors.set_sample_height(sample_height[i]) # Currently, no motor stage on this system
    # Move the probe to the pre-engage height
    # afm.z_control.moveZ_stage_distance(sample_height[i] + offset) # Currently, no motor stage on this system
    # Start the approaching process
    afm.motors.start_approach()
    
    # Wait until the approaching to finish
    max_wait = 5 * 60 # let's wait no longer than 5 min
    N = 0

    while afm.motors.is_approaching() and N <= int(max_wait / 10):
        time.sleep(10)
        N += 1

    # Remove continuous scan
    afm.scan_control.scan_continuous(False)

    step = L / (num_points - 1)  # Step size to distribute points evenly
    
    for i in range(num_points):
        print("Working on Location: {}/{}".format(i+1, num_points), end='\r')
    
        # Start the topography scan and wait until it's done
        afm.z_control.set_feedback(True)
        print("Feedback ON")
        afm.scan_control.scan_up()
        print("Scanning up")

        max_wait = 5 * 60 # let's wait no longer than 5 min
        N = 0
        
        elapsed_time = 0
        while afm.scan_control.is_scanning():
            time.sleep(1)  # Check every second
            elapsed_time += 1
        
            if elapsed_time >= 10:
                print("Scanning...")
                elapsed_time = 0  # Reset the counter
    
        # Next we withdraw the probe and move to the next location to measure
        afm.z_control.retract()
        print("Feedback OFF and retract")
        
        # afm.motors.moveXstage(L/num_points)# Currently, no motor stage on this system
        
        # Move the scan position
        offset = -L/2 + (i+1) * step
        afm.scan_parameters.set_offset_x(offset)
        print("Moving...")
        time.sleep(2)
        # Wait until the moving is done
        
        
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
        
if __name__ == "__main__":
    main()