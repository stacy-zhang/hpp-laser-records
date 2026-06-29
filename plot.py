# x-axis: wavelength (µm)
# y-axis: peak power (Watts, log scale)
# if needed, estimate peak power as pulse energy/pulse duration
# colors corresponding to NIR (0.7-1.0 µm), SWIR (1.0-3.0 µm), MWIR (3.0-8.0 µm), and LWIR (8.0-12.0 µm) bands
# useful extras: color by laser tech or year, marker size by repetition rate, 
# hover labels or point labels with name, institution, and DOI

import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

df = pd.read_csv("laser_systems.csv")

wavelength = df["wavelength(µm)"]
power = df["peak_power(W)"]

sizes = 30 + 70 * np.log10(df["repetition_rate(Hz)"] + 1)

plt.scatter(wavelength, power, s=sizes)
plt.title("Peak Power vs. Wavelength of High-Power Laser Systems")
plt.xlabel("Wavelength (µm)")
plt.ylabel("Peak power (W)")

# Log-scale y-axis with readable per-decade labels: 1 MW, 10, 100, 1 GW, 10, 100, ...
SI_PREFIXES = {3: "k", 6: "M", 9: "G", 12: "T", 15: "P", 18: "E"}


def format_power(value, _pos=None):
	exponent = round(math.log10(value))
	mantissa_exp = exponent % 3
	prefix_exp = exponent - mantissa_exp
	mantissa = 10 ** mantissa_exp
	if mantissa_exp == 0:
		return f"{mantissa:g} {SI_PREFIXES.get(prefix_exp, '')}W".strip()
	return f"{mantissa:g}"


ax = plt.gca()
ax.set_yscale("log")
ax.yaxis.set_major_locator(mticker.LogLocator(base=10))
ax.yaxis.set_major_formatter(mticker.FuncFormatter(format_power))
ax.yaxis.set_minor_locator(mticker.NullLocator())

# Start the y-axis at the bottom of the smallest value's prefix group (e.g. 1 GW)
# so the user always sees the unit the bare "10"/"100" labels belong to.
positive_power = power[power > 0]
if not positive_power.empty:
	min_exponent = math.floor(math.log10(positive_power.min()))
	max_exponent = math.ceil(math.log10(positive_power.max()))
	lower_exponent = min_exponent - (min_exponent % 3)
	ax.set_ylim(10 ** lower_exponent, 10 ** max_exponent)

ax.set_xlim(left=0)

plt.show()