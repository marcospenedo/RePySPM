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

# Path to the project
project_path = r"D:\\software\\Marcos\\OpenSPM-source\\"

afm = AFMController(project_path)

# Set the scan parameters for the exploration
# Please skip this step if you prefer setting the initial parameters manually 
print("\n--- Ramp ---")

# Actual z positon 
print("Actual position: ", afm.z_control.get_zposition())

# Start the F-D curve measurement
afm.utils.set_feedback_after_ramp(False)
afm.scan_control.do_ramp_relative_trig(0, 0.5, None, '<', 2000, 1e-6, 1e-6, 0.1)

# Wait until the ramp runs
while not afm.scan_control.is_ramping():
    print("Waiting ramping...")

# Wait until the spec is done
while afm.scan_control.is_ramping():
    print("Ramping...")
    time.sleep(0.5)

data_ramp = afm.image.get_all_channels_data_ramp()

height_fwd = - data_ramp[0][1]
height_bwd = - data_ramp[1][1]
amplitude_fwd = data_ramp[4][1]
amplitude_bwd = data_ramp[5][1]
phase_fwd = data_ramp[6][1]
phase_bwd = data_ramp[7][1]

plt.figure()
plt.plot(height_fwd, amplitude_fwd, '-b')
plt.plot(height_bwd, amplitude_bwd, '-r')
plt.ylabel('amplitude')
plt.xlabel('distance')
plt.show()

plt.figure()
plt.plot(height_fwd, phase_fwd, '-b')
plt.plot(height_bwd, phase_bwd, '-r')
plt.ylabel('phase')
plt.xlabel('distance')
plt.show()

# Step N: Disconnect from the AFM system
afm.disconnect()
print("\n--- AFM disconnected ---")
