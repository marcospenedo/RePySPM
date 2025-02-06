class ZControlPID:
    """
    A class to control the PID parameters for a Z-axis control system.

    This class provides methods to initialize, get, and set PID control parameters, 
    ensuring proper validation and encapsulation of the PID gains, setpoint, and feedback 
    units used in the control process.

    Methods:
        get_zcontrolpid_parameters: Fetches the actual Z control PID parameters from the system.
        set_zcontrolpid_parameters: Sets PID parameters on the target system.
        get_p_gain: Retrieves the proportional gain of the PID controller.
        set_p_gain: Sets the proportional gain of the PID controller.
        get_i_gain: Retrieves the integral gain of the PID controller.
        set_i_gain: Sets the integral gain of the PID controller.
        get_d_gain: Retrieves the derivative gain of the PID controller.
        set_d_gain: Sets the derivative gain of the PID controller.
        get_setpoint: Retrieves the setpoint of the PID controller.
        set_setpoint: Sets the setpoint of the PID controller.
        get_units: Retrieves the feedback units.
        set_units: Sets the feedback units.
        get_feedback: Retrieves the feedback status.
        set_feedback: Sets the feedback status.
        get_afm_mode: Retrieves the AFM mode.
        set_afm_mode: Sets the AFM mode.
        get_zposition: Retrieve the actual Z scanner position.
        set_zposition: Move the tip to the desired Z position.
    """

    def get_zcontrolpid_parameters(self):
        """Fetches the actual Z control PID parameters from the system."""
        pass

    def set_zcontrolpid_parameters(self, p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode):
        """Sets PID parameters on the target system.

        Args:
            p_gain (float): Proportional gain of the PID controller.
            i_gain (float): Integral gain of the PID controller.
            d_gain (float): Derivative gain of the PID controller.
            setpoint (float): Desired setpoint for the PID controller.
            units (str): Units of the feedback signal (e.g., V, m, N).
            feedback (bool): Feedback status of the PID controller.
            afm_mode (AFMMode): Indicates the used AFM mode on the system.
        """
        pass

    def get_p_gain(self):
        """Retrieves the proportional gain of the PID controller."""
        pass

    def set_p_gain(self, p_gain):
        """Sets the proportional gain of the PID controller.

        Args:
            p_gain (float): Proportional gain.
        """
        pass

    def get_i_gain(self):
        """Retrieves the integral gain of the PID controller."""
        pass

    def set_i_gain(self, i_gain):
        """Sets the integral gain of the PID controller.

        Args:
            i_gain (float): Integral gain.
        """
        pass

    def get_d_gain(self):
        """Retrieves the derivative gain of the PID controller."""
        pass

    def set_d_gain(self, d_gain):
        """Sets the derivative gain of the PID controller.

        Args:
            d_gain (float): Derivative gain.
        """
        pass

    def get_setpoint(self):
        """Retrieves the setpoint of the PID controller."""
        pass

    def set_setpoint(self, setpoint):
        """Sets the setpoint of the PID controller.

        Args:
            setpoint (float): Desired setpoint.
        """
        pass

    def get_units(self):
        """Retrieves the feedback units."""
        pass

    def set_units(self, units):
        """Sets the feedback units.

        Args:
            units (str): Units of the feedback signal (e.g., V, m, N).
        """
        pass

    def get_feedback(self):
        """Retrieves the feedback status."""
        pass

    def set_feedback(self, feedback):
        """Sets the feedback status.

        Args:
            feedback (bool): Feedback status.
        """
        pass

    def get_afm_mode(self):
        """Retrieves the AFM mode."""
        pass

    def set_afm_mode(self, afm_mode):
        """Sets the AFM mode.

        Args:
            afm_mode (AFMMode): The AFM mode to be set.
        """
        pass

    def get_zposition(self):
        """Retrieves the actual Z scanner position."""
        pass

    def set_zposition(self, z_position, forced=False):
        """Moves the tip to the desired Z position.

        Args:
            z_position (float): Desired Z position.
            forced (bool): Whether to force the position update if feedback is active.
        """
        pass

    def __repr__(self):
        """Represents the ZControlPID object as a string."""
        return "ZControlPID()"
