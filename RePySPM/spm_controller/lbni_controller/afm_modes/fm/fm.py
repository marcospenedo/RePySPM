from ..afmmode import ExcType, AFMModes

class FMMode():
    """
    A class to control the Frequency Modulation (FM) Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the FM Mode, 
    including the ability to manage excitation settings, lock-in amplifier parameters, and PLL gains.

    Methods:
        get_mode_parameters: Fetches the current FM Mode parameters from the system.
        set_mode_parameters: Sets the FM Mode parameters on the target system.
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
        get_pll_p_gain: Retrieves the PLL proportional gain.
        set_pll_p_gain: Sets the PLL proportional gain.
        get_pll_i_gain: Retrieves the PLL integral gain.
        set_pll_i_gain: Sets the PLL integral gain.
        get_pll_d_gain: Retrieves the PLL derivative gain.
        set_pll_d_gain: Sets the PLL derivative gain.
        get_pll_lock: Checks if the PLL is locked.
        set_pll_lock: Locks or unlocks the PLL.
        do_sweep: Performs a frequency sweep based on the given parameters.
    """

    def __init__(self):
        pass

    def get_mode_parameters(self):
        """Fetches the current FM Mode parameters from the system."""
        pass

    def set_mode_parameters(self, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll):
        """Sets the FM Mode parameters on the target system.

        Args:
            exc_type (ExcType): Type of excitation used (e.g., 'piezo', 'photothermal').
            exc_amplitude (float): Excitation amplitude in volts.
            exc_offset (float): Excitation offset in volts.
            exc_frequency (float): Excitation frequency in Hertz.
            exc_phase (float): Excitation phase in degrees (-180 to 180).
            lockin_bandwidth (float): Lock-in amplifier bandwidth in Hertz.
            lockin_order (int): Lock-in amplifier order (1, 2, 3, or 4).
            p_gain (float): PLL proportional gain.
            i_gain (float): PLL integral gain.
            d_gain (float): PLL derivative gain.
            lock_pll (bool): True to lock the PLL, False to unlock.
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
        pass

    def set_exc_amplitude(self, exc_amplitude):
        """Sets the excitation amplitude.

        Args:
            exc_amplitude (float): Amplitude in volts.
        """
        pass

    def get_exc_offset(self):
        """Retrieves the excitation offset."""
        pass

    def set_exc_offset(self, exc_offset):
        """Sets the excitation offset.

        Args:
            exc_offset (float): Offset in volts.
        """
        pass

    def get_exc_frequency(self):
        """Retrieves the excitation frequency."""
        pass

    def set_exc_frequency(self, exc_frequency):
        """Sets the excitation frequency.

        Args:
            exc_frequency (float): Frequency in Hertz.
        """
        pass

    def get_exc_phase(self):
        """Retrieves the excitation phase."""
        pass

    def set_exc_phase(self, exc_phase):
        """Sets the excitation phase.

        Args:
            exc_phase (float): Phase in degrees (-180 to 180).
        """
        pass

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
        pass

    def set_lockin_bandwidth(self, lockin_bandwidth):
        """Sets the lock-in amplifier bandwidth.

        Args:
            lockin_bandwidth (float): Bandwidth in Hertz.
        """
        pass

    def get_lockin_order(self):
        """Retrieves the lock-in amplifier order."""
        pass

    def set_lockin_order(self, lockin_order):
        """Sets the lock-in amplifier order.

        Args:
            lockin_order (int): Order of the lock-in amplifier (1, 2, 3, or 4).
        """
        pass

    def get_pll_p_gain(self):
        """Retrieves the PLL proportional gain."""
        pass

    def set_pll_p_gain(self, p_gain):
        """Sets the PLL proportional gain.

        Args:
            p_gain (float): Proportional gain.
        """
        pass

    def get_pll_i_gain(self):
        """Retrieves the PLL integral gain."""
        pass

    def set_pll_i_gain(self, i_gain):
        """Sets the PLL integral gain.

        Args:
            i_gain (float): Integral gain.
        """
        pass

    def get_pll_d_gain(self):
        """Retrieves the PLL derivative gain."""
        pass

    def set_pll_d_gain(self, d_gain):
        """Sets the PLL derivative gain.

        Args:
            d_gain (float): Derivative gain.
        """
        pass

    def get_pll_lock(self):
        """Checks if the PLL is locked."""
        pass

    def set_pll_lock(self, lock):
        """Locks or unlocks the PLL.

        Args:
            lock (bool): True to lock, False to unlock.
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
        """Represents the FMMode object as a string."""
        return "FMMode()"
