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
print("\n--- Get Channels names and all channels ---")

channel_names = afm.image.get_channels_names()
print (channel_names)

channel_data = afm.image.get_all_channels_data()
print (channel_data)

print("\n--- Get specific channel ---")

img_h = afm.image.get_channel("Height",0)
img_e = afm.image.get_channel("Error",0)

print(img_e)

# Step N: Disconnect from the AFM system
afm.disconnect()
print("\n--- AFM disconnected ---")
