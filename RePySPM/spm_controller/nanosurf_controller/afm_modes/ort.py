import nanosurf


class OffResonanceMode:
    """Off-resonance tapping (ORT) mode wrapper for Nanosurf SPM.

    In Nanosurf, this mode is called WaveMode.
    """

    def __init__(self, app):
        self._app = app

    def activate(self):
        self._app.OperatingMode.OperatingMode = nanosurf.SPM.OperatingMode.WaveMode
        return 0

    def get_exc_amplitude(self):
        return self._app.OperatingMode.VibratingAmpl

    def set_exc_amplitude(self, value):
        self._app.OperatingMode.VibratingAmpl = value
        return 0
