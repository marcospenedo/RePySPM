# Importing directly from the package (__init__.py manages module paths)
import win32com.client  # Python ActiveX Client
import time

from .signals import Signals
from .scanparameters import ScanParameters
from .scancontrol import ScanControl
from .zcontrol import ZControlPID
from .motors import Motors
from .lasers import Lasers
from .image import AcquiredImage

# Import AFM modes from the updated structure
from .afm_modes import AFMMode, AFMModes, AMMode, FMMode, ContactMode, OffResonanceMode

class AFMController:        
    def __init__(self, Python_LV_Bridge_path, Run_Python_LV_Bridge_path):
        """Main controller class for an SPM instrument."""
        self.Python_LV_Bridge_path = Python_LV_Bridge_path
        self.Run_Python_LV_Bridge_path = Run_Python_LV_Bridge_path
        print(f"Will connect to path: {self.Python_LV_Bridge_path}")
        
        self.labview =  win32com.client.Dispatch("LabVIEW.Application")
        self.Python_LV_Bridge_reference = None
        self.Run_Python_LV_Bridge_reference = None
        self.connect()
        self.run_Python_LV_Bridge()
        
        self.signals = Signals(self)
        self.scan_parameters = ScanParameters(self)
        self.scan_control = ScanControl(self)
        self.z_control = ZControlPID(self)
        self.motors = Motors(self)
        self.lasers = Lasers(self)
        self.image = AcquiredImage(self)
        
        # Create instances of the AFM modes
        self.contact_mode = ContactMode(self)
        self.am_mode = AMMode(self)
        self.fm_mode = FMMode(self)
        self.ort_mode = OffResonanceMode(self)

        # AFMMode now acts as a mode manager containing the specific modes
        self.afmmode = AFMMode(
            self,
            contact=self.contact_mode,
            am=self.am_mode,
            fm=self.fm_mode,
            ort=self.ort_mode
        )

    def write_control(self, command):
       message = 'message'
       while message != '': # wait until previous message is read
           self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue") 
           message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
           time.sleep(0.05)
       
       self.Python_LV_Bridge_reference._FlagAsMethod("SetControlValue")
       self.Python_LV_Bridge_reference.SetControlValue("RemoteMessage", command)
       
       return 0
    
    def read_control(self, command, control_name):
        message = 'message'
        while message != '': # wait until previous message is read
            self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue") 
            message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
            time.sleep(0.05)
            
        self.Python_LV_Bridge_reference._FlagAsMethod("SetControlValue")
        self.Python_LV_Bridge_reference.SetControlValue("RemoteMessage", command) 
        self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue")
        
        message = 'message'
        while message != '': # wait until previous message is read
            self.Python_LV_Bridge_reference._FlagAsMethod("GetControlValue") 
            message = self.Python_LV_Bridge_reference.GetControlValue("RemoteMessage")
            time.sleep(0.05)
        
        return self.Python_LV_Bridge_reference.GetControlValue(control_name)

    def connect(self):
        """Establishes connection to SPM hardware."""
        print("Connecting to SPM system...")
        try:
            # Connect to LabVIEW
            labview = win32com.client.Dispatch("LabVIEW.Application")
    
            # Open the VI reference
            self.Python_LV_Bridge_reference = labview.GetVIReference(self.Python_LV_Bridge_path)
            self.Python_LV_Bridge_reference.FPWinOpen = False  # Ensure the front panel is not shown
            
            self.Run_Python_LV_Bridge_reference = labview.GetVIReference(self.Run_Python_LV_Bridge_path)
            self.Run_Python_LV_Bridge_reference.FPWinOpen = False  # Ensure the front panel is not shown
            
            print(f"VI '{self.Python_LV_Bridge_path}' initialized.")
        
        except Exception as e:
            print(f"Error initializing VI: {e}")
    
    def run_Python_LV_Bridge(self):
        """Run the VI asynchronously in a separate thread."""
        try:
            if self.Python_LV_Bridge_reference is None:
                print("VI reference is not initialized.")
                return
    
            # Run the VI asynchronously
            self.Run_Python_LV_Bridge_reference.Run(False)
            print("VI is running asynchronously.")
    
        except Exception as e:
            print(f"Error running VI in thread: {e}")


    def disconnect(self):
        """Disconnects from SPM hardware."""
        print("Disconnecting from SPM system...")

