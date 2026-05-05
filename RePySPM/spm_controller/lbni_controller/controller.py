import ipaddress

from .activex_backend import ActiveXBackend
from .tcp_backend import TCPBackend

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
from .afm_modes.am import AMMode
from .afm_modes.fm import FMMode
from .afm_modes.ort import OffResonanceMode
from .afm_modes.contact import ContactMode


def _parse_address(address):
    """Return ('tcp', host, port) or ('activex', root_path, None)."""
    # Strip trailing slashes/backslashes to avoid confusing the IP check
    candidate = address.strip().rstrip("\\/")
    host_part = candidate.split(":")[0]
    try:
        ipaddress.ip_address(host_part)
        # It is a valid IP address
        if ":" in candidate:
            host, port_str = candidate.rsplit(":", 1)
            return "tcp", host, int(port_str)
        return "tcp", candidate, 6340
    except ValueError:
        return "activex", address, None


class AFMController:
    def __init__(self, address):
        """Main controller class for an SPM instrument.

        Args:
            address: Either a filesystem path to the LabVIEW project root
                     (ActiveX connection) or an IP address string, optionally
                     with port (TCP connection), e.g. ``"192.168.1.1"`` or
                     ``"192.168.1.1:6340"``.
        """
        conn_type, host_or_path, port = _parse_address(address)

        if conn_type == "tcp":
            self._backend = TCPBackend(host_or_path, port)
        else:
            self._backend = ActiveXBackend(host_or_path)

        self._backend.connect()

        self.signals = Signals(self)
        self.scan_parameters = ScanParameters(self)
        self.scan_control = ScanControl(self)
        self.z_control = ZControlPID(self)
        self.motors = Motors(self)
        self.lasers = Lasers(self)
        self.image = AcquiredImage(self)
        self.sicm = Sicm(self)

        if conn_type == "activex":
            self.utils = Utils(self, host_or_path)
        else:
            self.utils = None  # FPGA direct access not available over TCP

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

    # ------------------------------------------------------------------
    # Public communication interface (delegates to backend)
    # ------------------------------------------------------------------

    def write_control(self, command):
        return self._backend.write_control(command)

    def read_control(self, command, control_name):
        return self._backend.read_control(command, control_name)

    def connect(self):
        self._backend.connect()

    def disconnect(self):
        self._backend.disconnect()
