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


# Path and folder settings
save_path = r"D:\\AFM temp data\\"  # Base path where data will be saved
folder_name = "force_distance_data"  # Folder to store data and plots
curve_name = "curve_test"  # Prefix for naming the files

# Create the directory if it doesn't exist
full_save_path = os.path.join(save_path, folder_name)
if not os.path.exists(full_save_path):
    os.makedirs(full_save_path)


# Path to the project
project_path = r"D:\\Sakshi\\OpenSPM-source\\"
afm = AFMController(project_path)

# Set the scan parameters for the exploration
# Please skip this step if you prefer setting the initial parameters manually 
print("\n--- Ramp ---")
afm.scan_control.scan_stop()
# afm.z_control.retract()

# Actual z position 
print("Actual position: ", afm.z_control.get_zposition())

# Start the F-D curve measurement
afm.utils.set_feedback_after_ramp(True)

# Define the number of points along X and Y
nx = 3  # Number of steps in x-direction
ny = 1  # Number of steps in y-direction
N = 3  # Number of repetitions for each point

# Define the scan area dimensions in meters
width = 0.1e-6   # Total width of the grid (meters)
height = 0.1e-6  # Total height of the grid (meters)

# Define the origin (you can change this)
x0 = 0.0
y0 = 0.0

# Calculate the step size
dx = width / (nx - 1) if nx > 1 else 0
dy = height / (ny - 1) if ny > 1 else 0

# Initialize a plot
plt.ion()  # Turn on interactive mode (non-blocking)

# List to store all curves for the final plot
all_height_fwd = []
all_VD_fwd = []
all_height_bwd = []
all_VD_bwd = []

# List to store all the data for the final single data file
all_data = []

# Loop over the grid of (x, y) positions
for iy in range(ny):
    for ix in range(nx):
        # Calculate the absolute (x, y) position
        x_pos = x0 + ix * dx
        y_pos = y0 + iy * dy

        for repeat in range(N):  # Repeat N times for the same grid position
            # Set the AFM tip position
            afm.scan_control.set_xyposition(x_pos, y_pos, forced=False)
            print(f"Moving to position ({x_pos:.12e}, {y_pos:.12e}) - Repeat {repeat + 1}/{N}")

            # Start the force-distance ramp
            afm.scan_control.do_ramp_relative_trig(
                -50e-9,     # Init position
                0.5,         # Ramp set point
                None,        # Signal to trigger
                '>',         # Trigger condition
                2000,        # Trigger level
                0.5e-6,      # Speed fwd m/s
                0.51e-6,      # Speed bwd m/s
                0            # Waiting time
            )

            # Wait until the ramping starts
            while not afm.scan_control.is_ramping():
                print("Waiting for ramp to start...")
                time.sleep(0.1)

            # Wait until the ramping ends
            while afm.scan_control.is_ramping():
                print("Ramping in progress...")
                time.sleep(0.5)

            time.sleep(1)

            data_ramp = afm.image.get_all_channels_data_ramp()

            height_fwd = data_ramp[0][1]
            height_bwd = data_ramp[1][1]
            VD_fwd = data_ramp[2][1]
            VD_bwd = data_ramp[3][1]

            # Clear the previous plot to avoid infinite additions to the legend
            plt.clf()  # Clear the current figure

            # Plot the data on the same plot
            plt.plot(height_fwd, VD_fwd, '-b', label=f'Position ({x_pos:.2e}, {y_pos:.2e}) Forward')
            plt.plot(height_bwd, VD_bwd, '-r', label=f'Position ({x_pos:.2e}, {y_pos:.2e}) Backward')

            # Optionally, adjust labels and title dynamically
            plt.xlabel('Distance')
            plt.ylabel('VD')
            plt.title('Force-Distance Curves')

            # Optionally, display a legend
            plt.legend()

            # Refresh the plot without blocking
            plt.draw()

            # Pause for a short time to allow the plot to update
            plt.pause(0.1)  # Small pause to allow the plot to update

            # Save the plot as a PNG file
            plot_filename = f"{curve_name}_{iy}_{ix}_repeat{repeat + 1}.png"
            plt.savefig(os.path.join(full_save_path, plot_filename), format="png")
            print(f"Saved plot: {plot_filename}")

            # Save the data as a .dat file
            data_filename = f"{curve_name}_{iy}_{ix}_repeat{repeat + 1}.dat"
            data = np.column_stack((height_fwd, VD_fwd, height_bwd, VD_bwd))
            np.savetxt(os.path.join(full_save_path, data_filename), data, fmt='%.6e', header='Height_fwd\tVD_fwd\tHeight_bwd\tVD_bwd')
            print(f"Saved data: {data_filename}")

            # Add the current data to the list for the final plot
            all_height_fwd.append(height_fwd)
            all_VD_fwd.append(VD_fwd)
            all_height_bwd.append(height_bwd)
            all_VD_bwd.append(VD_bwd)

            # For the final single file (each curve will be a column)
            # Stack the 4 columns for this curve
            curve_data = np.column_stack((height_fwd, VD_fwd, height_bwd, VD_bwd))

            # Engadir cada fila (punto) a all_data
            all_data.append(curve_data)

            print(f"Ramp completed at position ({x_pos:.2e}, {y_pos:.2e}) - Repeat {repeat + 1}/{N}\n")

# After all ramps are done, turn off interactive mode
plt.ioff()  # Turn off interactive mode

# Create the final figure with all curves
plt.figure(figsize=(10, 6))
for h_fwd, v_fwd, h_bwd, v_bwd in zip(all_height_fwd, all_VD_fwd, all_height_bwd, all_VD_bwd):
    plt.plot(h_fwd, v_fwd, '-b')  # Forward curves in blue
    plt.plot(h_bwd, v_bwd, '-r')  # Backward curves in red

# Customize final plot
plt.xlabel('Distance')
plt.ylabel('VD')
plt.title('All Force-Distance Curves')
plt.legend(['Forward', 'Backward'], loc='best')

# Save the final figure as a PNG
final_plot_filename = "final_all_curves.png"
plt.savefig(os.path.join(full_save_path, final_plot_filename), format="png")
print(f"Saved final summary plot: {final_plot_filename}")

# Save all the collected data to a single file
final_data_filename = "all_curves_data.dat"
header_parts = []
for iy in range(ny):
    for ix in range(nx):
        for repeat in range(N):
            tag = f"{iy}_{ix}_repeat{repeat + 1}"
            header_parts.extend([
                f"Height_fwd_{tag}",
                f"VD_fwd_{tag}",
                f"Height_bwd_{tag}",
                f"VD_bwd_{tag}"
            ])
header = "\t".join(header_parts)

# Save the data in a single file with all columns
np.savetxt(os.path.join(full_save_path, final_data_filename), all_data, fmt='%.6e', header=header)
print(f"Saved all curves data: {final_data_filename}")

# Show the final plot
plt.show()


# Step N: Disconnect from the AFM system
afm.disconnect()
print("\n--- AFM disconnected ---")