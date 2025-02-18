from ..commands import OHCcommands

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
        self.controller = controller  # Store reference to AFMController
        
        self.contact = contact
        self.am = am
        self.fm = fm
        self.ort = ort
        
        # Default mode set to Contact Mode
        self.set_mode(AFMModes.CONTACT)

    def set_mode(self, mode):
        """Set the current mode to one of the available AFM modes."""
        if not isinstance(mode, AFMModes):
            raise ValueError("mode_name must be an instance of AFMModes.")
        
        # Define the mapping of AFMModes to command values
        mode_mapping = {
            AFMModes.CONTACT: "Contact Mode",
            AFMModes.AM: "AM Mode",
            AFMModes.FM: None,  # Not implemented
            AFMModes.ORT: "OR Tapping"
        }
    
        value = mode_mapping.get(mode)
    
        # Only send the command if the mode is implemented
        if value is not None:
            command = f"{OHCcommands.w_zcon}Mode:{value}"
            self.controller.write_control(command)
    
        return 0

    def get_mode(self):
        """Retrieve the current mode object."""
        
        control = "Mode"
        command = f"{OHCcommands.w_zcon}{control}"
        
        return self.controller.read_control(command, control)

    def __repr__(self):
        pass
