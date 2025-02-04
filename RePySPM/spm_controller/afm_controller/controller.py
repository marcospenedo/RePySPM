# Importing directly from the package (__init__.py manages module paths)
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
    def __init__(self, connection_params=None):
        """Main controller class for an SPM instrument."""
        self.signals = Signals()
        self.scan_parameters = ScanParameters()
        self.scan_control = ScanControl()
        self.z_control = ZControlPID()
        self.motors = Motors()
        self.lasers = Lasers()
        self.image = AcquiredImage()
        
        # Create instances of the AFM modes
        self.contact_mode = ContactMode()
        self.am_mode = AMMode()
        self.fm_mode = FMMode()
        self.ort_mode = OffResonanceMode()

        # AFMMode now acts as a mode manager containing the specific modes
        self.afmmode = AFMMode(
            contact=self.contact_mode,
            am=self.am_mode,
            fm=self.fm_mode,
            ort=self.ort_mode
        )

    def connect(self):
        """Establishes connection to SPM hardware."""
        print("Connecting to SPM system...")

    def disconnect(self):
        """Disconnects from SPM hardware."""
        print("Disconnecting from SPM system...")
