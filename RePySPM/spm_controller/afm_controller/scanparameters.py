import aespm as ae

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

    def set_scan_parameters(
        self, width=None, height=None, rotation=None, offset_x=None, offset_y=None, scan_speed=None, 
        pixels_x=None, pixels_y=None, tilt_x=None, tilt_y=None, close_loopXY=None, close_loopZ=None
    ):
        """Sets all scan parameters on the system."""
        # pass
        # We'd better use a single dict 'p' as the input here.
        p_input = {
            'width': width,
            'height': height,
            'rotation': rotation,
            'offset_x': offset_x,
            'offset_y': offset_y,
            'scan_speed': scan_speed,
            'pixels_x': pixels_x,
            'pixels_y': pixels_y,
            'tilt_x': None,
            'tilt_y': None,
            'close_loopXY': None,
            'close_loopZ': None,
        }
        p_control = {
            'width': 'ScanSize',
            'height': 'ScanSize',
            'rotation': 'ScanAngle',
            'offset_x': 'XOffset',
            'offset_y': 'YOffset',
            'scan_speed': 'ScanRate',
            'pixels_x': 'Points',
            'pixels_y': 'Points',
            'tilt_x': 'tilt_x',
            'tilt_y': 'tilt_y',
            'close_loopXY': 'close_loopXY',
            'close_loopZ': 'close_loopZ',
        }
        for key, item in p_input:
            if item is not None:
                ae.spm_control(p_control[key], item)

    def get_scan_parameters(self):
        """Retrieves all current scan parameters from the system."""
        # pass
        keys = ['ScanSize', 'ScanRate', 'ScanPoints', 'ScanAngle', 'AmplitudeSetpointVolts', 'DriveAmplitude', 'DriveFrequency', 
                'DeflectionSetpointVolts', 'ImagingMode', 'ScanDown', 'ZIgain',]
        params = {}
        values = ae.read_spm(key=keys)
        for i, ix in enumerate(keys):
            params[ix] = values[i]
        self.param = params
        return params

    def get_width(self):
        """Retrieves the current width of the scan area."""
        # pass
        return ae.read_spm(key=['ScanSize'])

    def set_width(self, value):
        """Sets the width of the scan area."""
        # pass
        ae.spm_control('ScanSize', value)

    def get_height(self):
        """Retrieves the current height of the scan area."""
        pass

    def set_height(self, value):
        """Sets the height of the scan area."""
        pass

    def get_rotation(self):
        """Retrieves the current rotation of the scan area."""
        # pass
        return ae.read_spm(key=['ScanAngle'])

    def set_rotation(self, value):
        """Sets the rotation of the scan area."""
        # pass
        ae.spm_control('ScanAngle', value)

    def get_offset_x(self):
        """Retrieves the current X offset of the scan area."""
        # pass
        return ae.read_spm(key=['XOffset'])

    def set_offset_x(self, value):
        """Sets the X offset of the scan area."""
        # pass
        ae.spm_control('XOffset', value)

    def get_offset_y(self):
        """Retrieves the current Y offset of the scan area."""
        # pass
        return ae.read_spm(key=['YOffset'])

    def set_offset_y(self, value):
        """Sets the Y offset of the scan area."""
        # pass
        ae.spm_control('YOffset', value)

    def get_scan_speed(self):
        """Retrieves the current scan speed."""
        # pass
        return ae.read_spm(key=['ScanRate'])

    def set_scan_speed(self, value):
        """Sets the scan speed."""
        # pass
        ae.spm_control('ScanRate', value)

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
