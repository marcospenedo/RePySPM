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
    """
    
    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController
    
    def get_channels_units(self):
        """Retrieve the units of all image channels."""
        pass
    
    def get_channels_names(self):
        """Retrieve the names of all image channels."""
        pass
    
    def get_all_channels_data(self):
        """Retrieve the data from all image channels."""
        pass
    
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
        control = "ImageChannels"
        command = f"{OHCcommands.r_sco}{control}"
        all_channels = np.array(self.controller.read_control(command, control))  # Shape: (2, num_channels, pixels_x, pixels_y)
    
        # Retrieve channel names
        control = "ChannelsNames"
        command = f"{OHCcommands.r_sco}{control}"
        channel_names = self.controller.read_control(command, control)  # Shape: (num_channels,)
    
        if not isinstance(channel_names, list):
            raise ValueError(f"Expected a list of channel names, but got {type(channel_names)}.")
    
        if name not in channel_names:
            raise ValueError(f"Channel '{name}' not found. Available channels: {channel_names}")
    
        # Find the index of the requested channel
        channel_index = channel_names.index(name)
    
        # Extract and return the data for the corresponding channel
        return all_channels[direction, channel_index, :, :]

    
    def __repr__(self):
        return (
            f"{self.__class__.__name__}()"
        )
   