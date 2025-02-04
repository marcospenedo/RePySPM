from ..afmmode import ExcType, AFMModes

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

    def __init__(self):
        pass

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