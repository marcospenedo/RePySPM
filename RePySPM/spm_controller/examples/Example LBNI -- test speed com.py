import sys
import os

import timeit

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController
from lbni_controller import AFMModes

# Example function to test
def my_function(afm_r):
    # Replace this with your function code
    afm_r.z_control.set_setpoint(0.25)
    afm_r.afmmode.am.set_exc_amplitude(0.2)
    
def my_function2(afm_r):
    # Replace this with your function code
    afm_r.utils.set_timeout(1)

def main():
    # Path to the project
    project_path = r"D:\Users\Marcos\OpenSPM\OpenSPM-source"
    
    afm = AFMController(project_path)
    
    # Set the scan parameters for the exploration
    # Please skip this step if you prefer setting the initial parameters manually 
    print("\n--- Setting AM Mode ---")

    afm.afmmode.set_mode(AFMModes.AM)
    
    print("\n--- Setting SetPoint ---")
    
    afm.z_control.set_setpoint(0.25)
    
    print("\n--- Setting Amplitude ---")
    
    afm.afmmode.am.set_exc_amplitude(0.2)
    
    print("\n--- Setting Timeout ---")
    
    afm.utils.set_timeout(1)
    
    # Measure execution time
    execution_time = timeit.timeit(lambda: my_function(afm), number=10) / 10  # Time per call

    # Calculate calls per second
    calls_per_second = 1 / execution_time if execution_time > 0 else float('inf')

    print(f"Average execution time per call: {execution_time:.10f} seconds")
    print(f"Estimated calls per second: {calls_per_second:.2f}")
    
    # Measure execution time
    execution_time = timeit.timeit(lambda: my_function2(afm), number=10) / 10  # Time per call

    # Calculate calls per second
    calls_per_second = 1 / execution_time if execution_time > 0 else float('inf')

    print(f"Average execution time per call: {execution_time:.10f} seconds")
    print(f"Estimated calls per second: {calls_per_second:.2f}")
    
    afm.utils.set_timeout(20)
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()
    
    