import nanosurf

from .signals import Signals
from .scanparameters import ScanParameters
from .scancontrol import ScanControl
from .zcontrol import ZControlPID
from .motors import Motors
from .lasers import Lasers
from .image import AcquiredImage
from .utils import Utils
from .sicm import Sicm

from .afm_modes.afmmode import AFMMode, AFMModes, ExcType
from .afm_modes.am.am import AMMode
from .afm_modes.fm.fm import FMMode
from .afm_modes.ort.ort import OffResonanceMode
from .afm_modes.contact.contact import ContactMode


class AFMController:
    def __init__(self):
        """Main controller class for a Nanosurf SPM instrument."""
        print("Connecting to Nanosurf software...")
        self._spm = nanosurf.SPM()
        self._app = self._spm.application
        print("Connected to Nanosurf.")

        self.signals = Signals(self)
        self.scan_parameters = ScanParameters(self)
        self.scan_control = ScanControl(self)
        self.z_control = ZControlPID(self)
        self.motors = Motors(self)
        self.lasers = Lasers(self)
        self.image = AcquiredImage(self)
        self.utils = Utils(self)
        self.sicm = Sicm(self)

        self.contact_mode = ContactMode(self)
        self.am_mode = AMMode(self)
        self.fm_mode = FMMode(self)
        self.ort_mode = OffResonanceMode(self)

        self.afmmode = AFMMode(
            self,
            contact=self.contact_mode,
            am=self.am_mode,
            fm=self.fm_mode,
            ort=self.ort_mode,
        )

    def disconnect(self):
        """Disconnects from Nanosurf software."""
        print("Disconnecting from Nanosurf software...")
        del self._spm
        self._spm = None
        self._app = None
        print("Nanosurf disconnected.")
