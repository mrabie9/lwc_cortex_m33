import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as plticker
import numpy as np


# fig, ax = plt.subplots(1,1)

# labels = ["S", "T", "A'", "A", "R", "I", "I'", "S'"]
# Speedup = [4.00, 1.457002398, 1.173512822, 1.113769354, 6.464059519, 2.566899485, 2.82531296, 3.642170873]
# Size_increase = [6.32, 1.071942446, 2.645714286, 3.13740458, 3.652439024, 6.032846715, 7.054744526, 7.1359447]
# Energy_efficiency = [3.857142857, 1.404298874, 1.227436823, 1.159250585, 5.840457556, 2.624551328, 2.884765625, 3.5]


# ax.plot(labels, Speedup, label='Speedup')
# ax.plot(labels, Size_increase, label='Size increase')
# ax.plot(labels, Energy_efficiency, label='Energy efficiency improvement')
# ax.yaxis.set_major_locator(plticker.MultipleLocator(0.5))
# plt.grid()
# plt.ylabel('Multiplier', fontsize=11)
# plt.legend(loc='lower right')
# plt.xlabel('Lightweight cryptography algorithm', fontsize=11)
# plt.show()

opt_data = {
    'labels' : ["AOpt", "AOpt'", "IOpt", "IOpt'", "SOpt", "SOpt'", "TOpt", "ROpt"],
    'M7' : {
        'Size_increase' : [0.531631997, 0.462262593, 5.188405797, 6.041407867, 5.179534314, 5.807912844, 0.878899083, 1.831673779],
        'Speedup' : [1.793172002, 2.112083204, 3.87357876, 4.507008862, 4.705884341, 4.360635242, 1.515608541, 17.73323292],
        'Energy_efficiency' : [1.828660436, 2.142344498, 3.948934177, 4.589410273, 4.584745763, 4.176339286, 1.510307644, 16.77277238]
    }, 

    'M4' : {
        'Size_increase' : [0.599308803, 0.517842982, 0.680381708, 0.784483827, 1.451775305, 1.553278418, 0.921232877, 1.884855582],
        'Speedup' : [1.183527232, 1.292792722, 2.287491371, 2.717691773, 1.481738384, 1.498972195, 1.56191936, 5.812835728],
        'Energy_efficiency' : [1.229226361, 1.344902386, 1.584141712, 1.875581395, 1.634868421, 1.618644068, 1.568940493, 6.232586069],
        },

    'M33' : {
        'Size_increase' : [0.572835022, 0.497593985, 0.817193164, 0.711872087, 1.467462222, 1.57033377, 1.244522968, 1.665706605],
        'Speedup' : [2.187926962, 2.396070456, 4.098017975, 4.617173794, 2.994667502, 2.633657463, 1.525718725, 10.52302618],
        'Energy_efficiency' : [2.416666667, 2.645833333, 4.432, 4.989189189, 3.285714286, 2.838235294, 1.545454545, 11.66666667],
    }
}

# ax.plot(labels, Speedup, label='Speedup')
# ax.plot(labels, Size_increase, label='Size increase')
# ax.plot(labels, Energy_efficiency, label='Energy efficiency improvement')
# ax.yaxis.set_major_locator(plticker.MultipleLocator(0.5))
# plt.grid()
# plt.ylabel('Multiplier', fontsize=11)
# plt.legend(loc='lower right')
# plt.xlabel('Lightweight cryptography algorithm', fontsize=11)
# plt.show()
# global labels
# fig, ax = plt.subplots(3,1)
# colors = ["blue", "Green", "Orange"]
colors = ["#000080", "#783114", "#1e90ff", "#87cefa"]
linestyles = ['-', '--', ':']
board_idx = 0
for board, data in opt_data.items():
    if board.lower() in 'labels':
        labels = data
    else:
        print(board, np.mean(data['Speedup']), np.mean(data['Energy_efficiency']),  np.mean(data['Size_increase']))
        # print(data)
        plt.plot(labels, data['Speedup'], label='Speedup - ' + board, color=colors[board_idx], linestyle=linestyles[0], marker='.', linewidth=1.5)
        plt.plot(labels, data['Energy_efficiency'], label='Energy efficiency - ' + board, color=colors[board_idx],  marker='.',linestyle=linestyles[1], linewidth=1.5)
        plt.plot(labels, data['Size_increase'], label='Size increase - ' + board, color=colors[board_idx],  marker='.',linestyle=linestyles[2], linewidth=1.5)

        # ylabels = plt.gca().get_yticklabels()
        # print(ylabels)
        # plt.set_title(board)
        # for i, label in enumerate(ylabels):
        #     if i % 2 == 0:
        #         label.set_visible(False)
        board_idx +=1

plt.yticks(np.arange(0, 19, 2))
plt.ylim((0,18))
plt.grid(axis='y', alpha=0.4)
# plt.yaxis.set_major_locator(plticker.MultipleLocator(0.5))
# plt.suptitle('Speedup, energy efficiency, and size of Armv7 optimised implementations', fontsize=12, fontweight='bold')
plt.subplots_adjust(left = 0.07, right = 0.98, top=1.0, wspace=0.9, hspace=0.1, bottom=0.16) 
# fig.text(0.06, 0.5, 'Multiplier', va='center', rotation='vertical', fontsize=12)
plt.ylabel('Multiplier', fontsize=12)
plt.legend(loc='upper left', prop={'size': 8})
plt.xlabel('Lightweight cryptography algorithm', fontsize=11)
plt.show()
        
# fig, ax = plt.subplots(3,1)
# subplot_idx = 1
# for board, data in opt_data.items():
#     if board.lower() in 'labels':
#         labels = data
#     else:
#         print(board)
#         # print(data)
#         ax[subplot_idx-1].plot(labels, data['Speedup'], label='Speedup')
#         ax[subplot_idx-1].plot(labels, data['Energy_efficiency'], label='Energy efficiency')
#         ax[subplot_idx-1].plot(labels, data['Size_increase'], label='Size increase')

#         ax[subplot_idx-1].yaxis.set_major_locator(plticker.MultipleLocator(1))
#         # ylabels = plt.gca().get_yticklabels()
#         # print(ylabels)
#         ax[subplot_idx-1].set_title(board)
#         ax[subplot_idx-1].grid(axis='y', alpha=0.4)
#         # for i, label in enumerate(ylabels):
#         #     if i % 2 == 0:
#         #         label.set_visible(False)
#         subplot_idx +=1

# plt.suptitle('Comparison of reference and available optimised implementations', fontsize=12, fontweight='bold')
# plt.subplots_adjust(left = 0.07, right = 0.98, top=0.9, wspace=0.9, hspace=0.1, bottom=0.1) 
# fig.text(0.06, 0.5, 'Multiplier', va='center', rotation='vertical', fontsize=12)
# # plt.ylabel('', fontsize=11)
# plt.legend(loc='lower right')
# plt.xlabel('Lightweight cryptography algorithm', fontsize=11)
# plt.show()
        