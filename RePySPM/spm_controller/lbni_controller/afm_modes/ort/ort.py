from ..afmmode import ExcType, AFMModes

class OffResonanceMode():
    """
    A class to control the Off Resonance Tapping (ORT) mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the Off Resonance Tapping mode, 
    ensuring proper validation and encapsulation of the excitation type, amplitude, frequency, phase, and offset 
    used in this mode.

    Methods:
        get_mode_parameters: Fetches the current Off Resonance Tapping mode parameters from the system.
        set_mode_parameters: Sets the Off Resonance Tapping mode parameters on the target system.
        get_exc_type: Retrieves the excitation type used.
        set_exc_type: Sets the excitation type used.
        get_exc_amplitude: Retrieves the excitation amplitude.
        set_exc_amplitude: Sets the excitation amplitude.
        get_exc_frequency: Retrieves the excitation frequency.
        set_exc_frequency: Sets the excitation frequency.
        get_exc_phase: Retrieves the excitation phase.
        set_exc_phase: Sets the excitation phase.
        get_exc_offset: Retrieves the excitation offset.
        set_exc_offset: Sets the excitation offset.
        get_output: Retrieves the state of the output (on/off)
        set_output_ON: Sets the state of the output (on/off).
        subtract_background: Subtracts the background from the vertical deflection signal of the cantilevers.
    """

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def get_mode_parameters(self):
        """Fetches the current Off Resonance Tapping mode parameters from the system."""
        pass

    def set_mode_parameters(self, exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset):
        """Sets the Off Resonance Tapping mode parameters on the target system.

        Args:
            exc_type (ExcType): Type of excitation used (e.g., 'piezo', 'photothermal').
            exc_amplitude (float): Amplitude of the excitation signal in volts.
            exc_frequency (float): Frequency of the excitation signal in Hertz.
            exc_phase (float): Phase of the excitation signal in degrees (-180 to 180).
            exc_offset (float): Offset of the excitation signal in volts.
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
            exc_amplitude (float): Amplitude of the excitation signal in volts.
        """
        pass

    def get_exc_frequency(self):
        """Retrieves the excitation frequency."""
        pass

    def set_exc_frequency(self, exc_frequency):
        """Sets the excitation frequency.

        Args:
            exc_frequency (float): Frequency of the excitation signal in Hertz.
        """
        pass

    def get_exc_phase(self):
        """Retrieves the excitation phase."""
        pass

    def set_exc_phase(self, exc_phase):
        """Sets the excitation phase.

        Args:
            exc_phase (float): Phase of the excitation signal in degrees (-180 to 180).
        """
        pass

    def get_exc_offset(self):
        """Retrieves the excitation offset."""
        pass

    def set_exc_offset(self, exc_offset):
        """Sets the excitation offset.

        Args:
            exc_offset (float): Offset of the excitation signal in volts.
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
    
    def subtract_background(self, num_averages):
        """
        Subtracts the background from the vertical deflection signal of the cantilevers and returns a list of background values.

        Args:
            num_averages (int): Number of averages to calculate the background signal.

        Returns:
            list: Background values subtracted from the vertical deflection signal.
        """
        
        pass

    def __repr__(self):
        """Represents the OffResonanceMode object as a string."""
        return "OffResonanceMode()"
