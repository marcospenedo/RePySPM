from .commands import OHCcommands

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
        get_line: Retrieves the current scanning line.
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
        is_ramping: Checks if the ramping is active.
        get_path_ramp: Retrieves the path for ramp data storage.
        set_path_ramp: Sets the path for ramp data storage.
        get_file_name_ramp: Retrieves the file name for ramp data storage.
        set_file_name_ramp: Sets the file name for ramp data storage.
    """

    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController
        
    def get_scan_control_parameters(self):
        """Retrieves the current scanning parameters from the system."""
        pass

    def set_scan_control_parameters(self, isScanningUp, isScanningDown, isBouncing, isContinuousScan, isAutoSave, path, file_name):
        """Sets the scanning parameters on the system."""
        pass

    def scan_up(self):
        """Starts scanning in the upward direction."""
        
        command = f"{OHCcommands.w_sca}Actions:Frame up:True"
            
        self.controller.write_control(command)
        
        return 0

    def scan_down(self):
        """Starts scanning in the downward direction."""
        
        command = f"{OHCcommands.w_sca}Actions:Frame down:True"
            
        self.controller.write_control(command)
        
        return 0

    def scan_bouncing(self):
        """Starts bouncing scan."""
        
        command = f"{OHCcommands.w_sca}Actions:Bounce:True"
            
        self.controller.write_control(command)
        
        return 0

    def scan_stop(self):
        """Stops scanning."""
        
        command = f"{OHCcommands.w_sca}Actions:Stop:True"
  
        self.controller.write_control(command)
        
        return 0

    def scan_pause(self):
        """Pauses scanning."""
        
        command = f"{OHCcommands.w_sca}Actions:Pause:True"
            
        self.controller.write_control(command)
        
        return 0

    def scan_resume(self):
        """Resumes scanning."""
        
        command = f"{OHCcommands.w_sca}Actions:Pause:False"
            
        self.controller.write_control(command)
        
        return 0

    def scan_continuous(self, value):
        """Enables or disables continuous scan.

        Args:
            value (bool): True to enable continuous scan, False to disable.
        """
        
        command = f"{OHCcommands.w_sca}Actions:Continuous:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_scan_direction(self):
        """Retrieves the current scan direction."""
        pass

    def scan_auto_save(self, value):
        """Enables or disables auto-save.

        Args:
            value (bool): True to enable auto-save, False to disable.
        """
        
        command = f"{OHCcommands.w_sca}Auto Save:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def scan_save_now(self):
        """Saves current scan data immediately."""
        
        command = f"{OHCcommands.w_sca}Save now:True"
            
        self.controller.write_control(command)
        
        return 0

    def is_scanning(self):
        """Checks if scanning is active."""
        
        control = "isScanEnable?"
        command = f"{OHCcommands.r_sco}{control}"
        
        return self.controller.read_control(command, control)

    def is_paused(self):
        """Checks if scanning is paused."""
        
        control = "Actions"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[4]
    
    def isContinuousScan(self):
        """Checks if continuous scanning is enabled."""
        
        control = "Actions"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)[3]

    def isAutoSave(self):
        """Checks if auto-save is enabled."""
        
        control = "Auto Save"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)

    def get_pixel_pos(self):
        """Retrieves the current scanning XY pixel numbers."""
        pass
    
    def get_line(self):
        """Retrieves the current scanning line."""
        
        control = "Line"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)

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
        if forced:
            self.controller.scan_control.scan_stop()
            
            # Set 0 scan site to place it with offset to the desired position
            self.controller.scan_parameters.set_width(1*10-12) 
            self.controller.scan_parameters.set_height(1*10-12) 
            
            self.controller.scan_parameters.set_offset_x(x)
            self.controller.scan_parameters.set_offset_y(y)

    def get_path(self):
        """Retrieves the path associated with the scan."""
        
        control = "Path"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)

    def set_path(self, path):
        """Sets the path associated with the scan.

        Args:
            path (str): Path for the scan.
        """
        
        command = f"{OHCcommands.w_sca}Path:{path}"
            
        self.controller.write_control(command)
        
        return 0

    def get_file_name(self):
        """Retrieves the file name for the scan."""
        
        control = "File name"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)

    def set_file_name(self, file_name):
        """Sets the file name for the scan.

        Args:
            file_name (str): Name of the file.
        """
        command = f"{OHCcommands.w_sca}File name:{file_name}"
            
        self.controller.write_control(command)
        
        return 0

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
        
        command = f"{OHCcommands.w_ram}Trigger Source:Relative Height"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Start:{init}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Distance:{length}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Points:{N}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Fwd:{speed_f}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Bwd:{speed_b}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Parameters:Pause:{wait_s}"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Actions:Play:True"
            
        self.controller.write_control(command)
        
        command = f"{OHCcommands.w_ram}Actions:Play:False"
            
        self.controller.write_control(command)
        
        return 0

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
    
    def is_ramping(self):
        """Checks if the ramping is active."""
        
        control = "Ramping?"
        command = f"{OHCcommands.r_ram}{control}"
        
        control = "Ramping?_"
        
        return self.controller.read_control(command, control)      

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

