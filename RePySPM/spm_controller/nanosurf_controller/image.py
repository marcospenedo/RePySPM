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
        read_nid: Reads a Nanosurf .nid measurement file and returns the reader object.
        read_nhf: Reads a Nanosurf Studio .nhf measurement file and returns the reader object.
    """

    def __init__(self, controller):
        self.controller = controller
        self._app = controller._app

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
        pass

    def get_channels_units_ramp(self):
        """Retrieve the units of all ramp channels."""
        pass

    def get_channels_names_ramp(self):
        """Retrieve the names of all ramp channels."""
        pass

    def get_all_channels_data_ramp(self):
        """Retrieve the data from all ramp channels."""
        pass

    def get_channel_ramp(self, name):
        """Retrieve the data from the ramp channel with the given name."""
        pass

    def get_last_line(self, name):
        """Retrieves the data of the last line of a specific channel."""
        pass

    def get_all_last_lines(self):
        """Retrieves the data for all last channels line."""
        pass

    def read_nid(self, file_path):
        """Reads a Nanosurf .nid measurement file and returns the reader object.

        Args:
            file_path (str): Path to the .nid file.

        Returns:
            NIDFileReader: Reader object with the loaded measurement data.
        """
        import nanosurf
        reader = nanosurf.util.nid_reader.NIDFileReader()
        reader.read(file_path)
        return reader

    def read_nhf(self, file_path):
        """Reads a Nanosurf Studio .nhf measurement file and returns the reader object.

        Args:
            file_path (str): Path to the .nhf file.

        Returns:
            NHFFileReader: Reader object with the loaded measurement data.
        """
        import nanosurf
        reader = nanosurf.util.nhf_reader.NHFFileReader(verbose=False)
        reader.read(file_path)
        return reader

    def __repr__(self):
        return f"{self.__class__.__name__}()"
