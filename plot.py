# x-axis: wavelength (µm)
# y-axis: peak power (Watts, log scale)
# if needed, estimate peak power as pulse energy/pulse duration
# colors corresponding to NIR (0.7-1.0 µm), SWIR (1.0-3.0 µm), MWIR (3.0-8.0 µm), and LWIR (8.0-12.0 µm) bands
# useful extras: color by laser tech or year, marker size by repetition rate, 
# hover labels or point labels with name, institution, and DOI

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("laser_systems.csv")

POWER_UNITS = {
	"GW": 1e9,
	"TW": 1e12,
	"PW": 1e15,
}

wavelength = df["wavelength"]
power = df["peak_power"]

plt.scatter(wavelength, power)
plt.title("Peak Power vs. Wavelength of High-Power Laser Systems")
plt.xlabel("Wavelength (µm)")
plt.ylabel("Peak power (W)")
plt.show()