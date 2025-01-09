import os
import re
import math
from enum import Enum


class AFMModes(Enum):
    CONTACT = "Contact Mode"
    AM = "AM Mode"
    FM = "FM Mode"
    ORT = "Off Resonance Tapping Mode"


class ExcType(Enum):
    PZ = "Piezo"
    PT = "Photothermal"


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
    
    def __init__(self):
        pass

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
        return self.__phase

    def get_exc_amplitude(self):
        """Retrieves the excitation amplitude signal from the system."""
        return self.__exc_amplitude

    def get_exc_phase(self):
        """Retrieves the excitation phase signal from the system."""
        pass


class ScanParameters:
    """
    A class to handle scan parameters for a scanning system.

    This class provides methods to set and get scan parameters. The implementation
    allows for later integration of functionality to ensure that the parameters stay
    within the defined bounds and that the scan area complies with the system's
    specifications.

    Methods:
        set_scan_parameters: Sets all scan parameters for the system.
        get_scan_parameters: Retrieves all current scan parameters from the system.
        get_width: Retrieves the current width of the scan area.
        set_width: Sets the width of the scan area.
        get_height: Retrieves the current height of the scan area.
        set_height: Sets the height of the scan area.
        get_rotation: Retrieves the current rotation of the scan area.
        set_rotation: Sets the rotation of the scan area.
        get_offset_x: Retrieves the current X offset of the scan area.
        set_offset_x: Sets the X offset of the scan area.
        get_offset_y: Retrieves the current Y offset of the scan area.
        set_offset_y: Sets the Y offset of the scan area.
        get_scan_speed: Retrieves the current scan speed.
        set_scan_speed: Sets the scan speed.
        get_pixels_x: Retrieves the number of pixels in the X-axis.
        set_pixels_x: Sets the number of pixels in the X-axis.
        get_pixels_y: Retrieves the number of pixels in the Y-axis.
        set_pixels_y: Sets the number of pixels in the Y-axis.
        get_tilt_x: Retrieves the tilt in the X-axis.
        set_tilt_x: Sets the tilt in the X-axis.
        get_tilt_y: Retrieves the tilt in the Y-axis.
        set_tilt_y: Sets the tilt in the Y-axis.
        get_close_loopXY: Retrieves the status of close-loop control for the XY plane.
        set_close_loopXY: Sets the status of close-loop control for the XY plane.
        get_close_loopZ: Retrieves the status of close-loop control for the Z-axis.
        set_close_loopZ: Sets the status of close-loop control for the Z-axis.
    """

    def __init__(self):
        pass

    @classmethod
    def init_scan_parameters_with_params(
        cls, width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ
    ):
        """Initialize the instance with specific values for all attributes"""
        # Initialize the instance with specific values for all attributes
        instance = cls()
        instance.set_scan_parameters(
            width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ
        )
        return instance

    def set_scan_parameters(
        self, width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ
    ):
        """Sets all scan parameters on the system."""
        pass

    def get_scan_parameters(self):
        """Retrieves all current scan parameters from the system."""
        pass

    def get_width(self):
        """Retrieves the current width of the scan area."""
        pass

    def set_width(self, value):
        """Sets the width of the scan area."""
        pass

    def get_height(self):
        """Retrieves the current height of the scan area."""
        pass

    def set_height(self, value):
        """Sets the height of the scan area."""
        pass

    def get_rotation(self):
        """Retrieves the current rotation of the scan area."""
        pass

    def set_rotation(self, value):
        """Sets the rotation of the scan area."""
        pass

    def get_offset_x(self):
        """Retrieves the current X offset of the scan area."""
        pass

    def set_offset_x(self, value):
        """Sets the X offset of the scan area."""
        pass

    def get_offset_y(self):
        """Retrieves the current Y offset of the scan area."""
        pass

    def set_offset_y(self, value):
        """Sets the Y offset of the scan area."""
        pass

    def get_scan_speed(self):
        """Retrieves the current scan speed."""
        pass

    def set_scan_speed(self, value):
        """Sets the scan speed."""
        pass

    def get_pixels_x(self):
        """Retrieves the number of pixels in the X-axis."""
        pass

    def set_pixels_x(self, value):
        """Sets the number of pixels in the X-axis."""
        pass

    def get_pixels_y(self):
        """Retrieves the number of pixels in the Y-axis."""
        pass

    def set_pixels_y(self, value):
        """Sets the number of pixels in the Y-axis."""
        pass

    def get_tilt_x(self):
        """Retrieves the tilt in the X-axis."""
        pass

    def set_tilt_x(self, value):
        """Sets the tilt in the X-axis."""
        pass

    def get_tilt_y(self):
        """Retrieves the tilt in the Y-axis."""
        pass

    def set_tilt_y(self, value):
        """Sets the tilt in the Y-axis."""
        pass

    def get_close_loopXY(self):
        """Retrieves the status of close-loop control for the XY plane."""
        pass

    def set_close_loopXY(self, value):
        """Sets the status of close-loop control for the XY plane."""
        pass

    def get_close_loopZ(self):
        """Retrieves the status of close-loop control for the Z-axis."""
        pass

    def set_close_loopZ(self, value):
        """Sets the status of close-loop control for the Z-axis."""
        pass

    def __repr__(self):
        """Represents the ScanParameters object as a string."""
        return "ScanParameters()"


class ScanControl:
    """
    A class to control scanning operations for a given system.

    This class provides methods to start, stop, and manage scanning operations,
    including setting parameters such as the scan direction, bounce mode, continuous scan,
    auto-save options, and file paths.

    Methods:
        get_scan_control_parameters: Retrieves the current scanning parameters from the system.
        set_scan_control_parameters: Sets the scanning parameters on the system.
        scan_up: Starts scanning in the upward direction.
        scan_down: Starts scanning in the downward direction.
        scan_bouncing: Starts bouncing scan.
        scan_stop: Stops scanning.
        scan_pause: Pauses scanning.
        scan_resume: Resumes scanning.
        scan_continuous: Enables or disables continuous scan.
        get_scan_direction: Retrieves the current scan direction.
        scan_auto_save: Enables or disables auto-save.
        scan_save_now: Saves current scan data immediately.
        is_scanning: Checks if scanning is active.
        is_paused: Checks if scanning is paused.
        isContinuousScan: Checks if continuous scanning is enabled.
        isAutoSave: Checks if auto-save is enabled.
        get_pixel_pos: Retrieves the current scanning XY pixel numbers.
        get_xyposition: Retrieves the current XY scanner position.
        set_xyposition: Moves the tip to the desired XY position.
        get_path: Retrieves the path associated with the scan.
        set_path: Sets the path associated with the scan.
        get_file_name: Retrieves the file name for the scan.
        set_file_name: Sets the file name for the scan.
        do_ramp_absolute: Performs a Z ramp with absolute starting and ending points.
        do_ramp_absolute_length: Performs a Z ramp with absolute starting point and ramp length.
        do_ramp_absolute_trig: Performs a Z ramp with an absolute starting point and a trigger-based endpoint.
        do_ramp_relative_length: Performs a Z ramp relative to the actual position with a specified length.
        do_ramp_relative_trig: Performs a Z ramp relative to the actual position with a trigger-based endpoint.
        get_path_ramp: Retrieves the path for ramp data storage.
        set_path_ramp: Sets the path for ramp data storage.
        get_file_name_ramp: Retrieves the file name for ramp data storage.
        set_file_name_ramp: Sets the file name for ramp data storage.
    """

    def __init__(self):
        pass

    @classmethod
    def init_scan_control_with_params(cls, isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name):
        """Initialize the instance with specific values for all attributes."""
        instance = cls()
        instance.set_scan_control_parameters(isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name)
        return instance

    def get_scan_control_parameters(self):
        """Retrieves the current scanning parameters from the system."""
        pass

    def set_scan_control_parameters(self, isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name):
        """Sets the scanning parameters on the system."""
        pass

    def scan_up(self):
        """Starts scanning in the upward direction."""
        pass

    def scan_down(self):
        """Starts scanning in the downward direction."""
        pass

    def scan_bouncing(self):
        """Starts bouncing scan."""
        pass

    def scan_stop(self):
        """Stops scanning."""
        pass

    def scan_pause(self):
        """Pauses scanning."""
        pass

    def scan_resume(self):
        """Resumes scanning."""
        pass

    def scan_continuous(self, value):
        """Enables or disables continuous scan.

        Args:
            value (bool): True to enable continuous scan, False to disable.
        """
        pass

    def get_scan_direction(self):
        """Retrieves the current scan direction."""
        pass

    def scan_auto_save(self, value):
        """Enables or disables auto-save.

        Args:
            value (bool): True to enable auto-save, False to disable.
        """
        pass

    def scan_save_now(self):
        """Saves current scan data immediately."""
        pass

    def is_scanning(self):
        """Checks if scanning is active."""
        pass

    def is_paused(self):
        """Checks if scanning is paused."""
        pass
    
    def isContinuousScan(self):
        """Checks if continuous scanning is enabled."""
        pass

    def isAutoSave(self):
        """Checks if auto-save is enabled."""
        pass

    def get_pixel_pos(self):
        """Retrieves the current scanning XY pixel numbers."""
        pass

    def get_xyposition(self):
        """Retrieves the current XY scanner position."""
        pass

    def set_xyposition(self, x, y, forced=False):
        """Moves the tip to the desired XY position.

        Args:
            x (float): Desired X position in meters.
            y (float): Desired Y position in meters.
            forced (bool): If True, scanning stops to move the tip.
        """
        pass

    def get_path(self):
        """Retrieves the path associated with the scan."""
        pass

    def set_path(self, path):
        """Sets the path associated with the scan.

        Args:
            path (str): Path for the scan.
        """
        pass

    def get_file_name(self):
        """Retrieves the file name for the scan."""
        pass

    def set_file_name(self, file_name):
        """Sets the file name for the scan.

        Args:
            file_name (str): Name of the file.
        """
        pass

    def do_ramp_absolute(self, init, end, N, speed_f, speed_b, wait_s):
        """
        Performs a Z ramp with absolute starting and ending points.

        Args:
            init (float): Initial position in meters.
            end (float): Final position in meters.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second.
            speed_b (float): Backward speed in meters per second.
            wait_s (float): Waiting time at the turnaround point in seconds.
        """
        pass

    def do_ramp_absolute_length(self, init, length, N, speed_f, speed_b, wait_s):
        """
        Performs a Z ramp with absolute starting point and ramp length.

        Args:
            init (float): Initial position in meters.
            length (float): Length of the Z movement in meters.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second.
            speed_b (float): Backward speed in meters per second.
            wait_s (float): Waiting time at the turnaround point in seconds.
        """
        pass

    def do_ramp_absolute_trig(self, init, trig_val, trig_signal, trig_sig, N, speed_f, speed_b, wait_s):
        """
        Performs a Z ramp with an absolute starting point and a trigger-based endpoint.

        Args:
            init (float): Initial position in meters.
            trig_val (float): Trigger value that determines when to end the ramp.
            trig_signal (str): The signal used for triggering (e.g., force or voltage).
            trig_sig (str): Trigger condition ('>' or '<') to stop the ramp.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second.
            speed_b (float): Backward speed in meters per second.
            wait_s (float): Waiting time at the turnaround point in seconds.
        """
        pass

    def do_ramp_relative_length(self, init, length, N, speed_f, speed_b, wait_s):
        """
        Performs a Z ramp relative to the actual position with a specified length.

        Args:
            init (float): Initial position relative to the actual position in meters.
            length (float): Length of the Z movement in meters.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second.
            speed_b (float): Backward speed in meters per second.
            wait_s (float): Waiting time at the turnaround point in seconds.
        """
        pass

    def do_ramp_relative_trig(self, init, trig_val, trig_signal, trig_sig, N, speed_f, speed_b, wait_s):
        """
        Performs a Z ramp relative to the actual position with a trigger-based endpoint.

        Args:
            init (float): Initial position relative to the actual position in meters.
            trig_val (float): Trigger value that determines when to end the ramp.
            trig_signal (str): The signal used for triggering (e.g., force or voltage).
            trig_sig (str): Trigger condition ('>' or '<') to stop the ramp.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second.
            speed_b (float): Backward speed in meters per second.
            wait_s (float): Waiting time at the turnaround point in seconds.
        """
        pass

    def get_path_ramp(self):
        """Retrieves the path for ramp data storage."""
        pass

    def set_path_ramp(self, path):
        """Sets the path for ramp data storage.

        Args:
            path (str): Path for ramp data.
        """
        pass

    def get_file_name_ramp(self):
        """Retrieves the file name for ramp data storage."""
        pass

    def set_file_name_ramp(self, file_name):
        """Sets the file name for ramp data storage.

        Args:
            file_name (str): Name of the file for ramp data.
        """
        pass

    def __repr__(self):
        """Represents the ScanControl object as a string."""
        return "ScanControl()"


class AFMMode:
    """
    A base class to represent different Atomic Force Microscopy (AFM) modes.
    
    This class serves as a foundation for specific AFM modes like AM Mode, FM Mode, 
    Off resonance mode or Contact Mode. It provides a common interface and shared 
    attributes that are used across different AFM modes.
    
    Attributes:
        __mode_name (AFMModes): The name of the AFM mode. Each subclass should set this 
                        to the specific mode it represents, such as "AM Mode" or "FM Mode".
    
    Methods:
        __repr__: Returns a string representation of the AFMMode object, 
                  displaying the mode name.
    """
    
    def __init__(self, mode_name):
        if not isinstance(mode_name, AFMModes):
            raise ValueError("mode_name must be an instance of AFMModes.")
        self.__mode_name = mode_name

    def __repr__(self):
        return f"AFMMode(mode_name={self.__mode_name})"


class AMMode(AFMMode):
    """
    A class to control the Amplitude Modulation (AM) Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the AM Mode, 
    including the ability to manage excitation settings, lock-in amplifier parameters, and the free amplitude.

    Attributes:
        __exc_type (ExcType): Type of excitation used, either 'piezo' or 'photothermal'.
        __exc_amplitude (float): Amplitude of the excitation signal in volts.
        __exc_offset (float): Offset of the excitation signal in volts.
        __exc_frequency (float): Frequency of the excitation signal in Hertz.
        __exc_phase (float): Phase of the excitation signal in degrees, ranging from -180 to 180.
        __lockin_bandwidth (float): Bandwidth of the lock-in amplifier in Hertz.
        __lockin_order (int): Order of the lock-in amplifier, restricted to values 1, 2, 3, or 4.
        __free_amplitude (float): Free amplitude of the cantilever in volts.

    Methods:
        init_mode_with_params: Initializes the instance with specific values for all attributes and returns the instance.
        get_mode_parameters: Fetches the current AM Mode parameters from the system.
        set_mode_parameters: Sets the AM Mode parameters on the target system.
        do_sweep: Performs a frequency sweep based on the given parameters.
    """       
        
    def __init__(self):
        super().__init__(AFMModes.AM)
        self.get_mode_parameters()
    
    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()       
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude)
        return instance  
    
    def get_mode_parameters(self):
        """Get the actual mode parameters"""
        # self.__exc_type = ExcType.PZ # Read that from target system [piezo, photothermal]
        # self.__exc_amplitude = 0  # Read that from target system [V]
        # self.__exc_offset = 0  # Read that from target system [V]
        # self.__exc_frequency = 0  # Read that from target system [Hz]
        # self.__exc_phase = 0  # Read that from target system [deg]
        # self.__lockin_bandwidth = 0  # Read that from target system [Hz]
        # self.__lockin_order = 1 # Read that from target system 
        # self.__free_amplitude = 0 # Read that from target system [V]

        # Retrieve these values from the target 
        
        pass
    
    def set_mode_parameters(self, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude):
        """Set the contact mode parameters on the target system"""
        self.__exc_type = exc_type # [piezo, photothermal]
        self.__exc_amplitude = exc_amplitude
        self.__exc_offset = exc_offset
        self.__exc_frequency = exc_frequency
        self.__exc_phase = exc_phase
        self.__lockin_bandwidth = lockin_bandwidth
        self.__lockin_order = lockin_order
        self.__free_amplitude = free_amplitude
        
        # Update these values on the target system if necessary   

    @property
    def exc_type(self):
        """The 'exc_type' property getter"""
        return self.__exc_type
    
    @exc_type.setter
    def exc_type(self, value):
        """The 'exc_type' property setter"""
        if not isinstance(value, ExcType):
            raise ValueError("exc_type must be an instance of ExcType.")
        self.__exc_type = value
        # Set the mode parameter on the target system
        
    @property
    def exc_amplitude(self):
        """The 'exc_amplitude' property getter"""
        return self.__exc_amplitude
    
    @exc_amplitude.setter
    def exc_amplitude(self, value):
        """The 'exc_amplitude' property setter"""
        if 0 <= value:
            self.__exc_amplitude = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation amplitude must be equal to or greater than 0.")     
   
    @property
    def exc_offset(self):
        """The 'exc_offset' property getter"""
        return self.__exc_offset
    
    @exc_offset.setter
    def exc_offset(self, value):
        """The 'exc_offset' property setter"""
        self.__exc_offset = value
        # Set the mode parameter on the target system  
        
    @property
    def exc_frequency(self):
        """The 'exc_frequency' property getter"""
        return self.__exc_frequency
    
    @exc_frequency.setter
    def exc_frequency(self, value):
        """The 'exc_frequency' property setter"""
        if 0 < value:
            self.__exc_frequency = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation frequency must be greater than 0.")   
            
    @property
    def exc_phase(self):
        """The 'exc_phase' property getter"""
        return self.__exc_phase
    
    @exc_phase.setter
    def exc_phase(self, value):
        """The 'exc_phase' property setter"""
        if -180 <= value <= 180:
            self.__exc_phase= value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation phase must be between -180 and 180 degrees.")     
    
    @property
    def lockin_bandwidth(self):
        """The 'lockin_bandwidth' property getter"""
        return self.__lockin_bandwidth
    
    @lockin_bandwidth.setter
    def lockin_bandwidth(self, value):
        """The 'lockin_bandwidth' property setter"""
        if 0 <= value:
            self.__lockin_bandwidth = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("Lock-in bandwidth must be equal to or greater than 0.")    
            
    @property
    def lockin_order(self):
        """The 'lockin_order' property getter"""
        return self.__lockin_order
    
    @lockin_order.setter
    def lockin_order(self, value):
        """The 'lockin_order' property setter"""
        if value in [1, 2, 3, 4]:
            self.__lockin_order = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("Lockin order must be 1, 2, 3, or 4.")           

    def do_sweep(self, freq_init, freq_end, num_points):
        matrix_sweep = []
        # Retrieve these values from the target 
        
        return matrix_sweep       

    @property
    def free_amplitude(self):
        """The 'free_amplitude' property getter"""
        return self.__free_amplitude
    
    @free_amplitude.setter
    def free_amplitude(self, value):
        """The 'free_amplitude' property setter"""
        if 0 <= value:
            self.__free_amplitude = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Free amplitude must be equal to or greater than 0.")     

    def __repr__(self):
        return (
            f"AMMode("
            f"exc_type={self.__exc_type}, "
            f"exc_amplitude={self.__exc_amplitude}, "
            f"free_amplitude={self.__free_amplitudey}, "
            f"exc_frequency={self.__exc_frequency}, "
            f"exc_phase={self.__exc_phase}, "
            f"lockin_bandwidth={self.__lockin_bandwidth}, "
            f"lockin_order={self.__lockin_order}, "
            f"free_amplitude={self.__free_amplitude})"
        )


class FMMode(AFMMode):
    """
    A class to control the Frequency Modulation (FM) Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the FM Mode, 
    including the ability to manage excitation settings, lock-in amplifier parameters, and PLL gains.

    Attributes:
        __exc_type (ExcType): Type of excitation used, either 'piezo' or 'photothermal'.
        __exc_amplitude (float): Amplitude of the excitation signal in volts.
        __exc_offset (float): Offset of the excitation signal in volts.
        __exc_init_frequency (float): Initial frequency of the excitation signal in Hertz.
        __exc_phase (float): Phase of the excitation signal in degrees, ranging from -180 to 180.
        __lockin_bandwidth (float): Bandwidth of the lock-in amplifier in Hertz.
        __lockin_order (int): Order of the lock-in amplifier, restricted to values 1, 2, 3, or 4.
        __pll_p_gain (float): Proportional gain of the Phase-Locked Loop (PLL).
        __pll_i_gain (float): Integral gain of the PLL.
        __pll_d_gain (float): Derivative gain of the PLL.
        __pll_lock_pll (bool): Indicates whether the PLL is locked.

    Methods:
        init_mode_with_params: Initializes the instance with specific values for all attributes and returns the instance.
        get_mode_parameters: Fetches the current FM Mode parameters from the system.
        set_mode_parameters: Sets the FM Mode parameters on the target system.
        do_sweep: Performs a frequency sweep based on the given parameters.
    """

    def __init__(self):
        super().__init__(AFMModes.FM)
        self.get_mode_parameters()
    
    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()       
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll)
        return instance  
    
    def get_mode_parameters(self):
        """Get the actual mode parameters"""
        # self.__exc_type = ExcType.PZ # Read that from target system [piezo, photothermal]
        # self.__exc_amplitude = 0  # Read that from target system [V]
        # self.__exc_offset = 0  # Read that from target system [V]
        # self.__exc_init_frequency = 0  # Read that from target system [Hz]
        # self.__exc_phase = 0  # Read that from target system [deg]
        # self.__lockin_bandwidth = 0  # Read that from target system [Hz]
        # self.__lockin_order = 1 # Read that from target system 
        # self.__pll_p_gain = 1 # Read that from target system 
        # self.__pll_i_gain = 1 # Read that from target system 
        # self.__pll_d_gain = 1 # Read that from target system 
        # self.__pll_lock_pll = True # Read that from target system 

        # Retrieve these values from the target 
        
        pass
    
    def set_mode_parameters(self, exc_type, exc_amplitude, exc_offset, exc_init_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll):
        """Set the contact mode parameters on the target system"""
        self.__exc_type = exc_type # [piezo, photothermal]
        self.__exc_amplitude = exc_amplitude
        self.__exc_offset = exc_offset
        self.__exc_init_frequency = exc_init_frequency
        self.__exc_phase = exc_phase
        self.__lockin_bandwidth = lockin_bandwidth
        self.__lockin_order = lockin_order
        self.__pll_p_gain = p_gain
        self.__pll_i_gain = i_gain
        self.__pll_d_gain = d_gain
        self.__pll_lock_pll = lock_pll
        
        # Update these values on the target system if necessary   

    @property
    def exc_type(self):
        """The 'exc_type' property getter"""
        return self.__exc_type
    
    @exc_type.setter
    def exc_type(self, value):
        """The 'exc_type' property setter"""
        if not isinstance(value, ExcType):
            raise ValueError("exc_type must be an instance of ExcType.")
        self.__exc_type = value
        # Set the mode parameter on the target system
        
    @property
    def exc_amplitude(self):
        """The 'exc_amplitude' property getter"""
        return self.__exc_amplitude
    
    @exc_amplitude.setter
    def exc_amplitude(self, value):
        """The 'exc_amplitude' property setter"""
        if 0 <= value:
            self.__exc_amplitude = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation amplitude must be equal to or greater than 0.")     
   
    @property
    def exc_offset(self):
        """The 'exc_offset' property getter"""
        return self.__exc_offset
    
    @exc_offset.setter
    def exc_offset(self, value):
        """The 'exc_offset' property setter"""
        self.__exc_offset = value
        # Set the mode parameter on the target system  
        
    @property
    def exc_init_frequency(self):
        """The 'exc_init_frequency' property getter"""
        return self.__exc_init_frequency
    
    @exc_init_frequency.setter
    def exc_init_frequency(self, value):
        """The 'exc_init_frequency' property setter"""
        if 0 < value:
            self.__exc_init_frequency = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation initial frequency must be greater than 0.")   
            
    @property
    def exc_phase(self):
        """The 'exc_phase' property getter"""
        return self.__exc_phase
    
    @exc_phase.setter
    def exc_phase(self, value):
        """The 'exc_phase' property setter"""
        if -180 <= value <= 180:
            self.__exc_phase= value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation phase must be between -180 and 180 degrees.")     
    
    @property
    def lockin_bandwidth(self):
        """The 'lockin_bandwidth' property getter"""
        return self.__lockin_bandwidth
    
    @lockin_bandwidth.setter
    def lockin_bandwidth(self, value):
        """The 'lockin_bandwidth' property setter"""
        if 0 <= value:
            self.__lockin_bandwidth = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("Lock-in bandwidth must be equal to or greater than 0.")    
            
    @property
    def lockin_order(self):
        """The 'lockin_order' property getter"""
        return self.__lockin_order
    
    @lockin_order.setter
    def lockin_order(self, value):
        """The 'lockin_order' property setter"""
        if value in [1, 2, 3, 4]:
            self.__lockin_order = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("Lockin order must be 1, 2, 3, or 4.") 
            
    @property
    def pll_p_gain(self):
        """The 'pll_p_gain' property getter"""
        return self.__pll_p_gain
    
    @pll_p_gain.setter
    def pll_p_gain(self, value):
        """The 'pll_p_gain' property setter"""
        if 0 <= value:
            self.__pll_p_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("P must be equal to or greater than 0.")        
            
    @property
    def pll_i_gain(self):
        """The 'pll_i_gain' property getter"""
        return self.__pll_i_gain
    
    @pll_i_gain.setter
    def pll_i_gain(self, value):
        """The 'pll_i_gain' property setter"""
        if 0 <= value:
            self.__pll_i_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("I must be equal to or greater than 0.")  

    @property
    def pll_d_gain(self):
        """The 'pll_d_gain' property getter"""
        return self.__pll_d_gain
    
    @pll_d_gain.setter
    def pll_d_gain(self, value):
        """The 'pll_d_gain' property setter"""
        if 0 <= value:
            self.__pll_d_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("D must be equal to or greater than 0.")  

    def do_sweep(self, freq_init, freq_end, num_points):
        matrix_sweep = []
        # Retrieve these values from the target 
        
        return matrix_sweep

    def __repr__(self):
        return (
            f"FMMode("
            f"exc_type={self.__exc_type}, "
            f"exc_amplitude={self.__exc_amplitude}, "
            f"exc_offset={self.e__xc_offset}, "
            f"exc_init_frequency={self.__exc_init_frequency}, "
            f"exc_phase={self.__exc_phase}, "
            f"lockin_bandwidth={self.__lockin_bandwidth}, "
            f"lockin_order={self.__lockin_order}, "
            f"pll_p_gain={self.__pll_p_gain}, "
            f"pll_i_gain={self.__pll_i_gain}, "
            f"pll_d_gain={self.__pll_d_gain}, "
            f"pll_lock_pll={self.__pll_lock_pll})"
        )


class ContactMode(AFMMode):
    """
    A class to control the Contact Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the Contact Mode, 
    including the ability to manage the relative setpoint and update the deflection value.

    Attributes:
        __relative_setpoint (bool): Indicates whether the setpoint is relative to the current deflection value.

    Methods:
        init_mode_with_params: Initialize the instance with specific values for all attributes and return the instance.
        get_mode_parameters: Fetches the current Contact Mode parameters from the system.
        set_mode_parameters: Sets the Contact Mode parameters on the target system.
        update_deflection_value: Updates the deflection value to be used for relative setpoint calculation.
        relative_setpoint: Gets or sets the relative setpoint mode.
    """
    
    def __init__(self):
        super().__init__(AFMModes.CONTACT)
        self.get_mode_parameters()
    
    @classmethod
    def init_mode_with_params(cls, relative_setpoint):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()       
        instance.set_mode_parameters(relative_setpoint)
        return instance  
    
    def get_mode_parameters(self):
        """Get the actual mode parameters"""
        # self.__relative_setpoint = False # Read that from target system

        # Retrieve these values from the target 
        
        pass
    
    def set_mode_parameters(self, relative_setpoint):
        """Set the contact mode parameters on the target system"""
        self.__relative_setpoint = relative_setpoint 
        
        # Update these values on the target system if necessary   
     
    def update_deflection_value(self):
        """Update the deflection value to be used on the relative setpoint calculation"""
        # Update the deflection value on the target system
        pass           
     
    @property
    def relative_setpoint(self):
        """The 'relative_setpoint' property getter"""
        return self.__relative_setpoint
    
    @relative_setpoint.setter
    def relative_setpoint(self, value):
        """The 'relative_setpoint' property setter"""
        self.__relative_setpoint = value
        # Set relative setpoint mode on the target system

    def __repr__(self):
        return f"ContactMode(relative_setpoint={self.__relative_setpoint})"


class OffResonanceMode(AFMMode):
    """
    A class to control the Off Resonance Tapping (ORT) mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the Off Resonance Tapping mode, 
    ensuring proper validation and encapsulation of the excitation type, amplitude, frequency, phase, and offset 
    used in this mode.

    Attributes:
        __exc_type (ExcType): Type of excitation used, either 'piezo' or 'photothermal'.
        __exc_amplitude (float): Amplitude of the excitation signal in volts.
        __exc_frequency (float): Frequency of the excitation signal in Hertz.
        __exc_phase (float): Phase of the excitation signal in degrees, ranging from -180 to 180.
        __exc_offset (float): Offset of the excitation signal in volts.
    
    Methods:
        init_mode_with_params: Initializes the instance with specific values for all attributes.
        get_mode_parameters: Fetches the current Off Resonance Tapping mode parameters from the system.
        set_mode_parameters: Sets the Off Resonance Tapping mode parameters on the target system.

    """    

    def __init__(self):
        super().__init__(AFMModes.ORT)
        self.get_mode_parameters()
        
    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()       
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset)
        return instance  
    
    def get_mode_parameters(self):
        """Get the actual mode parameters"""
        # self.__exc_type =  ExcType.PZ # Read that from target system [piezo, photothermal]
        # self.__exc_amplitude = 0  # Read that from target system [V]
        # self.__exc_frequency = 0  # Read that from target system [Hz]
        # self.__exc_phase = 0  # Read that from target system [deg]
        # self.__exc_offset = 0  # Read that from target system [V]
        
        # Retrieve these values from the target 
        
        pass
    
    def set_mode_parameters(self, exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset):
        """Set the Off Resonance Tapping mode parameters on the target system"""
        self.__exc_type = exc_type 
        self.__exc_amplitude = exc_amplitude
        self.__exc_frequency = exc_frequency
        self.__exc_phase = exc_phase
        self.__exc_offset = exc_offset
        # Update these values on the target system if necessary    
        
    @property
    def exc_type(self):
        """The 'exc_type' property getter"""
        return self.__exc_type
    
    @exc_type.setter
    def exc_type(self, value):
        """The 'exc_type' property setter"""
        if not isinstance(value, ExcType):
            raise ValueError("exc_type must be an instance of ExcType.")
        self.__exc_type = value
        # Set the mode parameter on the target system
        
    @property
    def exc_amplitude(self):
        """The 'exc_amplitude' property getter"""
        return self.__exc_amplitude
    
    @exc_amplitude.setter
    def exc_amplitude(self, value):
        """The 'exc_amplitude' property setter"""
        if 0 <= value:
            self.__exc_amplitude = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation amplitude must be equal to or greater than 0.")     

    @property
    def exc_frequency(self):
        """The 'exc_frequency' property getter"""
        return self.__exc_frequency
    
    @exc_frequency.setter
    def exc_frequency(self, value):
        """The 'exc_frequency' property setter"""
        if 0 < value:
            self.__exc_frequency = value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation frequency must be greater than 0.")   
            
    @property
    def exc_phase(self):
        """The 'exc_phase' property getter"""
        return self.__exc_phase
    
    @exc_phase.setter
    def exc_phase(self, value):
        """The 'exc_phase' property setter"""
        if -180 <= value <= 180:
            self.__exc_phase= value
            # Set the mode parameter on the target system   
        else:
            raise ValueError("Excitation phase must be between -180 and 180 degrees.")     

    @property
    def exc_offset(self):
        """The 'exc_offset' property getter"""
        return self.__exc_offset
    
    @exc_offset.setter
    def exc_offset(self, value):
        """The 'exc_offset' property setter"""
        self.__exc_offset = value
        # Set the mode parameter on the target system   

    def __repr__(self):
        return (
            f"OffResonanceMode("
            f"exc_type={self.__exc_type}, "
            f"exc_amplitude={self.__exc_amplitude}, "
            f"exc_frequency={self.__exc_frequency}, "
            f"exc_phase={self.__exc_phase}, "
            f"exc_offset={self.__exc_offset})"
        )


class ZControlPID:  
    """
    A class to control the PID parameters for a Z-axis control system.
    
    This class provides methods to initialize, get, and set PID control parameters, 
    ensuring proper validation and encapsulation of the PID gains, setpoint, and feedback 
    units used in the control process.
    
    Attributes:
        __p_gain (float): Proportional gain of the PID controller.
        __i_gain (float): Integral gain of the PID controller.
        __d_gain (float): Derivative gain of the PID controller.
        __setpoint (float): Desired setpoint for the PID controller.
        __units (str): Units of the feedback signal, e.g., Contact Mode [V, m, N], AM [V, m, %], FM [V, Hz], Off resonance [V, m, N]
        __feedback (bool): Indicates whether the feedback loop is active.
        __afm_mode (AFMMode): Indicates the used AFM mode on the systems
    
    Methods:
        init_zcontrolpid_with_params: Initializes the instance with specific values for all attributes.
        get_zcontrolpid_parameters: Fetches the actual Z control PID parameters from the system.
        set_zcontrolpid_parameters: Sets PID parameters on the target system.
        get_zposition: Retrieve the actual z scanner position.
        set_zposition: Move the tip to the desired z position.
    """
    
    def __init__(self):
        self.get_zcontrolpid_parameters()
        
    @classmethod
    def init_zcontrolpid_with_params(cls, p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode):
        """Initialize the instance with specific values for all attributes"""
        instance = cls()       
        instance.set_zcontrolpid_parameters(p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode)
        return instance  
        
    def get_zcontrolpid_parameters(self):
        """Get the actual Z control PID status of the system"""
        # self.__p_gain = 0  # Read that from target system
        # self.__i_gain = 0  # Read that from target system
        # self.__d_gain = 0  # Read that from target system
        # self.__setpoint = 0  # Read that from target system
        # self.__units = 'V'  # Read that from target system
        # self.__feedback = False # Read that from target system
        # self.__afm_mode = None # Read that from target system
        
        # Retrieve these values from the target 
        
        pass
    
    def set_zcontrolpid_parameters(self, p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode):
        """Set Z control PID parameters on the target system"""
        self.__p_gain = p_gain
        self.__i_gain = i_gain
        self.__d_gain = d_gain
        self.__setpoint = setpoint
        self.__units = units
        self.__feedback = feedback
        self.__afm_mode = afm_mode
        # Update these values on the target system if necessary            
        
    @property
    def p_gain(self):
        """The 'p_gain' property getter"""
        return self.__p_gain
    
    @p_gain.setter
    def p_gain(self, value):
        """The 'p_gain' property setter"""
        if 0 <= value:
            self.__p_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("P must be equal to or greater than 0.")        
            
    @property
    def i_gain(self):
        """The 'i_gain' property getter"""
        return self.__i_gain
    
    @i_gain.setter
    def i_gain(self, value):
        """The 'i_gain' property setter"""
        if 0 <= value:
            self.__i_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("I must be equal to or greater than 0.")  

    @property
    def d_gain(self):
        """The 'd_gain' property getter"""
        return self.__d_gain
    
    @d_gain.setter
    def d_gain(self, value):
        """The 'd_gain' property setter"""
        if 0 <= value:
            self.__d_gain = value
            # Set PID control parameter on the target system   
        else:
            raise ValueError("D must be equal to or greater than 0.")                  
                
    @property
    def setpoint(self):
        """The 'setpoint' property getter"""
        return self.__setpoint
    
    @setpoint.setter
    def setpoint(self, value):
        """The 'setpoint' property setter"""
        self.__setpoint = value
        # Set PID control parameter on the target system   

    @property
    def units(self):
        """The 'units' property getter"""
        return self.__units
    
    @units.setter
    def units(self, value):
        """The 'units' property setter"""
        
        if isinstance(self.__afm_mode, AMMode):
            if value == 'V'  or 'm' or '%':
                self.__units = value
            else:
                raise ValueError("Selected unit cannot be used in this mode.") 
        elif isinstance(self.__afm_mode, FMMode):
            if value == 'V'  or 'Hz':
                self.__units = value
            else:
                raise ValueError("Selected unit cannot be used in this mode.") 
        elif isinstance(self.__afm_mode, ContactMode) or isinstance(self.__afm_mode, OffResonanceMode):
            if value == 'V'  or 'm' or 'N':
                self.__units = value
            else:
                raise ValueError("Selected unit cannot be used in this mode.") 
        else:
            raise ValueError("Selected mode is not on the list.")     

        # Set PID control parameter on the target system   

    @property
    def feedback(self):
        """The 'feedback' property getter"""
        return self.__feedback
    
    @feedback.setter
    def feedback(self, value):
        """The 'feedback' property setter"""
        self.__feedback = value
        # Set PID control parameter on the target system                  
                
    @property
    def afm_mode(self):
        """The 'afm_mode' property getter"""
        return self.__afm_mode
    
    @afm_mode.setter
    def afm_mode(self, value):
        """The 'afm_mode' property setter"""
        self.__afm_mode = value
        # Set PID control parameter on the target system                  
    
    def get_zposition(self):
        """Retrieve the actual Z scanner position"""
        # Implement scan control parameters on the target system
        pass
    
    def set_zposition(self, x, y, forced=False):
        """Move the tip to the desired Z position"""
        if self.__feedback:  # If feedback is on
            if forced:  # If feedback is on, force stop and move to the desired Z position
                self.feedback = False  # This calls the feedback setter
                # Implement additional logic to move to the Z position
                pass
        else:
            # Implement logic to move to the Z position when feedback is off
            pass
      
    def __repr__(self):
        return (
            f"ZControlPID("
            f"p_gain={self.__p_gain}, "
            f"i_gain={self.__i_gain}, "
            f"d_gain={self.__d_gain}, "
            f"setpoint={self.__setpoint}, "
            f"units={self.__units}, "
            f"feedback={self.__feedback})"
            f"afm_mode={self.__afm_mode})"
        )


class AcquiredImage:
    """
    A class to handle image acquisition and manage image channels.

    This class provides methods to retrieve the names, units, and data for various image channels. 
    It allows users to access specific channels by name and retrieve all channel data.

    Methods:
        get_channels_names_units: Retrieves the names and units of all channels in the image.
        get_all_channels_data: Retrieves the data for all image channels.
        get_channel: Retrieves the data of a specific image channel by name.
    """
    
    def __init__(self):
        pass
    
    def get_channels_names_units(self):
        """Retrieve the names and units of all image channels."""
        pass
    
    def get_all_channels_data(self):
        """Retrieve the data from all image channels."""
        pass
    
    def get_channel(self, name):
        """Retrieve the data from the image channel with the given name."""
        pass
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__}()"
        )
   

class Motors:
    """
    A class to control the motors of the stage, lasers, and photodiode in a scanning arm system.
    
    This class provides methods to move and control different components of the system, 
    including the stage, readout laser, excitation laser, and photodiode, in the X, Y, and Z directions.
    The movement can be defined by steps, time, or distance.
    
    Methods:
        moveX_stage_steps: Move the stage by a specified number of steps in the X direction.
        moveX_stage_time: Move the stage for a specified duration in the X direction.
        moveX_stage_distance: Move the stage by a specific distance in the X direction.
        moveY_stage_steps: Move the stage by a specified number of steps in the Y direction.
        moveY_stage_time: Move the stage for a specified duration in the Y direction.
        moveY_stage_distance: Move the stage by a specific distance in the Y direction.
        moveZ_stage_steps: Move the stage by a specified number of steps in the Z direction.
        moveZ_stage_time: Move the stage for a specified duration in the Z direction.
        moveZ_stage_distance: Move the stage by a specific distance in the Z direction.
        center_stage: Move the stage to its center position.
        
        moveX_readout_laser_steps: Move the readout laser by a specified number of steps in the X direction.
        moveX_readout_laser_time: Move the readout laser for a specified duration in the X direction.
        moveX_readout_laser_distance: Move the readout laser by a specific distance in the X direction.
        moveY_readout_laser_steps: Move the readout laser by a specified number of steps in the Y direction.
        moveY_readout_laser_time: Move the readout laser for a specified duration in the Y direction.
        moveY_readout_laser_distance: Move the readout laser by a specific distance in the Y direction.
        moveZ_readout_laser_steps: Move the readout laser by a specified number of steps in the Z direction.
        moveZ_readout_laser_time: Move the readout laser for a specified duration in the Z direction.
        moveZ_readout_laser_distance: Move the readout laser by a specific distance in the Z direction.
        center_readout_laser: Center the readout laser.
        maximize_readout_laser: Maximize the signal from the readout laser.
        
        moveX_excitation_laser_steps: Move the excitation laser by a specified number of steps in the X direction.
        moveX_excitation_laser_time: Move the excitation laser for a specified duration in the X direction.
        moveX_excitation_laser_distance: Move the excitation laser by a specific distance in the X direction.
        moveY_excitation_laser_steps: Move the excitation laser by a specified number of steps in the Y direction.
        moveY_excitation_laser_time: Move the excitation laser for a specified duration in the Y direction.
        moveY_excitation_laser_distance: Move the excitation laser by a specific distance in the Y direction.
        moveZ_excitation_laser_steps: Move the excitation laser by a specified number of steps in the Z direction.
        moveZ_excitation_laser_time: Move the excitation laser for a specified duration in the Z direction.
        moveZ_excitation_laser_distance: Move the excitation laser by a specific distance in the Z direction.
        center_excitation_laser: Center the excitation laser.
        maximize_excitation_laser: Maximize the signal from the excitation laser.
        
        moveX_photodiode_steps: Move the photodiode by a specified number of steps in the X direction.
        moveX_photodiode_time: Move the photodiode for a specified duration in the X direction.
        moveX_photodiode_distance: Move the photodiode by a specific distance in the X direction.
        moveY_photodiode_steps: Move the photodiode by a specified number of steps in the Y direction.
        moveY_photodiode_time: Move the photodiode for a specified duration in the Y direction.
        moveY_photodiode_distance: Move the photodiode by a specific distance in the Y direction.
        center_photodiode: Center the photodiode.
        autoalign_photodiode: Automatically align the photodiode for optimal signal.
    """
    
    def __init__(self):
        pass

    def moveX_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the X direction."""
        pass

    def moveX_stage_time(self, duration):
        """Move the stage for a specified duration in the X direction."""
        pass

    def moveX_stage_distance(self, distance):
        """Move the stage by a specific distance in the X direction."""
        pass

    def moveY_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the Y direction."""
        pass

    def moveY_stage_time(self, duration):
        """Move the stage for a specified duration in the Y direction."""
        pass

    def moveY_stage_distance(self, distance):
        """Move the stage by a specific distance in the Y direction."""
        pass

    def moveZ_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the Z direction."""
        pass

    def moveZ_stage_time(self, duration):
        """Move the stage for a specified duration in the Z direction."""
        pass

    def moveZ_stage_distance(self, distance):
        """Move the stage by a specific distance in the Z direction."""
        pass

    def center_stage(self):
        """Move the stage to its center position."""
        pass

    def moveX_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the X direction."""
        pass

    def moveX_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the X direction."""
        pass

    def moveX_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the X direction."""
        pass

    def moveY_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the Y direction."""
        pass

    def moveY_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the Y direction."""
        pass

    def moveY_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the Y direction."""
        pass

    def moveZ_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the Z direction."""
        pass

    def moveZ_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the Z direction."""
        pass

    def moveZ_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the Z direction."""
        pass

    def center_readout_laser(self):
        """Center the readout laser."""
        pass

    def maximize_readout_laser(self):
        """Maximize the signal from the readout laser."""
        pass

    def moveX_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the X direction."""
        pass

    def moveX_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the X direction."""
        pass

    def moveX_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the X direction."""
        pass

    def moveY_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the Y direction."""
        pass

    def moveY_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the Y direction."""
        pass

    def moveY_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the Y direction."""
        pass

    def moveZ_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the Z direction."""
        pass

    def moveZ_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the Z direction."""
        pass

    def moveZ_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the Z direction."""
        pass

    def center_excitation_laser(self):
        """Center the excitation laser."""
        pass

    def maximize_excitation_laser(self):
        """Maximize the signal from the excitation laser."""
        pass

    def moveX_photodiode_steps(self, Nsteps):
        """Move the photodiode by a specified number of steps in the X direction."""
        pass

    def moveX_photodiode_time(self, duration):
        """Move the photodiode for a specified duration in the X direction."""
        pass

    def moveX_photodiode_distance(self, distance):
        """Move the photodiode by a specific distance in the X direction."""
        pass

    def moveY_photodiode_steps(self, Nsteps):
        """Move the photodiode by a specified number of steps in the Y direction."""
        pass

    def moveY_photodiode_time(self, duration):
        """Move the photodiode for a specified duration in the Y direction."""
        pass

    def moveY_photodiode_distance(self, distance):
        """Move the photodiode by a specific distance in the Y direction."""
        pass

    def center_photodiode(self):
        """Center the photodiode."""
        pass

    def autoalign_photodiode(self):
        """Automatically align the photodiode for optimal signal."""
        pass


class Lasers:
    """
    A class to control and manage the lasers in a scanning system.

    This class provides methods to initialize, set, and retrieve parameters for the lasers,
    including the readout power, excitation power, and excitation offset. It also controls
    the laser states (on/off) and allows dynamic adjustment of these values.

    Attributes:
        readout_mW: Power of the readout laser in milliwatts.
        excitation_mW: Power of the excitation laser in milliwatts.
        excitation_offset: Offset value for the excitation laser.
        readout_ON: Boolean indicating whether the readout laser is on.
        excitation_ON: Boolean indicating whether the excitation laser is on.

    Methods:
        init_laser_with_params: Initializes an instance with specific laser parameters.
        get_laser_parameters: Retrieves the current laser parameters from the system.
        set_laser_parameters: Sets laser parameters such as power and state.
    """
    
    def __init__(self):
        self.get_laser_parameters()
        
    @classmethod
    def init_laser_with_params(cls, readout_power, excitation_power, excitation_offset, readout_ON, excitation_ON):
        """Initialize the instance with specific values for laser power, offset, and states."""
        instance = cls()       
        instance.set_laser_parameters(readout_power, excitation_power, excitation_offset, readout_ON, excitation_ON)
        return instance  
        
    def get_laser_parameters(self):
        """Retrieve the current laser power, offset, and state values from the system."""
        # The following should be replaced with actual calls to retrieve values from the system:
        # self.__readout_mW = 0  # Example value from the system in mW
        # self.__excitation_mW = 0  # Example value from the system in mW
        # self.__excitation_offset = 0  # Example value from the system
        # self.__readout_ON = False  # Example value from the system
        # self.__excitation_ON = False  # Example value from the system
        
        # Actual system retrieval code goes here
        pass
    
    def set_laser_parameters(self, readout_mW, excitation_mW, excitation_offset, readout_ON, excitation_ON):
        """Set the laser parameters such as power, offset, and state on the system."""
        self.__readout_mW = readout_mW
        self.__excitation_mW = excitation_mW
        self.__excitation_offset = excitation_offset
        self.__readout_ON = readout_ON
        self.__excitation_ON = excitation_ON

        # Code to update the system with these values goes here
    
    @property
    def readout_mW(self):
        """Get the current readout laser power in milliwatts."""
        return self.__readout_mW 
    
    @readout_mW.setter
    def readout_mW(self, value):
        """Set the readout laser power, ensuring the value is non-negative."""
        if 0 <= value:
            self.__readout_mW  = value
            # Code to update the laser control on the system goes here
        else:
            raise ValueError("Readout power must be equal to or greater than 0.")   
            
    @property
    def excitation_mW(self):
        """Get the current excitation laser power in milliwatts."""
        return self.__excitation_mW 
    
    @excitation_mW.setter
    def excitation_mW(self, value):
        """Set the excitation laser power, ensuring the value is non-negative."""
        if 0 <= value:
            self.__excitation_mW  = value
            # Code to update the laser control on the system goes here
        else:
            raise ValueError("Excitation power must be equal to or greater than 0.")   
            
    @property
    def excitation_offset(self):
        """Get the current excitation laser offset."""
        return self.__excitation_offset
    
    @excitation_offset.setter
    def excitation_offset(self, value):
        """Set the excitation laser offset, ensuring the value is non-negative."""
        if 0 <= value:
            self.__excitation_offset  = value
            # Code to update the laser control on the system goes here
        else:
            raise ValueError("Excitation offset must be equal to or greater than 0.")   
            
    @property
    def readout_ON(self):
        """Get the current state of the readout laser (on or off)."""
        return self.__readout_ON
    
    @readout_ON.setter
    def readout_ON(self, value):
        """Set the readout laser state (on or off)."""
        self.__readout_ON  = value
        # Code to update the laser control on the system goes here

    @property
    def excitation_ON(self):
        """Get the current state of the excitation laser (on or off)."""
        return self.__excitation_ON
    
    @excitation_ON.setter
    def excitation_ON(self, value):
        """Set the excitation laser state (on or off)."""
        self.__excitation_ON  = value
        # Code to update the laser control on the system goes here
        
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"readout_mW={self.__readout_mW}, "
            f"excitation_mW={self.__excitation_mW}, "
            f"excitation_offset={self.__excitation_offset}, "
            f"readout_ON={self.__readout_ON}, "
            f"excitation_ON={self.__excitation_ON})"
        )


class AFMController:
    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.scan_parameters = None
        self.z_control_pid = None
        self.acquired_images = []
        self.afm_mode = None

    def connect(self):
        # Implement connection logic here
        pass

    def disconnect(self):
        # Implement disconnection logic here
        pass

    def set_scan_parameters(self, scan_size, scan_speed, resolution):
        self.scan_parameters = ScanParameters(scan_size, scan_speed, resolution)

    def set_z_control_pid(self, p_gain, i_gain, d_gain):
        self.z_control_pid = ZControlPID(p_gain, i_gain, d_gain)

    def set_afm_mode(self, mode):
        self.afm_mode = mode

    def start_scan(self):
        # Implement scan logic here
        # On completion, create an AcquiredImage and add to acquired_images
        pass

    def get_latest_image(self):
        if self.acquired_images:
            return self.acquired_images[-1]
        return None

    def __repr__(self):
        return (f"AFMController(connection_params={self.connection_params}, scan_parameters={self.scan_parameters}, "
                f"z_control_pid={self.z_control_pid}, afm_mode={self.afm_mode}, acquired_images={len(self.acquired_images)})")
