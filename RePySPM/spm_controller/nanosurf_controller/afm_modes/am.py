import nanosurf


class AMMode:
    """AM (Dynamic AFM / tapping) mode wrapper for Nanosurf SPM."""

    def __init__(self, app):
        self._app = app

    def activate(self):
        self._app.OperatingMode.OperatingMode = nanosurf.SPM.OperatingMode.DynamicAFM
        return 0

    def get_exc_amplitude(self):
        return self._app.OperatingMode.VibratingAmpl

    def set_exc_amplitude(self, value):
        self._app.OperatingMode.VibratingAmpl = value
        return 0
