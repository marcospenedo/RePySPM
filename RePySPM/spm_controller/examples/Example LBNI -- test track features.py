import sys
import os
import time

import numpy as np
from scipy.signal import correlate2d
from scipy.ndimage import shift
import matplotlib.pyplot as plt

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import AFMController
from lbni_controller import AFMController

def calculate_drift(reference_image, current_image):
    """Calculate pixel shift between reference and current image using cross-correlation."""
    # Normalized 
    ref = reference_image - np.mean(reference_image)
    cur = current_image - np.mean(current_image)

    correlation = correlate2d(cur, ref, mode='full')

    # Max correlation
    y_shift, x_shift = np.unravel_index(np.argmax(correlation), correlation.shape)

    # Center correlation center at the image center
    center_y = reference_image.shape[0] - 1
    center_x = reference_image.shape[1] - 1

    drift_y = y_shift - center_y
    drift_x = x_shift - center_x

    return (drift_y, drift_x)

def main():
    # Path to the project
    project_path = r"D:\\software\\Marcos\\OpenSPM-source\\"
    
    afm = AFMController(project_path)
    
    afm.scan_control.scan_stop()
    template_image = afm.image.get_channel("Height", 0)

    # Activate interactive mode for matplotlib
    plt.ion()
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    im1 = axs[0].imshow(template_image, cmap='gray')
    axs[0].set_title("Template Image")
    im2 = axs[1].imshow(template_image, cmap='gray')  # Placeholder
    axs[1].set_title("Current Image")
    plt.tight_layout()
    
    # afm.z_control.retract()
    afm.scan_control.scan_continuous(False)
    afm.z_control.set_feedback(True)

    while True:
        # scan_rate = afm.scan_parameters.get_scan_speed()
        # image_time = (1/scan_rate) * afm.scan_parameters.get_pixels_y()
        # time.sleep(image_time)

        afm.scan_control.scan_down()
        while afm.scan_control.is_scanning():
            time.sleep(0.1)
        
        current_image = afm.image.get_channel("Height", 0)

        im2.set_data(current_image)
        im2.set_clim(vmin=current_image.min(), vmax=current_image.max())  # Optional: normalize scale
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.01)

        drift = calculate_drift(template_image, current_image)

        # Set the scan parameters for the exploration
        # Please skip this step if you prefer setting the initial parameters manually 
        print("\n--- Setting Scan Parameters ---")

        width = afm.scan_parameters.get_width()
        pixels_x = afm.scan_parameters.get_pixels_x()
        height = afm.scan_parameters.get_height()
        pixels_y = afm.scan_parameters.get_pixels_y()

        # Calculate offsets from drift and width, pixels_x, height and pixels_y
        # Calculate physical offset from pixel drift
        drift_y, drift_x = drift  # unpack to match axis names

        off_x = drift_x * (width / pixels_x)
        off_y = drift_y * (height / pixels_y)

        print(f"Drift in pixels: x = {drift_x}, y = {drift_y}")
        print(f"Offset applied: off_x = {off_x:.9f}, off_y = {off_y:.9f}")

        afm.scan_parameters.set_offset_x(afm.scan_parameters.get_offset_x() + off_x)
        afm.scan_parameters.set_offset_y(afm.scan_parameters.get_offset_y() + off_y)
        
        print("\n--- Scan Parameters set ---")
        
        # template_image = current_image;
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()