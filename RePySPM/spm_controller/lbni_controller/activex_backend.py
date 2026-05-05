import win32com.client
import time
import os


class ActiveXBackend:
    """ActiveX/LabVIEW backend for AFMController."""

    def __init__(self, root_path):
        api_path = os.path.join(root_path, "pythonAPI")
        self.Python_LV_Bridge_path = os.path.join(api_path, "PythonLVExternalBridge.vi")
        self.Run_Python_LV_Bridge_path = os.path.join(api_path, "AsynRunPythonLVExternalBridge.vi")
        self.Stop_Python_LV_Bridge_path = os.path.join(api_path, "AsynStopPythonLVExternalBridge.vi")

        self.labview = None
        self.Python_LV_Bridge_reference = None
        self.Run_Python_LV_Bridge_reference = None

    def connect(self):
        print(f"Connecting to LabVIEW via ActiveX: {self.Python_LV_Bridge_path}")
        try:
            self.labview = win32com.client.Dispatch("LabVIEW.Application")
            self.Python_LV_Bridge_reference = self.labview.GetVIReference(self.Python_LV_Bridge_path)
            self.Python_LV_Bridge_reference.FPWinOpen = False
            self.Run_Python_LV_Bridge_reference = self.labview.GetVIReference(self.Run_Python_LV_Bridge_path)
            self.Run_Python_LV_Bridge_reference.FPWinOpen = False
            print(f"VI '{self.Python_LV_Bridge_path}' initialized.")
            self._run_bridge()
        except Exception as e:
            print(f"Error initializing VI: {e}")

    def _run_bridge(self):
        try:
            self.Run_Python_LV_Bridge_reference._FlagAsMethod("Run")
            self.Run_Python_LV_Bridge_reference.Run(False)
            print(f"VI '{self.Run_Python_LV_Bridge_path}' is running asynchronously.")
        except Exception as e:
            print(f"Error running VI: {e}")

    def disconnect(self):
        print("Disconnecting from LabVIEW (ActiveX)...")
        time.sleep(1)
        try:
            stop_ref = self.labview.GetVIReference(self.Stop_Python_LV_Bridge_path)
            stop_ref.FPWinOpen = False
            stop_ref._FlagAsMethod("Run")
            stop_ref.Run(False)
            print(f"VI '{self.Stop_Python_LV_Bridge_path}' is running asynchronously.")
        except Exception as e:
            print(f"Error stopping VI: {e}")

    def write_control(self, command):
        message = 'message'
        while message != '':
            self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue")
            message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
            time.sleep(0.05)

        self.Python_LV_Bridge_reference._FlagAsMethod("SetControlValue")
        self.Python_LV_Bridge_reference.SetControlValue("RemoteMessage", command)
        return 0

    def read_control(self, command, control_name):
        message = 'message'
        while message != '':
            self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue")
            message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
            time.sleep(0.05)

        self.Python_LV_Bridge_reference._FlagAsMethod("SetControlValue")
        self.Python_LV_Bridge_reference.SetControlValue("RemoteMessage", command)

        message = 'message'
        while message != '':
            self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue")
            message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
            time.sleep(0.05)

        return self.Python_LV_Bridge_reference.GetControlValue(control_name)
