from .commands import OHCcommands

class Utils:
    """
    A class containing other usuful functions to control the LBNI OHC.

    Methods:
        
    """
    
    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController
        
    def set_wave_N_poits(self, value):
               
        command = f"{OHCcommands.w_wav}scanWaveFormCtl:slowWavePts:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_wave_N_poits(self):
        
        control = "scanWaveFormCtl"
        command = f"{OHCcommands.r_wav}{control}"
        
        return self.controller.read_control(command, control)[0]

    def set_hyst_corr_X_path(self, value):
               
        command = f"{OHCcommands.w_wav}Hysteresis correction X:{value}"
            
        self.controller.write_control(command)
        
        return 0

    def get_hyst_corr_X_path(self):
        
        control = "Hysteresis correction X"
        command = f"{OHCcommands.r_sca}{control}"
        
        return self.controller.read_control(command, control)
    
    def __repr__(self):
        pass
