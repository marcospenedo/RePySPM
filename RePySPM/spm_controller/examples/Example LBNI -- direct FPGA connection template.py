import nifpga
import os

# Path to the project
project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"

# Path to the bitfile
bitfile_name = r"lbniAFMController_usbRIO_controllerFPGA_testboard.lvbitx"

bitfile_folder = os.path.join(project_path, "FPGA Bitfiles")  # Automatically add "pythonAPI\"
bitfile_path = os.path.join(bitfile_folder, "lbniAFMController_usbRIO_controllerFPGA_testboard.lvbitx")

# Specify your FPGA resource name (adjust based on your hardware)
resource_name = "RIO0"  # For example, use the correct resource from NI MAX

fpga_session = nifpga.Session(bitfile_path, resource_name)

value_r = fpga_session.registers['aio.o.invertInputs'].read()
print(value_r)

value_w = [False, False, True, False, False, False, False, False]
fpga_session.registers['aio.o.invertInputs'].write(value_w)
value_r = fpga_session.registers['aio.o.invertInputs'].read()
print(value_r)
