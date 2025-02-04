import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Now you can import AFMController
from afm_controller import AFMController
from afm_controller.afm_modes import AFMModes

# Step 1: Initialize the AFM Controller
afm = AFMController()

# Step 2: Connect to the AFM system
afm.connect()

afm.afmmode.get_mode()

afm.afmmode.set_mode(AFMModes.AM)

afm.afmmode.get_mode()

afm.afmmode.am.get_exc_type()

# Step N: Disconnect from the AFM system
afm.disconnect()
