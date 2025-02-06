class Signals:
    """
    A class to handle the signals from a scanning system.

    This class provides methods to retrieve various signal measurements, 
    such as deflection, amplitude, and phase from the system. It allows 
    updating the current signals dynamically.

    Methods:
        get_vertical_deflection: Retrieves the vertical deflection signal.
        get_lateral_deflection: Retrieves the lateral deflection signal.
        get_photodiode_sum: Retrieves the photodiode sum signal.
        get_X: Retrieves the X-coordinate signal.
        get_Y: Retrieves the Y-coordinate signal.
        get_Z: Retrieves the Z-coordinate signal.
        get_sensor_X: Retrieves the X-coordinate sensor signal.
        get_sensor_Y: Retrieves the Y-coordinate sensor signal.
        get_sensor_Z: Retrieves the Z-coordinate sensor signal.
        get_measured_Z: Retrieves the height measured by the sensor signal.
        get_amplitude: Retrieves the amplitude signal.
        get_phase: Retrieves the phase signal.
        get_exc_amplitude: Retrieves the excitation amplitude signal.
        get_exc_phase: Retrieves the excitation phase signal.
    """

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController
        
    def get_vertical_deflection(self):
        """Retrieves the vertical deflection signal from the system."""
        pass

    def get_lateral_deflection(self):
        """Retrieves the lateral deflection signal from the system."""
        pass

    def get_photodiode_sum(self):
        """Retrieves the photodiode sum signal from the system."""
        pass

    def get_X(self):
        """Retrieves the X-coordinate signal from the system."""
        pass

    def get_Y(self):
        """Retrieves the Y-coordinate signal from the system."""
        pass

    def get_Z(self):
        """Retrieves the Z-coordinate signal from the system."""
        pass
    
    def get_sensor_X(self):
        """Retrieves the X-coordinate sensor signal from the system."""
        pass

    def get_sensor_Y(self):
        """Retrieves the Y-coordinate sensor signal from the system."""
        pass

    def get_sensor_Z(self):
        """Retrieves the Z-coordinate sensor signal from the system."""
        pass
    
    def get_measured_Z(self):
        """Retrieves the hight from the sensor signal from the system."""
        pass

    def get_amplitude(self):
        """Retrieves the amplitude signal from the system."""
        pass

    def get_phase(self):
        """Retrieves the phase signal from the system."""
        pass

    def get_exc_amplitude(self):
        """Retrieves the excitation amplitude signal from the system."""
        pass

    def get_exc_phase(self):
        """Retrieves the excitation phase signal from the system."""
        pass