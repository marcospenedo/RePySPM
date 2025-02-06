from ..afmmode import ExcType, AFMModes

class ContactMode():
    """
    A class to control the Contact Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the Contact Mode, 
    including the ability to manage the relative setpoint and update the deflection value.

    Methods:
        get_mode_parameters: Fetches the current Contact Mode parameters from the system.
        set_mode_parameters: Sets the Contact Mode parameters on the target system.
        update_deflection_value: Updates the deflection value to be used for relative setpoint calculation.
        get_relative_setpoint: Retrieves the relative setpoint mode.
        set_relative_setpoint: Sets the relative setpoint mode.
    """

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def get_mode_parameters(self):
        """Fetches the current Contact Mode parameters from the system."""
        pass

    def set_mode_parameters(self, relative_setpoint):
        """Sets the Contact Mode parameters on the target system.

        Args:
            relative_setpoint (bool): True if the setpoint is relative to the current deflection value, False otherwise.
        """
        pass

    def update_deflection_value(self):
        """Updates the deflection value to be used for relative setpoint calculation."""
        pass

    def get_relative_setpoint(self):
        """Retrieves the relative setpoint mode."""
        pass

    def set_relative_setpoint(self, value):
        """Sets the relative setpoint mode.

        Args:
            value (bool): True to enable relative setpoint, False to disable.
        """
        pass

    def __repr__(self):
        """Represents the ContactMode object as a string."""
        return "ContactMode()"
