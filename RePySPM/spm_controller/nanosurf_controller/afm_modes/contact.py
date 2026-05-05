import nanosurf


class ContactMode:
    """Contact mode wrapper for Nanosurf SPM."""

    def __init__(self, app):
        self._app = app

    def activate(self):
        self._app.OperatingMode.OperatingMode = nanosurf.SPM.OperatingMode.StaticAFM
        return 0
