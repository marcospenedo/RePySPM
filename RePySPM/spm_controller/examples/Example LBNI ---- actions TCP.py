import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lbni_controller import AFMController

def main():
    # Connect via TCP to LabVIEW running on this machine
    afm = AFMController()

    # --- Read scan action states ---
    print("\n--- Scan Actions ---")

    print(f"Is scanning:       {afm.scan_control.is_scanning()}")
    print(f"Is paused:         {afm.scan_control.is_paused()}")
    print(f"Continuous scan:   {afm.scan_control.isContinuousScan()}")
    print(f"Auto save:         {afm.scan_control.isAutoSave()}")

    # --- Read channel names ---
    print("\n--- Channel Names ---")

    channel_names = afm.image.get_channels_names()
    print(f"Channels: {channel_names}")

    # Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")

if __name__ == "__main__":
    main()
