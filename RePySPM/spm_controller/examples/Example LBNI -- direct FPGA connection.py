import nifpga
import os

import timeit
from functools import partial


# Example function to test
def my_function(fpga_session):
    # Replace this with your function code
    params = fpga_session.registers['fb.p.params'].read()
    params['setPoint'] = 0.01
    # Write the updated cluster back to the FPGA
    fpga_session.registers['fb.p.params'].write(params)

# Example function to test
def my_function2(fpga_session):
    # Replace this with your function code
    # Write the updated cluster back to the FPGA
    value = True
    fpga_session.registers['fb.p.enable'].write(value)
 
# Example function to test
def my_function3(fpga_session):
    # Replace this with your function code
    # Write the updated cluster back to the FPGA
    value = 0
    fpga_session.registers['fb.p.params.e.upper_limit'].write(value)
    
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

value_r = fpga_session.registers['fb.p.params'].read()
print(value_r)

set_point = value_r['setPoint']
print(set_point)

# Measure execution time cluster
execution_time = timeit.timeit(lambda: my_function(fpga_session), number=1000) / 1000  # Time per call

# Calculate calls per second
calls_per_second = 1 / execution_time if execution_time > 0 else float('inf')

print(f"Average execution time per cluster call: {execution_time:.10f} seconds")
print(f"Estimated calls per second: {calls_per_second:.2f}")

# Measure execution time boolean
execution_time = timeit.timeit(lambda: my_function2(fpga_session), number=1000) / 1000  # Time per call

# Calculate calls per second
calls_per_second = 1 / execution_time if execution_time > 0 else float('inf')

print(f"Average execution time per boolean call: {execution_time:.10f} seconds")
print(f"Estimated calls per second: {calls_per_second:.2f}")

# Measure execution time integer
execution_time = timeit.timeit(lambda: my_function(fpga_session), number=1000) / 1000  # Time per call

# Calculate calls per second
calls_per_second = 1 / execution_time if execution_time > 0 else float('inf')

print(f"Average execution time per integer call: {execution_time:.10f} seconds")
print(f"Estimated calls per second: {calls_per_second:.2f}")




