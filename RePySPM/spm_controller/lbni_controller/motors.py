class Motors:
    """
    A class to control the motors of the stage, lasers, and photodiode in a scanning arm system.
    
    This class provides methods to move and control different components of the system, 
    including the stage, readout laser, excitation laser, and photodiode, in the X, Y, and Z directions.
    The movement can be defined by steps, time, or distance.
    
    Methods:
        moveX_stage_steps: Move the stage by a specified number of steps in the X direction.
        moveX_stage_time: Move the stage for a specified duration in the X direction.
        moveX_stage_distance: Move the stage by a specific distance in the X direction.
        moveY_stage_steps: Move the stage by a specified number of steps in the Y direction.
        moveY_stage_time: Move the stage for a specified duration in the Y direction.
        moveY_stage_distance: Move the stage by a specific distance in the Y direction.
        moveZ_stage_steps: Move the stage by a specified number of steps in the Z direction.
        moveZ_stage_time: Move the stage for a specified duration in the Z direction.
        moveZ_stage_distance: Move the stage by a specific distance in the Z direction.
        center_stage: Move the stage to its center position.
        
        moveX_readout_laser_steps: Move the readout laser by a specified number of steps in the X direction.
        moveX_readout_laser_time: Move the readout laser for a specified duration in the X direction.
        moveX_readout_laser_distance: Move the readout laser by a specific distance in the X direction.
        moveY_readout_laser_steps: Move the readout laser by a specified number of steps in the Y direction.
        moveY_readout_laser_time: Move the readout laser for a specified duration in the Y direction.
        moveY_readout_laser_distance: Move the readout laser by a specific distance in the Y direction.
        moveZ_readout_laser_steps: Move the readout laser by a specified number of steps in the Z direction.
        moveZ_readout_laser_time: Move the readout laser for a specified duration in the Z direction.
        moveZ_readout_laser_distance: Move the readout laser by a specific distance in the Z direction.
        center_readout_laser: Center the readout laser.
        maximize_readout_laser: Maximize the signal from the readout laser.
        
        moveX_excitation_laser_steps: Move the excitation laser by a specified number of steps in the X direction.
        moveX_excitation_laser_time: Move the excitation laser for a specified duration in the X direction.
        moveX_excitation_laser_distance: Move the excitation laser by a specific distance in the X direction.
        moveY_excitation_laser_steps: Move the excitation laser by a specified number of steps in the Y direction.
        moveY_excitation_laser_time: Move the excitation laser for a specified duration in the Y direction.
        moveY_excitation_laser_distance: Move the excitation laser by a specific distance in the Y direction.
        moveZ_excitation_laser_steps: Move the excitation laser by a specified number of steps in the Z direction.
        moveZ_excitation_laser_time: Move the excitation laser for a specified duration in the Z direction.
        moveZ_excitation_laser_distance: Move the excitation laser by a specific distance in the Z direction.
        center_excitation_laser: Center the excitation laser.
        maximize_excitation_laser: Maximize the signal from the excitation laser.
        
        moveX_photodiode_steps: Move the photodiode by a specified number of steps in the X direction.
        moveX_photodiode_time: Move the photodiode for a specified duration in the X direction.
        moveX_photodiode_distance: Move the photodiode by a specific distance in the X direction.
        moveY_photodiode_steps: Move the photodiode by a specified number of steps in the Y direction.
        moveY_photodiode_time: Move the photodiode for a specified duration in the Y direction.
        moveY_photodiode_distance: Move the photodiode by a specific distance in the Y direction.
        center_photodiode: Center the photodiode.
        autoalign_photodiode: Automatically align the photodiode for optimal signal.
    """
    
    def moveX_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the X direction."""
        pass

    def moveX_stage_time(self, duration):
        """Move the stage for a specified duration in the X direction."""
        pass

    def moveX_stage_distance(self, distance):
        """Move the stage by a specific distance in the X direction."""
        pass

    def moveY_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the Y direction."""
        pass

    def moveY_stage_time(self, duration):
        """Move the stage for a specified duration in the Y direction."""
        pass

    def moveY_stage_distance(self, distance):
        """Move the stage by a specific distance in the Y direction."""
        pass

    def moveZ_stage_steps(self, Nsteps):
        """Move the stage by a specified number of steps in the Z direction."""
        pass

    def moveZ_stage_time(self, duration):
        """Move the stage for a specified duration in the Z direction."""
        pass

    def moveZ_stage_distance(self, distance):
        """Move the stage by a specific distance in the Z direction."""
        pass

    def center_stage(self):
        """Move the stage to its center position."""
        pass

    def moveX_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the X direction."""
        pass

    def moveX_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the X direction."""
        pass

    def moveX_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the X direction."""
        pass

    def moveY_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the Y direction."""
        pass

    def moveY_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the Y direction."""
        pass

    def moveY_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the Y direction."""
        pass

    def moveZ_readout_laser_steps(self, Nsteps):
        """Move the readout laser by a specified number of steps in the Z direction."""
        pass

    def moveZ_readout_laser_time(self, duration):
        """Move the readout laser for a specified duration in the Z direction."""
        pass

    def moveZ_readout_laser_distance(self, distance):
        """Move the readout laser by a specific distance in the Z direction."""
        pass

    def center_readout_laser(self):
        """Center the readout laser."""
        pass

    def maximize_readout_laser(self):
        """Maximize the signal from the readout laser."""
        pass

    def moveX_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the X direction."""
        pass

    def moveX_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the X direction."""
        pass

    def moveX_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the X direction."""
        pass

    def moveY_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the Y direction."""
        pass

    def moveY_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the Y direction."""
        pass

    def moveY_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the Y direction."""
        pass

    def moveZ_excitation_laser_steps(self, Nsteps):
        """Move the excitation laser by a specified number of steps in the Z direction."""
        pass

    def moveZ_excitation_laser_time(self, duration):
        """Move the excitation laser for a specified duration in the Z direction."""
        pass

    def moveZ_excitation_laser_distance(self, distance):
        """Move the excitation laser by a specific distance in the Z direction."""
        pass

    def center_excitation_laser(self):
        """Center the excitation laser."""
        pass

    def maximize_excitation_laser(self):
        """Maximize the signal from the excitation laser."""
        pass

    def moveX_photodiode_steps(self, Nsteps):
        """Move the photodiode by a specified number of steps in the X direction."""
        pass

    def moveX_photodiode_time(self, duration):
        """Move the photodiode for a specified duration in the X direction."""
        pass

    def moveX_photodiode_distance(self, distance):
        """Move the photodiode by a specific distance in the X direction."""
        pass

    def moveY_photodiode_steps(self, Nsteps):
        """Move the photodiode by a specified number of steps in the Y direction."""
        pass

    def moveY_photodiode_time(self, duration):
        """Move the photodiode for a specified duration in the Y direction."""
        pass

    def moveY_photodiode_distance(self, distance):
        """Move the photodiode by a specific distance in the Y direction."""
        pass

    def center_photodiode(self):
        """Center the photodiode."""
        pass

    def autoalign_photodiode(self):
        """Automatically align the photodiode for optimal signal."""
        pass

