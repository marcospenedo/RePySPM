# Example usage:
afm = AFMController(connection_params="COM3")
afm.connect()
afm.set_scan_parameters(scan_size=50, scan_speed=2, resolution=512)
afm.set_z_control_pid(p_gain=0.1, i_gain=0.01, d_gain=0.001)

# Setting AM Mode
am_mode = AMMode(amplitude=10, frequency=150)
afm.set_afm_mode(am_mode)

# Setting FM Mode
fm_mode = FMMode(frequency=150, phase=90)
afm.set_afm_mode(fm_mode)

# Setting Contact Mode
contact_mode = ContactMode(force_setpoint=5)
afm.set_afm_mode(contact_mode)

# Setting Off Resonance Mode
off_resonance_mode = OffResonanceMode(off_resonance_value=100)
afm.set_afm_mode(off_resonance_mode)

afm.start_scan()
latest_image = afm.get_latest_image()
print(latest_image)
afm.disconnect()

# obj2 = MyClass.from_single_arg(10)
