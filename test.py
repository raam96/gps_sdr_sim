import hackrf
import numpy as np

# Parameters
center_frequency = 1575.42e6  # GPS L1 frequency in Hz
sample_rate = 2.048e6  # Sample rate in Hz
txvga_gain = 20  # TX VGA gain, adjust as needed
bin_file = "gpssim.bin"  # Replace with your GPS signal binary file

# Initialize HackRF
hackrf_device = hackrf.HackRF()

# Open HackRF device and set parameters
hackrf_device.setup()
hackrf_device.set_freq(center_frequency)
hackrf_device.set_sample_rate(sample_rate)
hackrf_device.set_txvga_gain(txvga_gain)

# Read the GPS signal from the binary file
with open(bin_file, "rb") as file:
    gps_signal = np.fromfile(file, dtype=np.complex64)

# Transmit the GPS signal
print("Transmitting GPS signal...")
hackrf_device.txvrt(gps_signal)

# Close HackRF device
hackrf_device.close()

print("GPS signal transmission complete.")
