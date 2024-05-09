import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as plticker
import numpy as np
from scipy.stats import norm


AUT = ["A", "AOpt", "A'", "AOpt'", "I", "IOpt" , "I'", "IOpt'", "S", "SOpt", "S'", "SOpt'", "T", "TOpt", "Gi", "X", "R", "ROpt", "E", "Gr", "P"]
x = AUT
m33 = [0.02080, 0.009508658, 0.01509756, 0.00630, 0.133581178, 0.032596533, 0.111168077, 0.024077083, 0.01546, 0.005162446, 0.021366698, 0.00811, 0.03883, 0.02545, 0.338608031, 0.062993513, 0.490128328, 0.046576747, 5.785723766, 5.802136501, 3.79344]
m4 = [0.062713915, 0.052988992, 0.045303212, 0.035042905, 0.273938018, 0.119754776, 0.235006402, 0.086472794, 0.033105055, 0.022342038, 0.051314609, 0.034233196, 0.077532967, 0.049639545, 0.846136083, 0.125425177, 1.095592449, 0.188478137, 10.67586803, 8.904929638, 8.064251661]
m7 = [0.02566, 0.01431, 0.01969, 0.00932, 0.18442, 0.04761, 0.15857, 0.03518, 0.02970, 0.00631, 0.04108, 0.00942, 0.05073, 0.03347, 0.49483, 0.09385, 0.97306, 0.05487, 8.06903, 6.56086, 8.72422]

m7 = np.array(m7)
m4 = np.array(m4) 
m33 = np.array(m33)

print("M7 Average:", np.mean(m7))
print("M4 Average:", np.mean(m4))
print("M33 Average :", np.mean(m33))

colors = ["#000080", "skyblue", "#1e90ff", "#87cefa"]
linestyles = ['-', '--', ':']

bar_width = 0.2  # Width of each bar
bar_space = 0  # Space between each group of bars
x_axis = np.arange(len(AUT))
plt.figure(figsize=(8,4.5))
plt.subplot(2,1,1)
plt.plot(x, m7, color=colors[0], marker='x', label='M7')
plt.plot(x, m4, color='#783114', marker='o',label='M4')
plt.plot(x, m33, color=colors[2], marker='x',label='M33')
# plt.bar(x_axis - bar_width - bar_space, m7, width=bar_width, color=colors[0], label='M7')
# plt.bar(x_axis, m4, width=bar_width, color=colors[1], label='M4')
# plt.bar(x_axis + bar_width + bar_space, m33, width=bar_width, color=colors[2], label='M33')
plt.xlim([x_axis[0]-bar_width-0.1, x_axis[20]+bar_width+0.1])
plt.legend()
plt.xticks([])
plt.xlabel('')
plt.grid(axis='y', alpha=0.4)
plt.ylim([3,12])
# plt.ylabel('runtime (s)', fontsize=11)


plt.subplot(2,1,2)
# plt.bar(x_axis - bar_width - bar_space, m7, width=bar_width, color=colors[0], label='M7')
# plt.bar(x_axis, m4, width=bar_width, color=colors[1], label='M4')
# plt.bar(x_axis + bar_width + bar_space, m33, width=bar_width, color=colors[2], label='M33')
plt.plot(x, m7, color=colors[0], marker='x', label='M7')
plt.plot(x, m4, color='#783114', marker='o',label='M4')
plt.plot(x, m33, color=colors[2], marker='x',label='M33')
plt.xlim([x_axis[0]-bar_width-0.1, x_axis[20]+bar_width+0.1])
plt.ylim([0,1.2])
plt.xticks(x_axis, AUT )
plt.xlabel('Lightweight Cryptography Algorithm')
# plt.ylabel('Average ', fontsize=11,labelpad=10)
plt.text(-1.75, 1.25, 'Runtime (s)', fontsize=11, rotation=90, verticalalignment='center')
plt.subplots_adjust(left = 0.07, right = 0.98, top=0.96, wspace=0.9, bottom=0.11, hspace=0.04)
plt.xlim([x_axis[0]-bar_width-0.1, x_axis[20]+bar_width+0.1])
# plt.xticks([])
plt.grid(axis='y', alpha=0.4)
# plt.text(-0.45, 0.07, "a)", fontsize=11, weight='bold',  va='bottom', ha='right')
# plt.legend(loc='upper left')
plt.show()
