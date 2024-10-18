import os
import re
import math
from enum import Enum


# To do list: get image (number of channels to get),

# Do the other modes and then update the mode control capabilities in ZControlPID class

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
    
    This class provides methods to set and get the signals, representing various measurements 
    such as deflection and amplitude from the system. It allows initialization with specific 
    signal values and updating the current signals dynamically.
    
    Attributes:
        __vertical_deflection (float): The vertical deflection signal [V].
        __lateral_deflection (float): The lateral deflection signal [V].
        __photodiode_sum (float): The sum of photodiode signals [V].
        __X (float): The X-axis position signal [V].
        __Y (float): The Y-axis position signal [V].
        __Z (float): The Z-axis position signal [V].
        __amplitude (float): The amplitude of the signal [V].
        __phase (float): The phase of the signal [degrees].
        __exc_amplitude (float): The excitation amplitude [V].
        __exc_phase (float): The excitation phase [degrees].
    
    Methods:
        init_signals_with_params: Initializes an instance with specific signal values.
        get_signals: Retrieves the current signal values from the system.
        set_signals: Sets the signal values on the system.
    """
    
    def __init__(self):
        self.get_signals()
        
    @classmethod
    def init_signals_with_params(cls, vertical_deflection, lateral_deflection, photodiode_sum, X, Y, Z, amplitude, phase, exc_amplitude, exc_phase):
        """Initialize the instance with specific values for all attributes"""
        instance = cls()       
        instance.set_signals(vertical_deflection, lateral_deflection, photodiode_sum, X, Y, Z, amplitude, phase, exc_amplitude, exc_phase)
        return instance
    
    def get_signals(self):
        """Get the actual scanning status of the system"""
        # self.__vertical deflection = 0  # Read that from target system [V]
        # self.__lateral deflection = 0  # Read that from target system [V]
        # self.__photodiode_sum = 0  # Read that from target system [V]
        # self.__X = 0  # Read that from target system [V]
        # self.__Y = 0  # Read that from target system [V]
        # self.__Z = 0  # Read that from target system [V]
        # self.__amplitude = 0  # Read that from target system [V]
        # self.__phase = 0  # Read that from target system [deg]
        # self.__exc_amplitude = 0  # Read that from target system [V]
        # self.__exc_phase = 0  # Read that from target system [deg]

        # Retrieve these values from the target system
        
        pass
    
    def set_signals(self, vertical_deflection, lateral_deflection, photodiode_sum, X, Y, Z, amplitude, phase, exc_amplitude, exc_phase):
        """Set scan control parameters on the target system"""
        self.__vertical_deflection = vertical_deflection
        self.__lateral_deflection = lateral_deflection
        self.__photodiode_sum = photodiode_sum
        self.__X = X
        self.__Y = Y
        self.__Z = Z
        self.__amplitude = amplitude
        self.__phase= phase
        self.__exc_amplitude = exc_amplitude
        self.__exc_phase = exc_phase
        # Update these values on the target system if necessary

    @property
    def vertical_deflection(self):
        """The 'vertical_deflection' property getter"""
        return self.__vertical_deflection    
 
    @property
    def lateral_deflection(self):
        """The 'lateral_deflection' property getter"""
        return self.__lateral_deflection   
    
    @property
    def photodiode_sum(self):
        """The 'photodiode_sum' property getter"""
        return self.__photodiode_sum
    
    @property
    def X(self):
        """The 'X' property getter"""
        return self.__X   
    
    @property
    def Y(self):
        """The 'Y' property getter"""
        return self.__Y    
    
    @property
    def Z(self):
        """The 'Z' property getter"""
        return self.__Z    
    
    @property
    def amplitude(self):
        """The 'amplitude' property getter"""
        return self.__amplitude    
    
    @property
    def phase(self):
        """The 'phase' property getter"""
        return self.__phase    
    
    @property
    def exc_amplitude(self):
        """The 'exc_amplitude' property getter"""
        return self.__exc_amplitude    
    
    @property
    def exc_phase(self):
        """The 'exc_phase' property getter"""
        return self.__exc_phase    
    
    def __repr__(self):
        return (f"Signals("
                f"vertical_deflection={self.__vertical_deflection}, "
                f"lateral_deflection={self.__lateral_deflection}, "
                f"photodiode_sum={self.__photodiode_sum}, "
                f"X={self.__X}, "
                f"Y={self.__Y}, "
                f"Z={self.__Z}, "
                f"amplitude={self.__amplitude}, "
                f"phase={self.__phase}, "
                f"exc_amplitude={self.__exc_amplitude}, "
                f"exc_phase={self.__exc_phase} "
                f")")

class ScanParameters:   
    """
    A class to handle scan parameters for a scanning system.
    
    This class provides methods to set and get scan parameters, ensuring
    that the parameters stay within the defined bounds. It also checks if the
    scan area is within the limits defined by the maximum scan dimensions.
    
    Attributes:
        max_scan_x (float): The maximum allowed scan width.
        max_scan_y (float): The maximum allowed scan height.
        max_scan_speed (float): The maximum allowed scan speed.
        min_scan_speed (float): The minimum allowed scan speed.
        max_pixels_x (int): The maximum allowed pixels in the x-axis.
        max_pixels_y (int): The maximum allowed pixels in the y-axis.
        __width (float): Width of the scan area [m].
        __height (float): Height of the scan area [m].
        __rotation (float): Rotation of the scan area [deg].
        __offset_x (float): X offset of the scan area [m].
        __offset_y (float): Y offset of the scan area [m].
        __scan_speed (float): Speed of the scan [Hz].
        __pixels_x (int): Number of pixels in the x-axis.
        __pixels_y (int): Number of pixels in the y-axis.
        __tilt_x (float): Tilt in the x-axis [%].
        __tilt_y (float): Tilt in the y-axis [%].
        __close_loopXY (bool): Close loop control for XY plane.
        __close_loopZ (bool): Close loop control for Z-axis.
    
    Methods:
        init_scan_parameters_with_params: Initializes an instance with specific scan parameters.
        get_scan_parameters: Gets the current scan parameters from the system.
        set_scan_parameters: Sets the scan parameters on the system.
        __is_scan_area_out_of_bounds: Checks if the scan area is within bounds.
    """
    
    # Common for all created ScanParameters objects 
    max_scan_x = -1 # Init value [m]
    max_scan_y = -1 # Init value [m]
    max_scan_speed = -1 # Init value [Hz]
    min_scan_speed = -1 # Init value [Hz]
    max_pixels_x = -1 # Init value 
    max_pixels_y = -1 # Init value 
    
    def __init__(self):   
        # Acquire all scan parameters from the target system
        self.get_scan_parameters()

    @classmethod
    def init_scan_parameters_with_params(cls, width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ):
        """Initialize the instance with specific values for all attributes"""
        # Initialize the instance with specific values for all attributes
        instance = cls()
        
        instance.set_scan_parameters(width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ)
        return instance
        
    def get_scan_parameters(self):
        """Get the actual scanning parameters of the system"""
        # self.__width = -1  # Read that from target system [m]
        # self.__height = -1  # Read that from target system [m]
        # self.__rotation = -1  # Read that from target system [deg]
        # self.__offset_x = -1  # Read that from target system [m]
        # self.__offset_y = -1  # Read that from target system [m]
        # self.__scan_speed = -1  # Read that from target system [Hz]
        # self.__pixels_x = -1  # Read that from target system
        # self.__pixels_y = -1  # Read that from target system
        # self.__tilt_x = -1  # Read that from target system [%]
        # self.__tilt_y = -1  # Read that from target system [%]
        # self.__close_loopXY = False  # Read that from target system
        # self.__close_loopZ = False  # Read that from target system
        
        # self.max_scan_x = -1 # Init value [m]
        # self.max_scan_y = -1 # Init value [m]
        # self.max_scan_speed = -1 # Init value [Hz]
        # self.min_scan_speed = -1 # Init value [Hz]
        # self.max_pixels_x = -1 # Init value
        # self.max_pixels_y = -1 # Init value

        # Retrieve these values from the target system     
        
        pass
    
    def set_scan_parameters(self, width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ):
        """Set scan parameters on the target system"""
        self.__width = width
        self.__height = height
        self.__rotation = rotation
        self.__offset_x = offset_x
        self.__offset_y = offset_y
        self.__scan_speed = scan_speed
        self.__pixels_x = pixels_x
        self.__pixels_y = pixels_y
        self.__tilt_x = tilt_x
        self.__tilt_y = tilt_y
        self.__close_loopXY = close_loopXY
        self.__close_loopZ = close_loopZ

        # Update these values on the target system if necessary   
    
    @property
    def width(self):
        """The 'width' property getter"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """The 'width' property setter"""
        temp_value  = self.__width # To save the value in case of out of bounds
        self.__width = value
        if self.__is_scan_area_out_of_bounds(self.__width, self.__height, self.__rotation, self.__offset_x, self.__offset_y, self.__max_scan_x, self.__max_scan_y):
            # Width out of bounds
            self.__width = temp_value
            raise ValueError("Width out of bounds")
        else:
            # Set scan parameter on the target system   
            pass
            
    @property
    def height(self):
        """The 'height' property getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """The 'height' property setter"""
        temp_value  = self.__height # To save the value in case of out of bounds
        self.__height = value
        if self.__is_scan_area_out_of_bounds(self.__width, self.__height, self.__rotation, self.__offset_x, self.__offset_y, self.__max_scan_x, self.__max_scan_y):
            # Height out of bounds
            self.__height = temp_value
            raise ValueError("Height out of bounds")
        else:
            # Set scan parameter on the target system   
            pass
             
    @property
    def rotation(self):
        """The 'rotation' property getter"""
        return self.__rotation
    
    @rotation.setter
    def rotation(self, value):
        """The 'rotation' property setter"""
        temp_value  = self.__rotation # To save the value in case of out of bounds
        self.__rotation = value
        if self.__is_scan_area_out_of_bounds(self.__width, self.__height, self.__rotation, self.__offset_x, self.__offset_y, self.__max_scan_x, self.__max_scan_y):
            # Rotation out of bounds
            self.__rotation = temp_value
            raise ValueError("Rotation out of bounds")
        else:
            # Set scan parameter on the target system   
            pass
                
    @property
    def offset_x(self):
        """The 'offset_x' property getter"""
        return self.__offset_x
    
    @offset_x.setter
    def offset_x(self, value):
        """The 'offset_x' property setter"""
        temp_value  = self.__offset_x # To save the value in case of out of bounds
        self.__offset_x = value
        if self.__is_scan_area_out_of_bounds(self.__width, self.__height, self.__rotation, self.__offset_x, self.__offset_y, self.__max_scan_x, self.__max_scan_y):
            # Offset_x out of bounds
            self.__offset_x = temp_value
            raise ValueError("Offset X out of bounds")
        else:
            # Set scan parameter on the target system   
            pass
                
    @property
    def offset_y(self):
        """The 'offset_y' property getter"""
        return self.__offset_y
    
    @offset_y.setter
    def offset_y(self, value):
        """The 'offset_y' property setter"""
        temp_value  = self.__offset_y # To save the value in case of out of bounds
        self.__offset_y= value
        if self.__is_scan_area_out_of_bounds(self.__width, self.__height, self.__rotation, self.__offset_x, self.__offset_y, self.__max_scan_x, self.__max_scan_y):
            # Offset_y out of bounds
            self.__offset_y = temp_value
            raise ValueError("Offset Y out of bounds")
        else:
            # Set scan parameter on the target system   
            pass
             
    @property
    def scan_speed(self):
        """The 'scan_speed' property getter"""
        return self.__scan_speed
    
    @scan_speed.setter
    def scan_speed(self, value):
        """The 'scan_speed' property setter"""
        if self.min_scan_speed <= value <= self.max_scan_speed:
            self.__scan_speed = value
            # Set scan parameter on the target system   
        else:
            raise ValueError("Scan speed out of bounds")
                         
    @property
    def pixels_x(self):
        """The 'pixels_x' property getter"""
        return self.__pixels_x
    
    @pixels_x.setter
    def pixels_x(self, value):
        """The 'pixels_x' property setter"""
        if 0 < value <= self.max_pixels_x:
            self.__pixels_x = value
            # Set scan parameter on the target system   
        else:
            raise ValueError("Pixels X out of bounds")
                         
    @property
    def pixels_y(self):
        """The 'pixels_y' property getter"""
        return self.__pixels_y
    
    @pixels_y.setter
    def pixels_y(self, value):
        """The 'pixels_y' property setter"""
        if 0 < value <= self.max_pixels_y:
            self.__pixels_y = value
            # Set scan parameter on the target system   
        else:
            raise ValueError("Pixels Y out of bounds")
                         
    @property
    def tilt_x(self):
        """The 'tilt_x' property getter"""
        return self.__tilt_x
    
    @tilt_x.setter
    def tilt_x(self, value):
        """The 'tilt_x' property setter"""
        if 0 <= value < 100:
            self.__tilt_x = value
            # Set scan parameter on the target system   
        else:
            raise ValueError("Tilt X out of bounds")
                         
    @property
    def tilt_y(self):
        """The 'tilt_y' property getter"""
        return self.__tilt_y
    
    @tilt_y.setter
    def tilt_y(self, value):
        """The 'width' property setter"""
        if 0 <= value < 100:
            self.__tilt_y = value
            # Set scan parameter on the target system   
        else:
            raise ValueError("Tilt Y out of bounds")
                         
    @property
    def close_loopXY(self):
        """The 'close_loopXY' property getter"""
        return self.__close_loopXY
    
    @close_loopXY.setter
    def close_loopXY(self, value):
        """The 'close_loopXY' property setter"""
        self.__close_loopXY = value
        # Set scan parameter on the target system   
        
    @property
    def close_loopZ(self):
        """The 'close_loopZ' property getter"""
        return self.__close_loopZ
    
    @close_loopZ.setter
    def close_loopZ(self, value):
        """The 'close_loopZ' property setter"""
        self.__close_loopZ = value
        # Set scan parameter on the target system  
        
    def __is_scan_area_out_of_bounds(self, width, height, rotation, offset_x, offset_y, max_scan_x, max_scan_y):
        """Private method to check if the scan area is within the allowed bounds."""
        # Convert rotation angle to radians
        rotation_rad = math.radians(rotation)
        
        # Calculate the four corners of the rectangle before rotation
        corners = [
            (-width / 2, -height / 2),
            (width / 2, -height / 2),
            (width / 2, height / 2),
            (-width / 2, height / 2)
        ]
        
        # Rotate the corners around the origin (0, 0)
        rotated_corners = []
        for x, y in corners:
            x_rot = x * math.cos(rotation_rad) - y * math.sin(rotation_rad)
            y_rot = x * math.sin(rotation_rad) + y * math.cos(rotation_rad)
            rotated_corners.append((x_rot, y_rot))
        
        # Offset the rotated corners
        offset_corners = [(x + offset_x, y + offset_y) for x, y in rotated_corners]
        
        # Find the bounding box of the rotated rectangle
        min_x = min(x for x, y in offset_corners)
        max_x = max(x for x, y in offset_corners)
        min_y = min(y for x, y in offset_corners)
        max_y = max(y for x, y in offset_corners)
        
        # Check if the bounding box is out of the defined limits
        if min_x < 0 or max_x > max_scan_x or min_y < 0 or max_y > max_scan_y:
            return True  # The scan area is out of bounds
        return False  # The scan area is within bounds
                    
    def __repr__(self):
        return (
            f"ScanParameters("
            f"width={self.__width}, "
            f"height={self.__height}, "
            f"rotation={self.__rotation}, "
            f"offset_x={self.__offset_x}, "
            f"offset_y={self.__offset_y}, "
            f"scan_speed={self.__scan_speed}, "
            f"pixels_x={self.__pixels_x}, "
            f"pixels_y={self.__pixels_y}, "
            f"tilt_x={self.__tilt_x}, "
            f"tilt_y={self.__tilt_y}, "
            f"close_loopXY={self.__close_loopXY}, "
            f"close_loopZ={self.__close_loopZ}, "
            f"max_scan_x={ScanParameters.max_scan_x}, "
            f"max_scan_y={ScanParameters.max_scan_y}, "
            f"max_scan_speed={ScanParameters.max_scan_speed}, "
            f"min_scan_speed={ScanParameters.min_scan_speed}, "
            f"max_pixels_x={ScanParameters.max_pixels_x}, "
            f"max_pixels_y={ScanParameters.max_pixels_y})"
        )


class ScanControl:   
    """
    A class to control scanning operations for a given system.
    
    This class provides methods to start, stop, and manage scanning operations, 
    including setting parameters such as the scan direction, bounce mode, continuous scan, 
    auto-save options, and file paths. It ensures proper validation and encapsulation of 
    the parameters used in the scanning process.
    
    Attributes:
        __isScanningUp (bool): Indicates if the scanning is in the upward direction.
        __isScanningDown (bool): Indicates if the scanning is in the downward direction.
        __isBouncing (bool): Indicates if the scanning is in bouncing mode.
        __isContinuousScan (bool): Indicates if the scanning is continuous.
        __isAutoSave (bool): Indicates if auto-save is enabled.
        __path (str): Path where the scan results will be saved.
        __file_name (str): Name of the file where the scan results will be saved.
    
    Methods:
        init_scan_control_with_params: Initializes the instance with specific values for all attributes.
        get_scan_control_parameters: Get the actual scanning status of the system.
        set_scan_control_parameters: Sets parameters on the target system.
        scan_up: Starts scanning in the upward direction.
        scan_down: Starts scanning in the downward direction.
        scan_bouncing: Starts bouncing scan.
        scan_stop: Stops scanning.
        scan_pause: Pauses scanning.
        scan_resume: Resumes scanning.
        scan_continuous: Enables or disables continuous scan.
        scan_auto_save: Enables or disables auto-save.
        scan_save_now: Saves current scan data immediately.
        is_scanning: Checks if scanning is active.
        is_paused: Checks if scanning is paused.
        get_pixel_pos: Retrieve the actual scanning XY pixel numbers.
        get_xyposition: Retrieve the actual XY scanner position.
        set_xyposition: Move the tip to the desired XY position.
        do_ramp_absolute: Performs a Z ramp with absolute starting and ending points.
        do_ramp_absolute_length: Performs a Z ramp with absolute starting point and ramp length.
        do_ramp_absolute_trig: Performs a Z ramp with an absolute starting point and a trigger-based endpoint.
        do_ramp_relative_length: Performs a Z ramp relative to the actual position with specified length.
        do_ramp_relative_trig: Performs a Z ramp relative to the actual position with a trigger-based endpoint.
    """
    
    def __init__(self):
        self.get_scan_control_parameters()
        
    @classmethod
    def init_scan_control_with_params(cls, isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name):
        """Initialize the instance with specific values for all attributes"""
        instance = cls()       
        instance.set_scan_control_parameters(isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name)
        return instance
    
    def get_scan_control_parameters(self):
        """Get the actual scanning status of the system"""
        # self.__isScanningUp = False  # Read that from target system
        # self.__isScanningDown = False  # Read that from target system
        # self.__isBouncing = False  # Read that from target system
        # self.__isContinuousScan = False  # Read that from target system
        # self.__isAutoSave = False  # Read that from target system
        # self.__path = ''  # Read that from target system
        # self.__file_name = ''  # Read that from target system
        
        # Retrieve these values from the target system
        
        pass
    
    def set_scan_control_parameters(self, isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name):
        """Set scan control parameters on the target system"""
        self.__isScanningUp = isScanningUp
        self.__isScanningDown = isScanningDown
        self.__isBouncing = isBouncing
        self.__isContinuousScan = isContinuousScan
        self.__isAutoSave = isAutoSave
        self.__path = path
        self.__file_name = file_name
        # Update these values on the target system if necessary

    @property
    def isScanningUp(self):
        """The 'isScanningUp' property getter"""
        return self.__isScanningUp
    
    @isScanningUp.setter
    def isScanningUp(self, value):
        """The 'isScanningUp' property setter"""
        if value:
            self.scan_up()
        elif self.__isScanningUp:
            self.scan_stop()
            
    def scan_up(self):
        """Start scanning up"""
        self.__isScanningUp = True
        self.__isScanningDown = False
        self.__isBouncing = False
        # Implement scan control parameters on the target system        
            
    @property
    def isScanningDown(self):
        """The 'isScanningDown' property getter"""
        return self.__isScanningDown
    
    @isScanningDown.setter
    def isScanningDown(self, value):
        """The 'isScanningDown' property setter"""
        if value:
            self.scan_down()
        elif self.__isScanningDown:
            self.scan_stop()   
    
    def scan_down(self):
        """Start scanning down"""
        self.__isScanningUp = False
        self.__isScanningDown = True
        self.__isBouncing = False
        # Implement scan control parameters on the target system
    
    @property
    def isBouncing(self):
        """The 'isBouncing' property getter"""
        return self.__isBouncing
    
    @isBouncing.setter
    def isBouncing(self, value):
        """The 'isBouncing' property setter"""
        if value:
            self.scan_bouncing()
        elif self.__isBouncing:
            self.scan_stop()      

    def scan_bouncing(self):
        """Start bouncing scan"""
        self.__isScanningUp = False
        self.__isScanningDown = False
        self.__isBouncing = True
        # Implement scan control parameters on the target system
    
    def scan_stop(self):
        """Stop scanning"""
        self.__isScanningUp = False
        self.__isScanningDown = False
        self.__isBouncing = False
        # Implement scan control parameters on the target system
       
    def scan_pause(self):
        """Pause scanning"""
        # Implement scan control parameters on the target system
        pass
    
    def scan_resume(self):
        """Resume scanning"""
        # Implement scan control parameters on the target system
        pass     

    @property
    def path(self):
        """The 'path' property getter"""
        return self.__path
    
    @path.setter
    def path(self, value):
        """The 'path' property setter"""
        if not os.path.exists(value):
            os.makedirs(value)  # Create the directory if it does not exist
        self.__path = value    
        # Implement scan control parameters on the target system
    
    @property
    def file_name(self):
        """The 'file_name' property getter"""
        return self.__file_name 

    @file_name.setter
    def file_name(self, value):
        """The 'file_name' property setter"""
        if not re.match(r'^[\w\-. ]+$', value):
            raise ValueError(f"The file name '{value}' is not valid.")
        self.__file_name = value
        # Implement scan control parameters on the target system

    @property
    def isContinuousScan(self):
        """The 'isContinuousScan' property getter"""
        return self.__isContinuousScan
    
    @isContinuousScan.setter
    def isContinuousScan(self, value):
        """The 'isContinuousScan' property setter"""
        self.__isContinuousScan = value
        self.scan_continuous(value)
        
    def scan_continuous(self, value):
        """Enable or disable continuous scan"""
        self.__isContinuousScan = value
        # Implement scan control parameters on the target system
        
    @property
    def isAutoSave(self):
        """The 'isAutoSave' property getter"""
        return self.__isAutoSave
    
    @isAutoSave.setter
    def isAutoSave(self, value):
        """The 'isAutoSave' property setter"""
        self.__isAutoSave = value
        self.scan_auto_save(value)
    
    def scan_auto_save(self, value):
        """Enable or disable auto-save"""
        self.__isAutoSave = value
        # Implement scan control parameters on the target system
     
    def scan_save_now(self):
        """Save current scan data immediately"""
        # Implement scan control parameters on the target system
        pass
    
    def is_scanning(self):
        """Check if scanning is active"""
        # Implement scan control parameters on the target system
        pass
    
    def is_paused(self):
        """Check if scanning is paused"""
        # Implement scan control parameters on the target system
        pass
    
    def get_pixel_pos(self):
        """Retrieve the actual scanning XY pixel numbers"""
        # Implement scan control parameters on the target system
        pass
    
    def get_xyposition(self):
        """Retrieve the actual XY scanner position"""
        # Implement scan control parameters on the target system
        pass
    
    def set_xyposition(self, x, y, forced = False):
        """Move the tip to the desired XY position"""
        if self.__isScanningUp or self.__isScanningUp or self.__isScanningUp: # If scanning
            if forced: # If scanning, it is forced to stop and move the the desired position
                self.scan_stop()
                # Implement scan control parameters on the target system
                pass
        else:
            # Implement scan control parameters on the target system
            pass

    def do_ramp_absolute(self, init, end, N, speed_f, speed_b, wait_s):
        """
        Perform a Z ramp with absolute starting and ending points.
    
        Args:
            init (float): Initial position in meters [m].
            end (float): Final position in meters [m].
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second [m/s].
            speed_b (float): Backward speed in meters per second [m/s].
            wait_s (float): Waiting time at the turnaround point in seconds [s].
    
        This method controls the ramp by defining absolute starting and ending points for the Z ramp,
        at specific forward and backward speeds, with a waiting period at the turnaround point.
        """
        # Implement scan control parameters on the target system
        pass
    
    def do_ramp_absolute_length(self, init, length, N, speed_f, speed_b, wait_s):
        """
        Perform a Z ramp with absolute starting and total ramp length.
    
        Args:
            init (float): Initial position in meters [m].
            length (float): Length of the Z movement in meters [m].
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second [m/s].
            speed_b (float): Backward speed in meters per second [m/s].
            wait_s (float): Waiting time at the turnaround point in seconds [s].
    
        This method controls the ramp by defining absolute starting and  and length for the Z ramp,
        at specific forward and backward speeds, with a waiting period at the turnaround point.
        """
        # Implement scan control parameters on the target system
        pass
    
    def do_ramp_absolute_trig(self, init, trig_val, trig_signal, trig_sig, N, speed_f, speed_b, wait_s):
        """
        Perform a Z ramp with an absolute starting point and a trigger-based endpoint.
    
        Args:
            init (float): Initial position in meters [m].
            trig_val (float): Trigger value that determines when to end the ramp [m].
            trig_signal (str): The signal used for triggering (e.g., force or voltage).
            trig_sig (str): The trigger condition, either '>' or '<', defining whether the ramp stops 
                            when the signal exceeds or drops below `trig_val`.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second [m/s].
            speed_b (float): Backward speed in meters per second [m/s].
            wait_s (float): Waiting time at the turnaround point in seconds [s].
    
        This method controls the ramp by defining an absolute starting point and a dynamic endpoint
        based on a trigger condition (`trig_sig`). The ramp will stop when `trig_signal` meets the condition 
        defined by `trig_sig` (either `>` or `<`) in relation to `trig_val`, while the speed and number of 
        steps are also specified. The scan will pause for `wait_s` seconds at the turnaround point.
        """
        # Implement scan control parameters on the target system
        pass
    
    def do_ramp_relative_length(self, init, length, N, speed_f, speed_b, wait_s):
        """
        Perform a Z ramp relative to the actual position.
    
        Args:
            init (float): Initial position in meters [m] relative to the actual position.
            length (float): Length of the Z movement in meters [m].
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second [m/s].
            speed_b (float): Backward speed in meters per second [m/s].
            wait_s (float): Waiting time at the turnaround point in seconds [s].
    
        This method controls the ramp by defining absolute starting points and length for the Z ramp,
        at specific forward and backward speeds, with a waiting period at the turnaround point.
        """
        # Implement scan control parameters on the target system
        pass
    
    def do_ramp_relative_trig(self, init, trig_val, trig_signal, trig_sig, N, speed_f, speed_b, wait_s):
        """
        Perform a Z ramp relative to the actual position and a trigger-based endpoint.
    
        Args:
            init (float): Initial position in meters [m] relative to the actual position.
            trig_val (float): Trigger value that determines when to end the ramp [m].
            trig_signal (str): The signal used for triggering (e.g., force or voltage).
            trig_sig (str): The trigger condition, either '>' or '<', defining whether the ramp stops 
                            when the signal exceeds or drops below `trig_val`.
            N (int): Number of steps in the ramp.
            speed_f (float): Forward speed in meters per second [m/s].
            speed_b (float): Backward speed in meters per second [m/s].
            wait_s (float): Waiting time at the turnaround point in seconds [s].
    
        This method controls the ramp by defining an absolute starting point and a dynamic endpoint
        based on a trigger condition (`trig_sig`). The ramp will stop when `trig_signal` meets the condition 
        defined by `trig_sig` (either `>` or `<`) in relation to `trig_val`, while the speed and number of 
        steps are also specified. The scan will pause for `wait_s` seconds at the turnaround point.
        """
        # Implement scan control parameters on the target system
        pass

    def __repr__(self):
        return (f"ScanControl("
                f"isScanningUp={self.__isScanningUp}, "
                f"isScanningDown={self.__isScanningDown}, "
                f"isBouncing={self.__isBouncing}, "
                f"isContinuousScan={self.__isContinuousScan}, "
                f"isAutoSave={self.__isAutoSave}, "
                f"path={self.__path}, "
                f"file_name={self.__file_name})")

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
    def __init__(self):
        self.image_data = []  # Get data from the target system

        # Implement image control on the target system

    def save(self, filepath):
        # Implement saving logic here
        pass
    
    def get_image(self):
        # Implement acquiring logic here
        pass

    def __repr__(self):
        return f"AcquiredImage(image_data={self.image_data})"


class Motors:
    # Z motor, XY motors, readout laser motor, excitation laser motor
    pass


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
