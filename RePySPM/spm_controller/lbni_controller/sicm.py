from .commands import OHCcommands

class Sicm:
    """
    A class containing functions to control the SICM module of the LBNI OHC.

    Methods:
        
    """
    
    def __init__(self, controller):
        """
        Initializes the Utils class with the given controller.
        
        Args:
            controller: An instance of the AFMController handling communication.
        """
        
        self.controller = controller  # Store reference to AFMController
        
    def set_setpoint(self, value: float):
        """
        Sets the setpoint value.
    
        Args:
            value (float): The setpoint value (must be between 0 and 100).
    
        Raises:
            ValueError: If the value is not a float or is outside the allowed range.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or not (0 <= value <= 100):
            raise ValueError(f"Invalid setpoint: {value}. Must be a float between 0 and 100.")
    
        command = f"{OHCcommands.w_sic}Setpoint:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_setpoint(self):
        """
        Retrieves the current setpoint value.
    
        Returns:
            float: The current setpoint value.
        """
        control = "Setpoint"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)

    def set_setpoint_stiff(self, value: float):
        """
        Sets the setpoint stiffness value.
    
        Args:
            value (float): The setpoint stiffness (must be between 0 and 100).
    
        Raises:
            ValueError: If the value is not a float or is outside the allowed range.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or not (0 <= value <= 100):
            raise ValueError(f"Invalid SetpointStiff: {value}. Must be a float between 0 and 100.")
    
        command = f"{OHCcommands.w_sic}SetpointStiff:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_setpoint_stiff(self):
        """
        Retrieves the current setpoint stiffness value.
    
        Returns:
            float: The current setpoint stiffness value.
        """
        control = "SetpointStiff"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_approach_rate(self, value: float):
        """
        Sets the approach rate.
    
        Args:
            value (float): The approach rate (must be a positive float or zero).
    
        Raises:
            ValueError: If the value is not a float or is not positive.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Approach Rate: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Approach rate:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_approach_rate(self):
        """
        Retrieves the current approach rate.
    
        Returns:
            float: The current approach rate.
        """
        control = "Approach rate"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_retract_height(self, value: float):
        """
        Sets the retract height.
    
        Args:
            value (float): The retract height (must be a positive float or zero).
    
        Raises:
            ValueError: If the value is not a float or is not positive.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Retract Height: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Retract height:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_retract_height(self):
        """
        Retrieves the current retract height.
    
        Returns:
            float: The current retract height.
        """
        control = "Retract height"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_retract_period(self, value: float):
        """
        Sets the retract period.
    
        Args:
            value (float): The retract period (must be a positive float or zero).
    
        Raises:
            ValueError: If the value is not a float or is not positive.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Retract Period: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Retract period:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_retract_period(self):
        """
        Retrieves the current retract period.
    
        Returns:
            float: The current retract period.
        """
        control = "Retract period"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_adaptive_min(self, value: float):
        """
        Sets the adaptive minimum value.
    
        Args:
            value (float): The adaptive minimum (must be between 0 and 100).
    
        Raises:
            ValueError: If the value is not a float or is outside the allowed range.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or not (0 <= value <= 100):
            raise ValueError(f"Invalid Adaptive Min: {value}. Must be a float between 0 and 100.")
    
        command = f"{OHCcommands.w_sic}Adaptive min:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_adaptive_min(self):
        """
        Retrieves the current adaptive minimum value.
    
        Returns:
            float: The current adaptive minimum value.
        """
        control = "Adaptive min"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)

    def set_retract_delay(self, value: float):
        """
        Sets the retract delay.
    
        Args:
            value (float): The retract delay (must be a float >= 0).
    
        Raises:
            ValueError: If the value is not a float or is negative.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Retract Delay: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Retract delay:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_retract_delay(self):
        """
        Retrieves the current retract delay.
    
        Returns:
            float: The current retract delay.
        """
        control = "Retract delay"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_average_period(self, value: float):
        """
        Sets the average period.
    
        Args:
            value (float): The average period (must be a float >= 0).
    
        Raises:
            ValueError: If the value is not a float or is negative.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Average Period: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Average period:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_average_period(self):
        """
        Retrieves the current average period.
    
        Returns:
            float: The current average period.
        """
        control = "Average period"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_time_constant(self, value: float):
        """
        Sets the time constant.
    
        Args:
            value (float): The time constant (must be a float >= 0).
    
        Raises:
            ValueError: If the value is not a float or is negative.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Time Constant: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Time constant:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_time_constant(self):
        """
        Retrieves the current time constant.
    
        Returns:
            float: The current time constant.
        """
        control = "Time constant"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)
    
    
    def set_delta(self, value: float):
        """
        Sets the delta value.
    
        Args:
            value (float): The delta value (must be a float >= 0).
    
        Raises:
            ValueError: If the value is not a float or is negative.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, float) or value < 0:
            raise ValueError(f"Invalid Delta: {value}. Must be a positive float or zero.")
    
        command = f"{OHCcommands.w_sic}Delta:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_delta(self):
        """
        Retrieves the current delta value.
    
        Returns:
            float: The current delta value.
        """
        control = "Delta"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)

    def set_adaptive(self, value: bool):
        """
        Sets the adaptive mode.
    
        Args:
            value (bool): Adaptive mode status (must be True or False).
    
        Raises:
            ValueError: If the value is not a boolean.
    
        Returns:
            int: Always returns 0.
        """
        if not isinstance(value, bool):
            raise ValueError(f"Invalid Adaptive value: {value}. Must be True or False.")
    
        command = f"{OHCcommands.w_sic}Adaptive:{value}"
        self.controller.write_control(command)
    
        return 0        
    
    def get_adaptive(self):
        """
        Retrieves the current adaptive mode status.
    
        Returns:
            bool: True if adaptive mode is enabled, False otherwise.
        """
        control = "Adaptive"
        command = f"{OHCcommands.w_sic}{control}"
    
        return self.controller.read_control(command, control)

