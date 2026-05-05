class Sicm:
    """
    A class containing functions to control the SICM module of the LBNI OHC.

    This class provides methods to set and get SICM (Scanning Ion Conductance
    Microscopy) parameters via the OHC controller. Each parameter has a setter
    that validates the input and sends the command, and a getter that reads the
    current value from the hardware.

    Methods:
        set_setpoint: Sets the setpoint value (0–100).
        get_setpoint: Retrieves the current setpoint value.
        set_setpoint_stiff: Sets the setpoint stiffness value (0–100).
        get_setpoint_stiff: Retrieves the current setpoint stiffness value.
        set_approach_rate: Sets the approach rate (>= 0).
        get_approach_rate: Retrieves the current approach rate.
        set_retract_height: Sets the retract height (>= 0).
        get_retract_height: Retrieves the current retract height.
        set_retract_period: Sets the retract period (>= 0).
        get_retract_period: Retrieves the current retract period.
        set_adaptive_min: Sets the adaptive minimum value (0–100).
        get_adaptive_min: Retrieves the current adaptive minimum value.
        set_retract_delay: Sets the retract delay (>= 0).
        get_retract_delay: Retrieves the current retract delay.
        set_average_period: Sets the average period (>= 0).
        get_average_period: Retrieves the current average period.
        set_time_constant: Sets the time constant (>= 0).
        get_time_constant: Retrieves the current time constant.
        set_delta: Sets the delta value (>= 0).
        get_delta: Retrieves the current delta value.
        set_adaptive: Sets the adaptive mode (True or False).
        get_adaptive: Retrieves the current adaptive mode status.
    """

    def __init__(self, controller):
        self.controller = controller
        self._app = controller._app

    def set_setpoint(self, value: float):
        """Sets the setpoint value.

        Args:
            value (float): The setpoint value (must be between 0 and 100).

        Raises:
            ValueError: If the value is not a float or is outside the allowed range.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_setpoint(self):
        """Retrieves the current setpoint value.

        Returns:
            float: The current setpoint value.
        """
        pass

    def set_setpoint_stiff(self, value: float):
        """Sets the setpoint stiffness value.

        Args:
            value (float): The setpoint stiffness (must be between 0 and 100).

        Raises:
            ValueError: If the value is not a float or is outside the allowed range.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_setpoint_stiff(self):
        """Retrieves the current setpoint stiffness value.

        Returns:
            float: The current setpoint stiffness value.
        """
        pass

    def set_approach_rate(self, value: float):
        """Sets the approach rate.

        Args:
            value (float): The approach rate (must be a positive float or zero).

        Raises:
            ValueError: If the value is not a float or is not positive.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_approach_rate(self):
        """Retrieves the current approach rate.

        Returns:
            float: The current approach rate.
        """
        pass

    def set_retract_height(self, value: float):
        """Sets the retract height.

        Args:
            value (float): The retract height (must be a positive float or zero).

        Raises:
            ValueError: If the value is not a float or is not positive.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_retract_height(self):
        """Retrieves the current retract height.

        Returns:
            float: The current retract height.
        """
        pass

    def set_retract_period(self, value: float):
        """Sets the retract period.

        Args:
            value (float): The retract period (must be a positive float or zero).

        Raises:
            ValueError: If the value is not a float or is not positive.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_retract_period(self):
        """Retrieves the current retract period.

        Returns:
            float: The current retract period.
        """
        pass

    def set_adaptive_min(self, value: float):
        """Sets the adaptive minimum value.

        Args:
            value (float): The adaptive minimum (must be between 0 and 100).

        Raises:
            ValueError: If the value is not a float or is outside the allowed range.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_adaptive_min(self):
        """Retrieves the current adaptive minimum value.

        Returns:
            float: The current adaptive minimum value.
        """
        pass

    def set_retract_delay(self, value: float):
        """Sets the retract delay.

        Args:
            value (float): The retract delay (must be a float >= 0).

        Raises:
            ValueError: If the value is not a float or is negative.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_retract_delay(self):
        """Retrieves the current retract delay.

        Returns:
            float: The current retract delay.
        """
        pass

    def set_average_period(self, value: float):
        """Sets the average period.

        Args:
            value (float): The average period (must be a float >= 0).

        Raises:
            ValueError: If the value is not a float or is negative.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_average_period(self):
        """Retrieves the current average period.

        Returns:
            float: The current average period.
        """
        pass

    def set_time_constant(self, value: float):
        """Sets the time constant.

        Args:
            value (float): The time constant (must be a float >= 0).

        Raises:
            ValueError: If the value is not a float or is negative.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_time_constant(self):
        """Retrieves the current time constant.

        Returns:
            float: The current time constant.
        """
        pass

    def set_delta(self, value: float):
        """Sets the delta value.

        Args:
            value (float): The delta value (must be a float >= 0).

        Raises:
            ValueError: If the value is not a float or is negative.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_delta(self):
        """Retrieves the current delta value.

        Returns:
            float: The current delta value.
        """
        pass

    def set_adaptive(self, value: bool):
        """Sets the adaptive mode.

        Args:
            value (bool): Adaptive mode status (must be True or False).

        Raises:
            ValueError: If the value is not a boolean.

        Returns:
            int: Always returns 0.
        """
        pass

    def get_adaptive(self):
        """Retrieves the current adaptive mode status.

        Returns:
            bool: True if adaptive mode is enabled, False otherwise.
        """
        pass
