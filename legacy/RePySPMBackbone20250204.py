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
        pass

    def get_exc_amplitude(self):
        """Retrieves the excitation amplitude signal from the system."""
        pass

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

    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, free_amplitude)
        return instance

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


class FMMode(AFMMode):
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

    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_offset, exc_frequency, exc_phase, lockin_bandwidth, lockin_order, p_gain, i_gain, d_gain, lock_pll)
        return instance

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


class ContactMode(AFMMode):
    """
    A class to control the Contact Mode for an Atomic Force Microscope (AFM) system.

    This class provides methods to initialize, get, and set parameters specific to the Contact Mode, 
    including the ability to manage the relative setpoint and update the deflection value.

    Methods:
        get_mode_parameters: Fetches the current Contact Mode parameters from the system.
        set_mode_parameters: Sets the Contact Mode parameters on the target system.
        update_deflection_value: Updates the deflection value to be used for relative setpoint calculation.
        get_relative_setpoint: Retrieves the relative setpoint mode.
        set_relative_setpoint: Sets the relative setpoint mode.
    """

    def __init__(self):
        pass

    @classmethod
    def init_mode_with_params(cls, relative_setpoint):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()
        instance.set_mode_parameters(relative_setpoint)
        return instance

    def get_mode_parameters(self):
        """Fetches the current Contact Mode parameters from the system."""
        pass

    def set_mode_parameters(self, relative_setpoint):
        """Sets the Contact Mode parameters on the target system.

        Args:
            relative_setpoint (bool): True if the setpoint is relative to the current deflection value, False otherwise.
        """
        pass

    def update_deflection_value(self):
        """Updates the deflection value to be used for relative setpoint calculation."""
        pass

    def get_relative_setpoint(self):
        """Retrieves the relative setpoint mode."""
        pass

    def set_relative_setpoint(self, value):
        """Sets the relative setpoint mode.

        Args:
            value (bool): True to enable relative setpoint, False to disable.
        """
        pass

    def __repr__(self):
        """Represents the ContactMode object as a string."""
        return "ContactMode()"


class OffResonanceMode(AFMMode):
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
        subtract_background: Subtracts the background from the vertical deflection signal of the cantilevers.
    """

    def __init__(self):
        pass

    @classmethod
    def init_mode_with_params(cls, exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset):
        """Initialize the instance with specific values for all attributes and return the instance."""
        instance = cls()
        instance.set_mode_parameters(exc_type, exc_amplitude, exc_frequency, exc_phase, exc_offset)
        return instance

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

    def __init__(self):
        pass

    @classmethod
    def init_zcontrolpid_with_params(cls, p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode):
        """Initialize the instance with specific values for all attributes."""
        instance = cls()
        instance.set_zcontrolpid_parameters(p_gain, i_gain, d_gain, setpoint, units, feedback, afm_mode)
        return instance

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


class AcquiredImage:
    """
    A class to handle image acquisition and manage image channels.

    This class provides methods to retrieve the names, units, and data for various image channels. 
    It allows users to access specific channels by name and retrieve all channel data.

    Methods:
        get_channels_units: Retrieves the units of all channels in the image.
        get_channels_names: Retrieves the names of all channels in the image.
        get_all_channels_data: Retrieves the data for all image channels.
        get_channel: Retrieves the data of a specific image channel by name.
    """
    
    def __init__(self):
        pass
    
    def get_channels_units(self):
        """Retrieve the units of all image channels."""
        pass
    
    def get_channels_names(self):
        """Retrieve the names of all image channels."""
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

    Methods:
        get_laser_parameters: Retrieves the current laser parameters from the system.
        set_laser_parameters: Sets laser parameters such as power and state.
        get_readout_mW: Retrieves the power of the readout laser in milliwatts.
        set_readout_mW: Sets the power of the readout laser in milliwatts.
        get_excitation_mW: Retrieves the power of the excitation laser in milliwatts.
        set_excitation_mW: Sets the power of the excitation laser in milliwatts.
        get_excitation_offset: Retrieves the offset of the excitation laser.
        set_excitation_offset: Sets the offset of the excitation laser.
        get_readout_ON: Retrieves the state of the readout laser (on/off).
        set_readout_ON: Sets the state of the readout laser (on/off).
        get_excitation_ON: Retrieves the state of the excitation laser (on/off).
        set_excitation_ON: Sets the state of the excitation laser (on/off).
    """

    def __init__(self):
        pass

    @classmethod
    def init_laser_with_params(cls, readout_mW, excitation_mW, excitation_offset, readout_ON, excitation_ON):
        """Initialize the instance with specific values for laser power, offset, and states."""
        instance = cls()
        instance.set_laser_parameters(readout_mW, excitation_mW, excitation_offset, readout_ON, excitation_ON)
        return instance

    def get_laser_parameters(self):
        """Retrieves the current laser parameters from the system."""
        pass

    def set_laser_parameters(self, readout_mW, excitation_mW, excitation_offset, readout_ON, excitation_ON):
        """Sets laser parameters such as power, offset, and state on the system.

        Args:
            readout_mW (float): Power of the readout laser in milliwatts.
            excitation_mW (float): Power of the excitation laser in milliwatts.
            excitation_offset (float): Offset value for the excitation laser.
            readout_ON (bool): State of the readout laser (True for ON, False for OFF).
            excitation_ON (bool): State of the excitation laser (True for ON, False for OFF).
        """
        pass

    def get_readout_mW(self):
        """Retrieves the power of the readout laser in milliwatts."""
        pass

    def set_readout_mW(self, readout_mW):
        """Sets the power of the readout laser in milliwatts.

        Args:
            readout_mW (float): Power in milliwatts.
        """
        pass

    def get_excitation_mW(self):
        """Retrieves the power of the excitation laser in milliwatts."""
        pass

    def set_excitation_mW(self, excitation_mW):
        """Sets the power of the excitation laser in milliwatts.

        Args:
            excitation_mW (float): Power in milliwatts.
        """
        pass

    def get_excitation_offset(self):
        """Retrieves the offset of the excitation laser."""
        pass

    def set_excitation_offset(self, excitation_offset):
        """Sets the offset of the excitation laser.

        Args:
            excitation_offset (float): Offset value.
        """
        pass

    def get_readout_ON(self):
        """Retrieves the state of the readout laser (on/off)."""
        pass

    def set_readout_ON(self, readout_ON):
        """Sets the state of the readout laser (on/off).

        Args:
            readout_ON (bool): True for ON, False for OFF.
        """
        pass

    def get_excitation_ON(self):
        """Retrieves the state of the excitation laser (on/off)."""
        pass

    def set_excitation_ON(self, excitation_ON):
        """Sets the state of the excitation laser (on/off).

        Args:
            excitation_ON (bool): True for ON, False for OFF.
        """
        pass

    def __repr__(self):
        """Represents the Lasers object as a string."""
        return "Lasers()"


class AFMController:
    def __init__(self, connection_params):
        
        self.Signals = Signals()
        self.Signals = ScanParameters()
        self.ScanControl = ScanControl()
        self.ZControlPID = ZControlPID(self)
        self.motors = Motors()
        self.Lasers = Lasers()
        self.AcquiredImage = AcquiredImage()
        self.ContactMode = ContactMode()

    def connect(self):
        # Implement connection logic here
        pass

    def disconnect(self):
        # Implement disconnection logic here
        pass
