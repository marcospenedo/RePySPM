import sys
import os
import time

import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

import cv2

import shutil

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

# Here we need a function to convert the pixel coordinates to the distance coordinates 
def convert_coord(obj, img, coord, angle=None):
    '''
    Convert the coordinate from pixel to distance.
    Apply rotation if needed.

    Input:
        obj    - Required: AFMController object
        img    - Required: the image array where coordinates were extracted
        coord  - Required: coordinate pairs in the unit of pixels: [[x0, x1, x2, ...], [y0, y1, y2, ...]]
        angle  - Optional: the rotation angle of the scan. If not provided, angle will be read from the controller.
    Output:
        pos_sorted - Sorted array of coordinate pairs in the physical unit
    '''
    
    x, y = coord
    
    scan_angle = obj.scan_parameters.get_rotation() if angle is None else angle
    
    # Convert angle to radians
    theta_rad = np.radians(-scan_angle)
    
    # Create 2D rotation matrix
    rot_matrix = np.array([[np.cos(theta_rad), -np.sin(theta_rad)],
                           [np.sin(theta_rad), np.cos(theta_rad)]])
    
    # Apply the rotation matrix to the coordinates
    center = (np.array(np.shape(img))-1) // 2
    x_rot, y_rot = np.zeros_like(x), np.zeros_like(y)
    for i in range(len(x)):
        x_rot[i], y_rot[i] = np.dot(rot_matrix, (np.array([x[i], y[i]])-center)) + center
    
    # Convert the pixels to the distance
    xpixels, ypixels = np.shape(img)
    xsize, ysize = obj.scan_parameters.get_width(), obj.scan_parameters.get_height()

    xfactor = xsize / xpixels
    yfactor = ysize / ypixels

    positions = np.zeros([len(x), 2])

    for i in range(len(x)):
        positions[i] = np.array([x_rot[i] * xfactor, y_rot[i] * yfactor])

    # Sort the positions according to x first and y second
    pos_sorted = sorted(positions, key=lambda x: (x[1], x[0]))
    
    ###########
    ###########
    # I assume the lines below are a copy paste thing and they are a mistake
    # for key in p:
        # self.update_param(key=key, value=p[key])
    
    return pos_sorted

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)

    # Step 4: Set scan parameters
    # Please skip this step if you prefer setting the initial parameters manually 
    print("\n--- Setting Scan Parameters ---")
    afm.scan_parameters.set_scan_parameters(
        width = 10e-6,  # 10 µm
        height = 10e-6, # 10 µm
        rotation = 0, # 0 deg
        offset_x = 0, # 0 µm
        offset_y = 0, # 0 µm
        scan_speed = 1, # 1 Hz
        pixels_x = 128,
        pixels_y = 128,
        tilt_x = 0,
        tilt_y = 0,
        close_loopXY = False,
        close_loopZ = False
    )
    print("Scan parameters set.")

    # Start a new scan and wait until it's done
    
    print("\n--- Starting Scan ---")
    # Start the topography scan and wait until it's done
    afm.z_control.set_feedback(True)
    print("Feedback ON")
    afm.scan_control.scan_up()
    print("Scanning upwards...")
    
    # You can either wait for a fixed time, or check if the scan is done every 10 sec
        
    elapsed_time = 0
    while afm.scan_control.is_scanning():
        time.sleep(1)  # Check every second
        elapsed_time += 1
    
        if elapsed_time >= 10:
            print("Scanning...")
            elapsed_time = 0  # Reset the counter

    # Read the topography data from the controller or the saved image file
    
    img = afm.image.get_channel("Height",0)

    # img = np.copy(w.data[0])
    
    # Normalize the image
    image = (img-img.min())/img.ptp() * 256
    image = image.astype(np.uint8)
    # Apply the Canny edge detector
    edges = cv2.Canny(image, 150, 200)  # Adjust the threshold values based on your image
    
    # Display the original image and the edges
    plt.subplot(121), plt.imshow(image, cmap='viridis')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Canny Edges'), plt.xticks([]), plt.yticks([])
    
    plt.show()
 
    # Adjust the threshold number as needed
    y, x = np.where(edges>200)
    
    plt.imshow(img, origin='lower')
    plt.plot(x, y, 'b.')
    # plt.xlim(0, 50)
    # plt.ylim(0, 50)
    print(len(x))
    len(x)
        
    pos_sorted = convert_coord(afm, img, coord=[x, y])   
    
    num_pts = len(pos_sorted[0])
    
    for i in range(num_pts):
        print("Working on Location {}/{}".format(i, num_pts), end='\r')
        
        # Get the next point to measure
        x_next, y_next = pos_sorted[i]
    
        # Move the probe to the new location
        afm.scan_control.set_xyposition(x_next, y_next, True)
    
        # Start the F-D curve measurement
        afm.utils.set_feedback_after_ramp(True)
        afm.scan_control.do_ramp_relative_length(-0.5e-6, 1e-6, 2000, 0.5e-6, 0.5e-6, 0.1)
        # Wait for ramp starts
        time.sleep(5)
    
        # Wait until the spec is done
        while afm.scan_control.is_ramping():
            time.sleep(0.2)
            
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
        
if __name__ == "__main__":
    main()