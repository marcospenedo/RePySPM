from .commands import OHCcommands
import numpy as np

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
        get_channels_units_ramp: Retrieves the units of all channels in the ramp.
        get_channels_names_ramp: Retrieves the names of all channels in the ramp.
        get_all_channels_data_ramp: Retrieves the data for all ramp channels.
        get_channel_ramp: Retrieves the data of a specific ramp channel by name.
        get_last_line: Retrieves the data for all last channels line.
        get_all_last_lines: Retrieves the data of the last line of a specific channels.
    """
    
    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController
    
    def get_channels_units(self):
        """Retrieve the units of all image channels."""
        pass
    
    def get_channels_names(self):
        """Retrieve the names of all image channels."""
        
        # Retrieve channel names
        control = "ChannelsNames"
        command = f"{OHCcommands.r_sco}{control}"
        
        return self.controller.read_control(command, control)
    
    def get_all_channels_data(self):
        """Retrieve the data from all image channels."""
        
        control = "ImageChannels"
        command = f"{OHCcommands.r_sco}{control}"
        
        return np.array(self.controller.read_control(command, control))  # Shape: (2, num_channels, pixels_x, pixels_y)
    
    def get_channel(self, name: str, direction: int):
        """
        Retrieve the data from the image channel with the given name.
    
        Args:
            name (str): The name of the channel to retrieve.
            direction (int): Direction, either forward (0) or backward (1).
    
        Raises:
            ValueError: If `name` is not a string.
            ValueError: If `direction` is not 0 or 1.
            ValueError: If the channel name is not found.
    
        Returns:
            np.ndarray: The image data corresponding to the requested channel.
        """
        
        if not isinstance(name, str):
            raise ValueError(f"Invalid channel name: {name}. Must be a string.")
    
        if not isinstance(direction, int) or direction not in {0, 1}:
            raise ValueError(f"Invalid direction: {direction}. Must be an integer (0 for forward, 1 for backward).")
    
        # Retrieve all available channels (convert list to NumPy array)
        all_channels = self.get_all_channels_data()
    
        # Retrieve all available channels names
        channel_names = self.get_channels_names()
    
        if not isinstance(channel_names, tuple):
            raise ValueError(f"Expected a list of channel names, but got {type(channel_names)}.")
    
        if name not in channel_names:
            raise ValueError(f"Channel '{name}' not found. Available channels: {channel_names}")
    
        # Find the index of the requested channel
        channel_index = channel_names.index(name)
    
        # Extract and return the data for the corresponding channel
        return all_channels[direction, channel_index, :, :]

    def get_channels_units_ramp(self):
        """Retrieve the units of all ramp channels."""
        pass
    
    def get_channels_names_ramp(self):
        """Retrieve the names of all ramp channels."""
        pass
    
    def get_all_channels_data_ramp(self):
        control = "GraphData"
        command = f"{OHCcommands.r_ram}{control}"
        
        return np.array(self.controller.read_control(command, control))  # Shape: (2xnum_channels, 2, num points)
    
    def get_channel_ramp(self, name):
        """Retrieve the data from the ramp channel with the given name."""
        pass
    
    def get_last_line(self, name):
        """Retrieves the data of the last line of a specific channel."""
        
        if not isinstance(name, str):
            raise ValueError(f"Invalid channel name: {name}. Must be a string.")
    
        # Retrieve all available channels (convert list to NumPy array)
        all_channels = self.get_all_channels_data()
    
        # Retrieve all available channels names
        channel_names = self.get_channels_names()
    
        if not isinstance(channel_names, tuple):
            raise ValueError(f"Expected a list of channel names, but got {type(channel_names)}.")
    
        if name not in channel_names:
            raise ValueError(f"Channel '{name}' not found. Available channels: {channel_names}")
    
        # Find the index of the requested channel
        channel_index = channel_names.index(name)
    
        # Extract and return the data for the corresponding channel line
        line_number = self.controller.scan_control.get_line()
        if line_number > 0:
            return all_channels[:, channel_index, line_number - 1, :]
        else:
            return -1
        
    def get_all_last_lines(self):
        """Retrieves the data for all last channels line."""
        pass
    
    def __repr__(self):
        return (
            f"{self.__class__.__name__}()"
        )
   