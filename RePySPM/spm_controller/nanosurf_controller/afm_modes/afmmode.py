import nanosurf
from enum import Enum


class AFMModes(Enum):
    CONTACT = "Contact Mode"
    AM = "AM Mode"
    FM = "FM Mode"
    ORT = "Off Resonance Tapping Mode"


class ExcType(Enum):
    PZ = "Piezo"
    PT = "Photothermal"


class AFMMode:
    """
    A base class to represent different Atomic Force Microscopy (AFM) modes.

    This class serves as a foundation for specific AFM modes like AM Mode, FM Mode,
    Off resonance mode or Contact Mode. It provides a common interface and shared
    attributes that are used across different AFM modes.

    Attributes:
        mode_name (AFMModes): The name of the AFM mode.

    Methods:
        set_mode: Sets the SPM mode.
        get_mode: Gets the SPM mode.
        __repr__: Returns a string representation of the AFMMode object,
                  displaying the mode name.
    """

    def __init__(self, controller, contact, am, fm, ort):
        self.controller = controller
        self._app = controller._app

        self.contact = contact
        self.am = am
        self.fm = fm
        self.ort = ort

    def set_mode(self, mode):
        """Set the current mode to one of the available AFM modes."""
        if not isinstance(mode, AFMModes):
            raise ValueError("mode_name must be an instance of AFMModes.")

        mode_mapping = {
            AFMModes.CONTACT: nanosurf.SPM.OperatingMode.StaticAFM,
            AFMModes.AM:      nanosurf.SPM.OperatingMode.DynamicAFM,
            AFMModes.FM:      None,
            AFMModes.ORT:     nanosurf.SPM.OperatingMode.WaveMode,
        }

        value = mode_mapping.get(mode)
        if value is not None:
            self._app.OperatingMode.OperatingMode = value

        return 0

    def get_mode(self):
        """Retrieve the current mode object."""
        return self._app.OperatingMode.OperatingMode

    def __repr__(self):
        pass
