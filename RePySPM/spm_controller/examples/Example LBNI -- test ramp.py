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
project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"

afm = AFMController(project_path)

# Set the scan parameters for the exploration
# Please skip this step if you prefer setting the initial parameters manually 
print("\n--- Ramp ---")

afm.scan_control.set_xyposition(5e-6, 15e-6, True)

# Start the F-D curve measurement
afm.utils.set_feedback_after_ramp(True)
afm.scan_control.do_ramp_relative_length(-0.5e-6, 1e-6, 2000, 0.1e-6, 0.1e-6, 0.1)

# Wait for ramp starts
time.sleep(5)

# Wait until the spec is done
while afm.scan_control.is_ramping():
    print("Ramping...")
    time.sleep(0.5)

data_ramp = afm.image.get_all_channels_data_ramp()

# Step N: Disconnect from the AFM system
afm.disconnect()
print("\n--- AFM disconnected ---")
