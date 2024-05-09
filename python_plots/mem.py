import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as plticker
import numpy as np
from scipy.stats import norm

AUT = ["A", "AOpt", "A'", "AOpt'", "I", "IOpt" , "I'", "IOpt'", "S", "SOpt", "S'", "SOpt'", "T", "TOpt", "Gi", "X", "R", "ROpt", "E", "Gr", "P"]

x = AUT
flash_m7 = [12434.66667, 6610.666667, 16146.66667, 7464, 2576, 13365.33333, 2576, 15562.66667, 4352, 22541.33333, 4650.666667, 27010.66667, 1453.333333, 1277.333333, 3242.666667, 3386.666667, 5624, 10301.33333, 4096, 4548, 4540]
flashO3_m7 = [17560, 6616, 22680, 7448, 2952, 13520, 2952, 15760, 5992, 23952, 6520, 29824, 2128, 1376, 5984, 4504, 10536, 11288, 5560, 7436, 8364]
flashO2_m7 = [17648, 6576, 22960, 7408, 2584, 13224, 2584, 15464, 3704, 22432, 3960, 26432, 1120, 1264, 1968, 2992, 3712, 10032, 3656, 3556, 2820]
flashOs_m7 = [2096, 6640, 2800, 7536, 2192, 13352, 2192, 15464, 3360, 21240, 3472, 24776, 1112, 1192, 1776, 2664, 2624, 9584, 3072, 2652, 2436]
flash_m4 = [13117, 7861, 16813, 8707, 21517, 14640, 21517, 16880, 40256, 58443, 40467, 62856, 2336, 2152, 4483, 22304, 6832, 12877, 39968, 6824, 40469]
flash_m33 = [13949.33333, 7990.666667,17733.33333, 8824,   20597.33333, 16832, 20597.33333, 14662.66667, 39441.33333, 57878.66667, 39668, 62292, 1886.666667, 2348, 4664, 21360, 6944, 11566.66667, 35873.33333, 6686.666667, 39632]

ram_m7 = [0, 0, 0, 0, 0, 96, 0, 96, 0, 0, 0, 0, 24, 0, 0, 32, 8, 0, 1024, 0, 0]
ram_m4 = [0, 0, 0, 0, 1072, 96, 1072, 96, 1072, 1080, 1072, 1072, 24, 0, 0, 1104, 8, 0, 2104, 0, 1104]
ram_m33 = [0, 0, 0, 0, 2104, 0, 0, 1080, 1080, 96, 96, 1112, 0, 8, 1080, 1080, 1080, 1080, 24, 0, 1112]

flash_m7 = np.array(flash_m7)/1e3
flash_m4 = np.array(flash_m4) /1e3
flash_m33 = np.array(flash_m33)/1e3

ram_m7 = np.array(ram_m7)/1e3
ram_m4 = np.array(ram_m4) /1e3
ram_m33 = np.array(ram_m33)/1e3
# Create a figure and plot

print("Flash: ")
print("M7 Average:", np.mean(flash_m7))
print("M4 Average:", np.mean(flash_m4))
print("M33 Average :", np.mean(flash_m33))

print("RAM:")
print("M7 Average:", np.mean(ram_m7))
print("M4 Average:", np.mean(ram_m4))
print("M33 Average :", np.mean(ram_m33))

colors = ["#000080", "skyblue", "#1e90ff", "#87cefa"]
linestyles = ['-', '--', ':']
flash = True
plt.figure(figsize=(8,4.5))
plt.subplot(2,1,1)

plt.plot(x, ram_m7, color=colors[0], marker='x', label='M7')
plt.plot(x, ram_m4, color='#783114', marker='o',label='M4')
plt.plot(x, ram_m33, color=colors[2], marker='x',label='M33')
plt.ylabel('RAM footprint (KB)', fontsize=11)
plt.xlabel('')
plt.xticks([])
plt.grid(axis='y', alpha=0.4)
plt.text(-0.45, 0.07, "a)", fontsize=11, weight='bold',  va='bottom', ha='right')
plt.legend(loc='upper left')

plt.subplot(2,1,2)
# Plot the first dataset on the primary y-axis
plt.plot(x, flash_m7, color=colors[0], marker='x', label='M7')
plt.plot(x, flash_m4, color='#783114', marker='o',label='M4')
plt.plot(x, flash_m33, color=colors[2], marker='x',label='M33')
plt.ylabel('Average Flash footprint (KB)', fontsize=11)
plt.xlabel('Lightweight Cryptography Algorithm', fontsize=11)
plt.grid(axis='y', alpha=0.4)
plt.subplots_adjust(left = 0.07, right = 0.988, top=1.0, wspace=0.9, bottom=0.1, hspace=0.04)
plt.text(-0.45, 0.07, "b)", fontsize=11, weight='bold', va='bottom', ha='right')

plt.legend(loc='upper left')
plt.show()

# # Create a secondary y-axis and plot the second dataset
# ax2 = ax1.twinx()
# ax2.plot(x, ram_m7, color=colors[0], linestyle='--', marker='o', label='RAM')
# ax2.set_ylabel('RAM', color='red')

# # Add legends
# lines, labels = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(lines + lines2, labels + labels2, loc='upper right')

# # Add title and labels
# ax1.set_xlabel('x')
# ax1.set_title('Dual Y-axis Plot')

