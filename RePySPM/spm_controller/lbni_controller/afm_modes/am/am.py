from ..afmmode import ExcType, AFMModes

from ...commands import OHCcommands

class AMMode():
    """
    A class to control the Amplitude Modulation (AM) Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the AM Mode, 
    including the ability to manage excitation settings, lock-in amplifier parameters, and the free amplitude.

    Methods:
        get_mode_parameters: Fetches the current AM Mode parameters from the system.
        set_mode_parameters: Sets the AM Mode parameters on the target system.
        get_exc_type: Retrieves the excitation type used.
        set_exc_type: Sets the excitation type used.
        get_exc_amplitude: Retrieves the excitation amplitude.
        set_exc_amplitude: Sets the excitation amplitude.
        get_exc_offset: Retrieves the excitation offset.
        set_exc_offset: Sets the excitation offset.
        get_exc_frequency: Retrieves the excitation frequency.
        set_exc_frequency: Sets the excitation frequency.
        get_exc_phase: Retrieves the excitation phase.
        set_exc_phase: Sets the excitation phase.
        get_output: Retrieves the state of the output (on/off)
        set_output_ON: Sets the state of the output (on/off).
        get_lockin_bandwidth: Retrieves the lock-in amplifier bandwidth.
        set_lockin_bandwidth: Sets the lock-in amplifier bandwidth.
        get_lockin_order: Retrieves the lock-in amplifier order.
        set_lockin_order: Sets the lock-in amplifier order.
        get_free_amplitude: Retrieves the free amplitude of the cantilever.
        set_free_amplitude: Sets the free amplitude of the cantilever.
        do_sweep: Performs a frequency sweep based on the given parameters.
    """

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def get_mode_parameters(self):
        """Fetches the current AM Mode parameters from the system."""
        pass

    def set_mode_parameters(self, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude):
        """Sets the AM Mode parameters on the target system.

        Args:
            exc_type (ExcType): Type of excitation used (e.g., 'piezo', 'photothermal').
            exc_amplitude (float): Excitation amplitude in volts.
            exc_offset (float): Excitation offset in volts.
            exc_frequency (float): Excitation frequency in Hertz.
            exc_phase (float): Excitation phase in degrees (-180 to 180).
            lockin_bandwidth (float): Lock-in amplifier bandwidth in Hertz.
            lockin_order (int): Lock-in amplifier order (1, 2, 3, or 4).
            free_amplitude (float): Free amplitude of the cantilever in volts.
        """
        pass

    def get_exc_type(self):
        """Retrieves the excitation type used."""
        pass

    def set_exc_type(self, exc_type):
        """Sets the excitation type used.

        Args:
            exc_type (ExcType): Type of excitation (e.g., 'piezo', 'photothermal').
        """
        pass

    def get_exc_amplitude(self):
        """Retrieves the excitation amplitude."""
        
        control = "Amplitude (V)"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_exc_amplitude(self, value: float):
        """Sets the excitation amplitude.

        Args:
            value (float): Amplitude in volts.
        """
        if not isinstance(value, (int, float)) or not (0 <= value <= 10):
            raise ValueError(f"Invalid number of excitation amplitude: {value}. Must be a non-negative float.")
        
        command = f"{OHCcommands.w_exc}Amplitude (V):{value}"
        self.controller.write_control(command)
        
        return 0

    def get_exc_offset(self):
        """Retrieves the excitation offset."""
        
        control = "Offset (V)"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_exc_offset(self, value: float):
        """Sets the excitation offset.
    
        Args:
            value (float): Offset in volts (-10 to 10).
        """
        
        if not isinstance(value, (int, float)) or not (-10 <= value <= 10):
            raise ValueError(f"Invalid excitation offset: {value}. Must be a float between -10 and 10 volts.")
        
        command = f"{OHCcommands.w_exc}Offset (V):{value}"
        self.controller.write_control(command)
        
        return 0

    def get_exc_frequency(self):
        """Retrieves the excitation frequency."""
        
        control = "Frequency (Hz)"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_exc_frequency(self, value: float):
        """Sets the excitation frequency.

        Args:
            exc_frequency (float): Frequency in Hertz.
        """
        
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Invalid number of excitation amplitude: {value}. Must be a positive float.")
        
        command = f"{OHCcommands.w_exc}Offset (V):{value}"
        self.controller.write_control(command)
        
        return 0

    def get_exc_phase(self):
        """Retrieves the excitation phase."""
        
        control = "Phase Shift (°)"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_exc_phase(self, value: float):
        """Sets the excitation phase.
    
        Args:
            value (float): Phase in degrees (-180 to 180).
        """
        
        if not isinstance(value, (int, float)) or not (-180 <= value <= 180):
            raise ValueError(f"Invalid excitation phase: {value}. Must be a float between -180 and 180 degrees.")
        
        command = f"{OHCcommands.w_exc}Phase Shift (°):{value}"
        self.controller.write_control(command)
        
        return 0

    def get_output(self) -> bool:
        """Retrieves the state of the output (on/off)."""
        pass

    def set_output_ON(self, output_ON: bool):
        """Sets the state of the output (on/off).

        Args:
            output_ON (bool): True to turn ON, False to turn OFF.
        """
        if not isinstance(output_ON, bool):
            raise ValueError("output_ON must be a boolean value (True/False).")
        pass

    def get_lockin_bandwidth(self):
        """Retrieves the lock-in amplifier bandwidth."""
        
        control = "Bandwidth"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_lockin_bandwidth(self, value: float):
        """Sets the lock-in amplifier bandwidth.
    
        Args:
            value (float): Bandwidth in Hertz (must be a positive float greater than 0).
        """
        
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"Invalid bandwidth: {value}. Must be a positive float greater than 0.")
        
        command = f"{OHCcommands.w_exc}Bandwidth:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_lockin_order(self):
        """Retrieves the lock-in amplifier order."""
        
        control = "Order"
        command = f"{OHCcommands.r_exc}{control}"
        
        return self.controller.read_control(command, control)

    def set_lockin_order(self, value: int):
        """Sets the lock-in amplifier order.
    
        Args:
            value (int): Order of the lock-in amplifier (must be 1, 2, 3, or 4).
        """
        
        if value not in {1, 2, 3, 4}:
            raise ValueError(f"Invalid order: {value}. Must be 1, 2, 3, or 4.")
        
        command = f"{OHCcommands.w_exc}Order:{value}"
        self.controller.write_control(command)
        
        return 0

    def get_free_amplitude(self):
        """Retrieves the free amplitude of the cantilever."""
        pass

    def set_free_amplitude(self, free_amplitude):
        """Sets the free amplitude of the cantilever.

        Args:
            free_amplitude (float): Amplitude in volts.
        """
        pass

    def do_sweep(self, freq_init, freq_end, num_points):
        """
        Performs a frequency sweep based on the given parameters.

        Args:
            freq_init (float): Initial frequency in Hertz.
            freq_end (float): Final frequency in Hertz.
            num_points (int): Number of points in the sweep.

        Returns:
            list: Sweep data as a list of measured values.
        """
        pass

    def __repr__(self):
        """Represents the AMMode object as a string."""
        return "AMMode()"