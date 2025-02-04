from afm_controller import AFMController

# Step 1: Initialize the AFM Controller
afm = AFMController()

# Step 2: Connect to the AFM system
afm.connect()

# Step 3: Move the motors (stage, lasers, photodiode)
print("\n--- Moving Stage ---")
afm.motors.move_x_stage(100)   # Move stage 100 steps in X
afm.motors.move_y_stage(50)    # Move stage 50 steps in Y
afm.motors.move_z_stage(-20)   # Move stage -20 steps in Z
afm.motors.center_stage()      # Center the stage

print("\n--- Moving Readout Laser ---")
afm.motors.move_x_readout_laser_steps(10)
afm.motors.center_readout_laser()

print("\n--- Moving Excitation Laser ---")
afm.motors.move_x_excitation_laser_steps(15)
afm.motors.center_excitation_laser()

print("\n--- Moving Photodiode ---")
afm.motors.moveX_photodiode_steps(5)
afm.motors.center_photodiode()

# Step 4: Set scan parameters
print("\n--- Setting Scan Parameters ---")
afm.scan_parameters.set_scan_parameters(
    width=10e-6,  # 10 µm
    height=10e-6, # 10 µm
    rotation=0,
    speed=1e-6    # 1 µm/s
)
print("Scan parameters set.")

# Step 5: Start scanning
print("\n--- Starting Scan ---")
afm.scan_control.scan_up()
print("Scanning upwards...")

# Step 6: Pause scanning
afm.scan_control.scan_pause()
print("Scanning paused.")

# Step 7: Resume scanning
afm.scan_control.scan_resume()
print("Scanning resumed.")

# Step 8: Stop scanning
afm.scan_control.scan_stop()
print("Scanning stopped.")

# Step 9: Get signals
print("\n--- Reading Signals ---")
vertical_deflection = afm.signals.get_vertical_deflection()
amplitude = afm.signals.get_amplitude()
phase = afm.signals.get_phase()

print(f"Vertical Deflection: {vertical_deflection}")
print(f"Amplitude: {amplitude}")
print(f"Phase: {phase}")

# Step 10: Using AFM Modes
print("\n--- Switching to AM Mode ---")
afm.am_mode.set_excitation_amplitude(2.5)
afm.am_mode.set_excitation_frequency(150000)  # 150 kHz
print("AM Mode parameters set.")

print("\n--- Switching to FM Mode ---")
afm.fm_mode.set_pll_gain(p_gain=1.0, i_gain=0.1, d_gain=0.01)
print("FM Mode PLL parameters set.")

print("\n--- Switching to Contact Mode ---")
afm.contact_mode.set_relative_setpoint(True)
print("Contact Mode set to relative setpoint mode.")

# Step 11: Image Acquisition
print("\n--- Acquiring Image ---")
channels = afm.image.get_channels_names()
print("Available channels:", channels)

topography = afm.image.get_channel("Topography")
print("Topography data acquired.")

# Step 12: Control Lasers
print("\n--- Controlling Lasers ---")
afm.lasers.set_readout_mW(1.0)  # Set readout laser to 1mW
afm.lasers.set_excitation_mW(2.0)  # Set excitation laser to 2mW
afm.lasers.set_readout_ON(True)  # Turn on readout laser
afm.lasers.set_excitation_ON(True)  # Turn on excitation laser
print("Lasers configured.")

# Step 13: Controlling Z Position
print("\n--- Controlling Z Position ---")
afm.z_control.set_p_gain(0.5)
afm.z_control.set_i_gain(0.1)
afm.z_control.set_d_gain(0.01)
afm.z_control.set_setpoint(0.002)  # Setpoint at 2mV
print("Z PID parameters configured.")

# Step 14: Disconnecting
print("\n--- Disconnecting from AFM System ---")
afm.disconnect()
print("AFM system disconnected.")
