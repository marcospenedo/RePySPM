from .commands import OHCcommands

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

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def set_scan_parameters(
        self, width, height, rotation, offset_x, offset_y, scan_speed, pixels_x, pixels_y, tilt_x, tilt_y, close_loopXY, close_loopZ
    ):
        """Sets all scan parameters on the system."""
        self.set_width(width)
        self.set_height(height)
        self.set_rotation(rotation)
        self.set_offset_x(offset_x)
        self.set_offset_y(offset_y)
        self.set_scan_speed(scan_speed)
        self.set_pixels_x(pixels_x)
        self.set_pixels_y(pixels_y)
        
        return 0

    def get_scan_parameters(self):
        """Retrieves all current scan parameters from the system."""
        
        return [self.set_width(), self.set_height(), self.set_rotation(), self.set_offset_x(), self.set_offset_y(), self.set_scan_speed(), self.set_pixels_x(), self.set_pixels_y(), 0, 0, False, False]

    def get_width(self):
        """Retrieves the current width of the scan area."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[0]

    def set_width(self, value):
        """Sets the width of the scan area."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Width:{value}"
            
        self.controller.write_control(command)
        
        return 0
    
    def get_height(self):
        """Retrieves the current height of the scan area."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[1]

    def set_height(self, value):
        """Sets the height of the scan area."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Height:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_rotation(self):
        """Retrieves the current rotation of the scan area."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[4]

    def set_rotation(self, value):
        """Sets the rotation of the scan area."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Angle:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_offset_x(self):
        """Retrieves the current X offset of the scan area."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[2]

    def set_offset_x(self, value):
        """Sets the X offset of the scan area."""

        command = f"{OHCcommands.w_sca}Scan Parameters:X Offset:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_offset_y(self):
        """Retrieves the current Y offset of the scan area."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[3]

    def set_offset_y(self, value):
        """Sets the Y offset of the scan area."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Y Offset:{value}"
            
        self.controller.write_control(command)
        
        return 0
    def get_scan_speed(self):
        """Retrieves the current scan speed."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[7]

    def set_scan_speed(self, value):
        """Sets the scan speed."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Scan Rate:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_pixels_x(self):
        """Retrieves the number of pixels in the X-axis."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[5]

    def set_pixels_x(self, value):
        """Sets the number of pixels in the X-axis."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Pixels:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_pixels_y(self):
        """Retrieves the number of pixels in the Y-axis."""
        
        control = "Scan Parameters"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[6]

    def set_pixels_y(self, value):
        """Sets the number of pixels in the Y-axis."""
        
        command = f"{OHCcommands.w_sca}Scan Parameters:Lines:{value}"
            
        self.controller.write_control(command)
        
        return 0

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
