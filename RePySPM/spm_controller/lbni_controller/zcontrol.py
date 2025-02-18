from .commands import OHCcommands

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
        retract: Withdraw from the surface.
        get_afm_mode: Retrieves the AFM mode.
        set_afm_mode: Sets the AFM mode.
        get_zposition: Retrieve the actual Z scanner position.
        set_zposition: Move the tip to the desired Z position.
    """
    
    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def get_zcontrolpid_parameters(self):
        """Fetches the actual Z control PID parameters from the system."""
        return [self.get_p_gain(), self.get_i_gain(), self.get_d_gain(), self.get_setpoint(), self.get_units(), self.get_feedback(), self.get_afm_mode()]

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
        
        self.set_afm_mode(afm_mode)
        self.set_p_gain(p_gain)
        self.set_i_gain(i_gain)
        self.set_d_gain(d_gain)
        self.set_units(units)
        self.set_setpoint(setpoint)
        self.set_feedback(feedback)
        
        return 0

    def get_p_gain(self):
        """Retrieves the proportional gain of the PID controller."""
        
        control = "PID"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)[1]

    def set_p_gain(self, p_gain):
        """Sets the proportional gain of the PID controller.

        Args:
            p_gain (float): Proportional gain.
        """
        
        command = f"{OHCcommands.w_zcon}PID:P Gain:{p_gain}"
            
        self.controller.write_control(command)
        
        return 0

    def get_i_gain(self):
        """Retrieves the integral gain of the PID controller."""
        
        control = "PID"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)[2]

    def set_i_gain(self, i_gain):
        """Sets the integral gain of the PID controller.

        Args:
            i_gain (float): Integral gain.
        """
                
        command = f"{OHCcommands.w_zcon}PID:I Gain:{i_gain}"
            
        self.controller.write_control(command)
        
        return 0

    def get_d_gain(self):
        """Retrieves the derivative gain of the PID controller."""
        
        return -1

    def set_d_gain(self, d_gain):
        """Sets the derivative gain of the PID controller.

        Args:
            d_gain (float): Derivative gain.
        """
        
        return -1

    def get_setpoint(self):
        """Retrieves the setpoint of the PID controller."""
        
        control = "PID"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)[0]

    def set_setpoint(self, setpoint):
        """Sets the setpoint of the PID controller.

        Args:
            setpoint (float): Desired setpoint.
        """
                
        command = f"{OHCcommands.w_zcon}PID:Setpoint:{setpoint}"
            
        self.controller.write_control(command)
        
        return 0

    def get_units(self):
        """Retrieves the feedback units."""
                
        control = "Units"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)

    def set_units(self, units):
        """Sets the feedback units.

        Args:
            units (str): Units of the feedback signal (e.g., V, m, N).
        """
                
        command = f"{OHCcommands.w_zcon}Units:{units}"
            
        self.controller.write_control(command)
        
        return 0

    def get_feedback(self):
        """Retrieves the feedback status."""
        
        control = "Feedback On"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)

    def set_feedback(self, feedback):
        """Sets the feedback status.

        Args:
            feedback (bool): Feedback status.
        """
        
        command = f"{OHCcommands.w_zcon}Feedback On:{feedback}"
            
        self.controller.write_control(command)
        
        return 0
    
    def retract(self):
        """Withdraw from the surface."""
        
        command = f"{OHCcommands.w_zcon}Withdraw:True"
            
        self.controller.write_control(command)
        
        return 0

    def get_afm_mode(self):
        """Retrieves the AFM mode."""
                
        control = "Mode"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)

    def set_afm_mode(self, afm_mode):
        """Sets the AFM mode.

        Args:
            afm_mode (AFMMode): The AFM mode to be set.
        """
                
        command = f"{OHCcommands.w_zcon}{afm_mode}"
            
        self.controller.write_control(command)
        
        return 0

    def get_zposition(self):
        """Retrieves the actual Z scanner position."""
                
        control = "Z (m)"
        command = f"{OHCcommands.r_zcon}{control}"
        
        return self.controller.read_control(command, control)

    def set_zposition(self, z_position, forced=False):
        """Moves the tip to the desired Z position.

        Args:
            z_position (float): Desired Z position.
            forced (bool): Whether to force the position update if feedback is active.
        """
        command = f"{OHCcommands.w_zcon}Z (m):{z_position}"
        
        if forced:
            self.set_feedback(False)
            self.controller.write_control(command)
        else:
            if not self.get_feedback():
                self.controller.write_control(command)
        
        return 0

    def __repr__(self):
        """Represents the ZControlPID object as a string."""
        return "ZControlPID()"
