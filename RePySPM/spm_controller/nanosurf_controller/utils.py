class Utils:
    """
    A class containing useful functions to control the LBNI OHC.

    Attributes:
        controller: An instance of the AFMController responsible for communication.

    Methods:
        update_waveform_FPGA():
            Sends a command to update the waveform parameters in the FPGA.
        set_waveform_params():
            Sets the parameters for slow and fast waveforms with validation.
        get_waveform_params():
            Retrieves the waveform parameters from the controller.
        set/get_slowwave_N_poits():
            Sets or retrieves the number of points for the slow wave.
        set/get_slowwave_type():
            Sets or retrieves the type of slow wave.
        set/get_slowwave_roundN_poits():
            Sets or retrieves the number of rounding points for the slow wave.
        set/get_fastwave_N_poits():
            Sets or retrieves the number of points for the fast wave.
        set/get_fastwave_type():
            Sets or retrieves the type of fast wave.
        set/get_fastwave_roundN_poits():
            Sets or retrieves the number of rounding points for the fast wave.
        set/get_hysX_type():
            Sets or retrieves the type of hysteresis correction for the X-axis.
        set/get_hysY_type():
            Sets or retrieves the type of hysteresis correction for the Y-axis.
        set/get_hys_corr():
            Sets or retrieves whether hysteresis correction is enabled.
        set/get_res_corr():
            Sets or retrieves whether resonance correction is enabled.
        set/get_hyst_corr_X_path():
            Sets or retrieves the file path for hysteresis correction on the X-axis.
        set/get_hyst_corr_Y_path():
            Sets or retrieves the file path for hysteresis correction on the Y-axis.
        set/get_custom_waveform_X_path():
            Sets or retrieves the file path for a custom waveform on the X-axis.
        set/get_custom_waveform_Y_path():
            Sets or retrieves the file path for a custom waveform on the Y-axis.
        set/get_custom_wav_X():
            Sets or retrieves whether a custom waveform is used for the X-axis.
        set/get_custom_wav_Y():
            Sets or retrieves whether a custom waveform is used for the Y-axis.
        set/get_uni_bi_dir():
            Sets or retrieves whether the scanning is unidirectional or bidirectional.
        set/get_skip_lines():
            Sets or retrieves whether lines are skipped in the scan.
        set/get_feedback_after_ramp():
            Sets the feedback on/off after a ramp.
        set_timeout():
            Sets timeout of the loop that keeps listening the messages.
        set_setpoint_FPGA: Set the setpoint value (in V) on the FPGA using floats.
        set_excitation_amplitude_FPGA: Set the excitation amplitude on the FPGA.
        linear_ramp_setpoint_exc_amplitude: Gradually change the setpoint and excitation amplitude over a specified duration (in milliseconds)
            using float arithmetic
    """

    def __init__(self, controller):
        self.controller = controller
        self._app = controller._app

    def update_waveform_FPGA(self):
        pass

    def set_waveform_params(self, slowN, slowType, slowroundN, fastN, fastType, fastroundN):
        """Set parameters for slow and fast waveforms with validation."""
        pass

    def get_waveform_params(self):
        """Retrieve waveform parameters from the controller."""
        pass

    def set_slowwave_N_points(self, value: int):
        """Set the number of points for the slow wave, ensuring it is greater than 2."""
        pass

    def get_slowwave_N_poits(self):
        pass

    def set_slowwave_type(self, value: str):
        """Set the slow wave type, ensuring it is a valid option."""
        pass

    def get_slowwave_type(self):
        pass

    def set_slowwave_roundN_poits(self, value: int):
        pass

    def get_slowwave_roundN_poits(self):
        pass

    def set_fastwave_N_points(self, value: int):
        """Set the number of points for the fast wave, ensuring it is greater than 2."""
        pass

    def get_fastwave_N_poits(self):
        pass

    def set_fastwave_type(self, value: str):
        """Set the fast wave type, ensuring it is a valid option."""
        pass

    def get_fastwave_type(self):
        pass

    def set_fastwave_roundN_poits(self, value: int):
        pass

    def get_fastwave_roundN_poits(self):
        pass

    def set_hysX_type(self, value: str):
        pass

    def get_hysX_type(self):
        pass

    def set_hysY_type(self, value: str):
        pass

    def get_hysY_type(self):
        pass

    def set_hys_corr(self, value: bool):
        pass

    def get_hys_corr(self):
        pass

    def set_res_corr(self, value: bool):
        pass

    def get_res_corr(self):
        pass

    def update_shift(self):
        pass

    def set_N_shift(self, value: int):
        pass

    def get_N_shift(self):
        pass

    def set_hyst_corr_X_path(self, value: str):
        """Set the hysteresis correction X file path, ensuring it exists."""
        pass

    def get_hyst_corr_X_path(self):
        pass

    def set_hyst_corr_Y_path(self, value: str):
        pass

    def get_hyst_corr_Y_path(self):
        pass

    def set_custom_waveform_X_path(self, value: str):
        pass

    def get_custom_waveform_X_path(self):
        pass

    def set_custom_wav_X(self, value: bool):
        pass

    def get_custom_wav_X(self):
        pass

    def set_custom_waveform_Y_path(self, value: str):
        pass

    def get_custom_waveform_Y_path(self):
        pass

    def set_custom_wav_Y(self, value: bool):
        pass

    def get_custom_wav_Y(self):
        pass

    def set_uni_bi_dir(self, value: bool):
        pass

    def get_uni_bi_dir(self):
        pass

    def set_skip_lines(self, value: bool):
        pass

    def get_skip_lines(self):
        pass

    def set_feedback_after_ramp(self, value: bool):
        pass

    def get_feedback_after_ramp(self):
        pass

    def set_excitation(self, value: bool):
        pass

    def get_excitation(self):
        pass

    def set_timeout(self, value: int):
        """Sets timeout of the loop that keeps listening the messages.

        Args:
            value (int): time in ms.
        """
        pass

    def set_setpoint_FPGA(self, set_point_val):
        """Set the setpoint value (in V) on the FPGA using floats."""
        pass

    def set_excitation_amplitude_FPGA(self, amplitude_val):
        """Set the excitation amplitude on the FPGA."""
        pass

    def linear_ramp_setpoint_exc_amplitude(self, final_setpoint, final_exc_amplitude, duration_ms):
        """
        Gradually change the setpoint and excitation amplitude over a specified duration (in milliseconds)
        using float arithmetic.

        :param final_setpoint: Final setpoint value (float)
        :param final_exc_amplitude: Final excitation amplitude (float)
        :param duration_ms: Duration for the ramp in milliseconds (float/int)
        """
        pass

    def __repr__(self):
        pass
