import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as plticker
import numpy as np

colours = ["#000080", "#1e90ff", "#b0c4de", "#87cefa"]
# : \[.*
meta_data = {
    'widths' : [0.8, 0.6, 0.35],
    'colours' : ["#000080", "#1e90ff", "#87cefa", "#b0c4de"],
    'M7' : {
        'Runtime' : {
            'Group A' : {
                'Labels' :  ["Sopt", "AOpt'", "SOpt'", "A'", "AOpt", "A", "S", "S'"],
                '-Os' : [0.006595685, 0.00946038, 0.0095545, 0.030064648, 0.014453283, 0.037541041, 0.037278291, 0.051797912],
                '-O2' : [0.006309551, 0.009258482, 0.009346204, 0.018148597, 0.014209139, 0.023606185, 0.027713625, 0.037390403],
                '-O3' : [0.006026296, 0.009245393, 0.009358662, 0.010849588, 0.014263148, 0.015825704, 0.024097686, 0.034040472]
            },

            'Group B' : {
                'Labels' :  ["IOpt'", "TOpt", "X", "T", "IOpt", "ROpt", "I'", "I"],
                '-Os' : [0.035690226, 0.030173112, 0.121495686, 0.050355889, 0.048245458, 0.05499793, 0.208716147, 0.241132148],
                '-O2' : [0.035407392, 0.035252875, 0.121851992, 0.057863094, 0.047830397, 0.053588709, 0.169662215, 0.192121737],
                '-O3' : [0.034453772, 0.03498337, 0.038196612, 0.043962296, 0.046757068, 0.056029815, 0.097342689, 0.120020695]

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "E", "P", "Gr"],
                '-Os' : [0.560316175, 1.551475465, 11.45726681, 10.29466534, 7.245157957],
                '-O2' : [0.688881427, 1.021305859, 8.08711338, 10.72446299, 6.425505877],
                '-O3' : [0.235283487, 0.346400604, 4.66270113, 5.153528929, 6.011909485],
            },
        },

        'Energy' : {
            'Group A' : {
                'Labels' :  ["Sopt", "AOpt'", "SOpt'", "A'", "AOpt", "A", "S", "S'"],
                '-Os' : [0.00204, 0.0028, 0.00303, 0.00893, 0.0043, 0.01122, 0.01132, 0.01557],
                '-O2' : [0.00197, 0.00279, 0.00297, 0.00558, 0.00427, 0.00731, 0.00844, 0.01149],
                '-O3' : [0.00189, 0.00277, 0.00296, 0.0034, 0.00427, 0.00495, 0.00729,  0.01036]

            },

            'Group B' : {
                'Labels' :  ["IOpt'", "TOpt", "X", "T", "IOpt", "ROpt", "I'", "I"],
                '-Os' : [0.0107, 0.00977, 0.03616, 0.0162, 0.01443, 0.01661, 0.06374, 0.07356],
                '-O2' : [0.0106, 0.0109, 0.03754, 0.0177, 0.01433, 0.01684, 0.05147, 0.05846],
                '-O3' : [0.01024, 0.01086, 0.01169, 0.01372, 0.01393, 0.01694, 0.02954, 0.03656]

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "E", "P", "Gr"],
                '-Os' : [0.16839, 0.46214, 3.45335, 3.03387, 1.84576],
                '-O2' : [0.20311, 0.28603, 2.50422, 3.11213, 1.6547],
                '-O3' : [0.07115, 0.09701, 1.45594, 1.50832, 1.49913],
            },
        },
        'Memory' : {  
            'Group A' : {   
                # 'Labels' :  ["Sopt", "AOpt'", "SOpt'", "A'", "AOpt", "A", "S", "S'"], 
                # '-O2': [21240, 7536, 24776, 2800, 6640, 2096, 3360, 3472],
                # '-O3' :  [22432, 7408, 26432, 22960, 6576, 17648, 3704, 3960],
                # '-Os' : [23952, 7448, 29824, 22680, 6616, 17560, 5992, 6520]
                'Labels' :  ["AOpt'", "A'", "AOpt", "A", "S", "S'"], 
                '-O2': [7536, 2800, 6640, 2096, 3360, 3472], # Os
                '-O3' :  [7408,22960, 6576, 17648, 3704, 3960], # O2
                '-Os' : [7448, 22680, 6616, 17560, 5992, 6520] # O3
            },

            'Group B' : {
                'Labels' :  [ "TOpt", "X", "T", "I'", "I"],
                '-Os' : [1192, 2664, 1112, 2192, 2192],
                '-O2' : [1264, 2992, 1120, 2584, 2584],
                '-O3' : [1376, 4504, 2128, 2952, 2952]

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "E", "P", "Gr"],
                '-Os' : [1776, 2624, 3072, 2436, 2652],
                '-O2' : [1968, 3712, 3656, 2820, 3556],
                '-O3' : [5984, 10536, 5560, 8364, 7436],
            },
        },

        # 'RAM' : {  
        #     'Group A' : {   
        #         'Labels' :  ["AOpt'", "A'", "AOpt", "A", "S", "S'"], 
        #         '-Os': [7536, 2800, 6640, 2096, 3360, 3472], 
        #     },

        #     'Group B' : {
        #         'Labels' :  [ "TOpt", "X", "T", "I'", "I"],
        #         '-Os' : [1192, 2664, 1112, 2192, 2192],

        #     },

        #     'Group C' : {
        #         'Labels' :  ["Gi", "R", "E", "P", "Gr"],
        #         '-Os' : [1776, 2624, 3072, 2436, 2652],
        #     },
        # }
    },

    'M33' : {
        'Runtime' : {
            'Group A' : {
                'Labels' :  [ "Sopt", "AOpt'", "SOpt'", "AOpt", "A'", "S", "A", "S'"],
                '-Os' : [0.005218356, 0.006254156, 0.008091894, 0.009539919, 0.020134381, 0.016488638, 0.027040207, 0.022937831],
                '-O2' : [0.005235087, 0.006324406, 0.00810825, 0.009493231, 0.0144941, 0.015576619, 0.019589537, 0.021441231],
                '-O3' : [0.005033894, 0.006324338, 0.008138669, 0.009492825, 0.0106642, 0.014314169, 0.015783006, 0.019721031],
            },

            'Group B' : {
                'Labels' :  ["IOpt'", "TOpt", "X", "T", "IOpt", "ROpt", "I'", "I"],
                '-Os' : [0.024396537, 0.028156619, 0.0825582, 0.045285545, 0.032963412, 0.046564087, 0.142079338, 0.166409478],
                '-O2' : [0.023995006, 0.024100219, 0.07804849, 0.039238706, 0.032490706, 0.046497174, 0.114803817, 0.136479482],
                '-O3' : [0.023839706, 0.024099956, 0.02837385, 0.031974738, 0.032335481, 0.04666898, 0.076621074, 0.097854573],

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "P", "E", "Gr"],
                '-Os' : [0.403684407, 0.690934151, 4.721044779, 7.400717974, 6.190942764],
                '-O2' : [0.422478706, 0.56662342, 4.197080612, 6.042227983, 5.725517511],
                '-O3' : [0.189660981, 0.212827414, 2.462208033, 3.91422534, 5.489949226],
            },
        },

        'Energy' : {
            'Group A' : {
                'Labels' :  [ "Sopt", "AOpt'", "SOpt'", "AOpt", "A'", "S", "A", "S'"],
                '-Os' : [0.00014, 0.00016, 0.00022, 0.00024, 0.00057, 0.00049, 0.00077, 0.00069],
                '-O2' : [0.00014, 0.00016, 0.00022, 0.00024, 0.0004, 0.00047, 0.00053, 0.00065],
                '-O3' : [0.00014, 0.00016, 0.00024, 0.00024, 0.0003, 0.00042, 0.00044, 0.00059],
            },

            'Group B' : {
                'Labels' :  ["IOpt'", "TOpt", "X", "T", "IOpt", "ROpt", "I'", "I"],
                '-Os' : [0.00062, 0.00077, 0.00234, 0.00129, 0.00084, 0.00121, 0.00397, 0.00464],
                '-O2' : [0.00062, 0.00066, 0.00228, 0.0011, 0.00084, 0.00121, 0.00314, 0.00374],
                '-O3' : [0.00061, 0.00066, 0.00091, 0.00084, 0.00082, 0.00121, 0.00212, 0.0027],

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "P", "E", "Gr"],
                '-Os' : [0.01016, 0.01974, 0.12109, 0.19261, 0.18862],
                '-O2' : [0.01062, 0.01641, 0.10895, 0.16456, 0.17386],
                '-O3' : [0.0048, 0.0062, 0.06391, 0.10831, 0.16691],
            },
        },

        'Memory' : {  
            'Group A' : {   
                 'Labels' :  [ "Sopt", "AOpt'", "SOpt'", "AOpt", "A'", "S", "A", "S'"],
                '-Os': [56468, 8792, 59988, 7924, 3800, 38380, 3096, 38436],
                '-O2' : [57748, 8768, 61748, 7952, 24680, 38820, 19308, 39004],
                '-O3' : [59420, 8912, 65140, 8096, 24720, 41124, 19444, 41564],
            },

            'Group B' : {
                'Labels' :  ["IOpt'", "TOpt", "X", "T", "IOpt", "ROpt", "I'", "I"],               
                '-Os' : [14648, 2184, 20576, 2096, 16772, 10880, 20088, 20088],
                '-O2' : [14464, 2296, 20912, 2200, 16656, 11360, 20580, 20580],
                '-O3' : [14876, 2564, 22592, 1364, 17068, 12460, 21124, 21124],

            },

            'Group C' : {
                'Labels' :  ["Gi", "R", "P", "E", "Gr"],
                '-Os' : [3068, 3880, 37472, 38108, 4896],
                '-O2' : [3356, 5004, 37808, 38692, 5788],
                '-O3' : [7568, 11948, 43616, 30820, 9376],
            },
        }
    }, 

    'M4' : {
        'Runtime' : {
            'Group A' : {
                'Labels' :  ["Sopt", "S", "SOpt'", "AOpt'", "A'", "TOpt", "AOpt", "A"],
                '-Os' : [0.022569875, 0.034502426, 0.034255737, 0.035168288, 0.04107455, 0.052418787, 0.053440301, 0.055036437],
                '-O2' : [0.022110538, 0.031917963, 0.033992738, 0.034979802, 0.05215035, 0.048250349, 0.052800363, 0.071007699],
                '-O3' : [0.0223457, 0.032894775, 0.034451112, 0.034980625, 0.042684738, 0.0482495, 0.052726313, 0.062097611],
            },

            'Group B' : {
                'Labels' :  ["X", "T", "S'", "IOpt'", "I'", "IOpt", "ROpt", "I"],
                '-Os' : [0.164861783, 0.090213638, 0.046938987, 0, 0.293865278, 0, 0.188637204, 0.341086254],
                '-O2' : [0.147647686, 0.078530475, 0.042308187, 0.130084395, 0.248218618, 0.179974042, 0.188317992, 0.28362079],
                '-O3' : [0.063766062, 0.063854787, 0.064696651, 0.129333988, 0.162935309, 0.179290287, 0.188479215, 0.19710701],
            },

            'Group C' : {
                'Labels' :  ["R", "Gi", "P", "E", "Gr"],
                '-Os' : [1.382799149, 0.8055785, 9.949514389, 14.46337843, 9.667762756],
                '-O2' : [1.138388395, 0.817688376, 9.111887932, 10.47863865, 8.74007082],
                '-O3' : [0.765589803, 0.915141374, 5.131352663, 7.085587025, 8.306955338],
            },
        },

        'Energy' : {
            'Group A' : {
                'Labels' :  ["Sopt", "S", "SOpt'", "AOpt'", "A'", "TOpt", "AOpt", "A"],
                '-Os' : [0.00102, 0.00174, 0.00158, 0.00155, 0.00189, 0.00244, 0.00236, 0.00254],
                '-O2' : [0.001, 0.00163, 0.00156, 0.00153, 0.00237, 0.00222, 0.00231, 0.00322],
                '-O3' : [0.00102, 0.0016, 0.00158, 0.00153, 0.00194, 0.00223, 0.00231, 0.00282],
            },

            'Group B' : {
                'Labels' :  ["X", "T", "S'", "IOpt'", "I'", "IOpt", "ROpt", "I"],
                '-Os' : [0.00768, 0.00425, 0.00236, 0, 0.01355, 0, 0.00834, 0.01572],
                '-O2' : [0.00729, 0.00368, 0.00218, 0.00573, 0.01123, 0.0079, 0.0083, 0.01281],
                '-O3' : [0.00325, 0.00288, 0.0031, 0.00567, 0.00748, 0.00784, 0.00834, 0.00903],

            },

            'Group C' : {
                'Labels' :  ["R", "Gi", "P", "E", "Gr"],
                '-Os' : [0.06571, 0.03348, 0.4226, 0.62957, 0.52692],
                '-O2' : [0.0544, 0.03449, 0.38779, 0.47402, 0.47848],
                '-O3' : [0.03558, 0.03933, 0.21408, 0.33353, 0.45582],
            },
        },

        'Memory' : {  
            'Group A' : {
                'Labels' :  ["Sopt", "S", "SOpt'", "AOpt'", "A'", "TOpt", "AOpt", "A"],
                '-O2': [57104, 39264, 60576, 8720, 3664, 2056, 7880, 2960],
                '-O3' : [58320, 39704, 62368, 8696, 23576, 2136, 7848, 18200],
                '-Os' : [59904, 41800, 65624, 8704, 23200, 2264, 7856, 18192],
            },

            'Group B' : {
                'Labels' :  ["X", "T", "S'", "IOpt'", "I'", "IOpt", "ROpt", "I"],
                '-Os' : [21616, 1968, 39304, 0, 21088, 0, 12216, 21088],
                '-O2' : [21904, 2040, 39872, 14504, 21568, 16736, 12600, 21568],
                '-O3' : [23392, 3000, 42224, 14776, 21896, 17024, 13816, 21896],

            },

            'Group C' : {
                'Labels' :  ["R", "Gi", "P", "E", "Gr"],
                '-Os' : [3824, 3000, 38288, 38944, 5064],
                '-O2' : [4984, 3216, 38640, 39544, 5960],
                '-O3' : [11688, 7232, 44480, 41416, 9448],
            },
        },
    },
}

# plt.bar(labels, Os, 0.8, label="Os", color=colours[0])
# plt.bar(labels, O2, 0.6, label="O2", color=colours[1])
# plt.bar(labels, O3, 0.4, label="O3", color=colours[2])
# plt.legend()
# plt.grid(axis='y')
# plt.show()
labels = ['a)', 'b)', 'c)', 'd)', 'e)', 'f)', 'g)', 'h)', 'i)']
board = "m4"
for type, data in meta_data.items():
    print(type)
    if isinstance(data, dict) and (board.lower() in type.lower()):
        fig= plt.figure(figsize=(12, 8))
        # create grid for different subplots
        spec = gridspec.GridSpec(ncols=3, nrows=3,
                         width_ratios=[3,3, 2], wspace=0.15)
        subplot_idx = 1
        for metric, values in data.items():
            for group, values, in values.items():
                idx = 0
                ax=fig.add_subplot(spec[subplot_idx-1])
                ax.get_yaxis().set_label_coords(-0.15,0.5)
                y_max = 0
                for x, y in values.items(): 
                    if not 'labels' in x.lower():
                        y_vals = y
                        if 'Energy' == metric:
                            y_vals = [y_val * 1000 for y_val in y]
                        elif 'Memory' == metric:
                            y_vals = [y_val / 1000 for y_val in y]
                        else:
                            y_vals = [y_val for y_val in y]
                            # print(y_vals)
                        if max(y_vals) > y_max:
                            y_max = max(y_vals)
                            # print(y_max)
                        # ax.subplot(1, 3, subplot_idx)#, gridspec_kw={'width_ratios': [1, 3]})
                        ax.bar(values['Labels'], y_vals, width=meta_data['widths'][idx], color=meta_data['colours'][idx], label=x)
                        ax.text(0.065, 0.95, labels[subplot_idx-1], transform=ax.transAxes, fontsize=11,  va='top', ha='right')
                        idx+=1
                if subplot_idx == 1:
                    plt.ylabel("Runtime (s)", fontsize=12)
                if subplot_idx == 4:
                    plt.ylabel("Average Energy (mJ)", fontsize=12)
                if subplot_idx == 7:
                    plt.ylabel("Flash Memory Usage (KB)", fontsize=12)
                if subplot_idx < 4:
                    ax.set_title(group)
                if subplot_idx < 7:    
                    ax.set_xticklabels([])
                if 'm4' in type.lower(): 
                    if subplot_idx == 1:
                        loc = plticker.MultipleLocator(base=0.005)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.2f'))
                        ylabels = plt.gca().get_yticklabels()
                        # ax.set_yticks(ax.get_yticks()[::2])
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 2:
                        loc = plticker.MultipleLocator(base=0.025)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.2f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 3:
                        plt.legend(loc='center left')
                        loc = plticker.MultipleLocator(base=1)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 4:
                        plt.ylabel("Average Energy (mJ)")
                        loc = plticker.MultipleLocator(base=0.25)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.1f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 5:
                        loc = plticker.MultipleLocator(base=1)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 6:
                        loc = plticker.MultipleLocator(base=50)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 7:
                        plt.ylabel("Flash memory usage (KB)")
                        loc = plticker.MultipleLocator(base=5)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 8:
                        loc = plticker.MultipleLocator(base=2.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 9:
                        loc = plticker.MultipleLocator(base=2)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                if 'm7' in type.lower():
                    if subplot_idx == 1:
                        loc = plticker.MultipleLocator(base=0.005)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.2f'))
                        ylabels = plt.gca().get_yticklabels()
                        # ax.set_yticks(ax.get_yticks()[::2])
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 2:
                        loc = plticker.MultipleLocator(base=0.025)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.2f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 3:
                        plt.legend(loc='center left')
                        loc = plticker.MultipleLocator(base=1)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 4:
                        plt.ylabel("Average Energy (mJ)")
                        loc = plticker.MultipleLocator(base=1.25)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.1f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 5:
                        loc = plticker.MultipleLocator(base=5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 6:
                        loc = plticker.MultipleLocator(base=200)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 7:
                        plt.ylabel("Flash memory usage (KB)")
                        loc = plticker.MultipleLocator(base=2.5)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 8:
                        loc = plticker.MultipleLocator(base=1.25)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.1f'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 9:
                        loc = plticker.MultipleLocator(base=1)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    # ax.set_yticklabels(np.arange(0,round(y_max*1.05,3), round((y_max/12),3)))
                if 'm33' in type.lower():
                    if subplot_idx == 1:
                        loc = plticker.MultipleLocator(base=0.0025)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.3f'))
                        ylabels = plt.gca().get_yticklabels()
                        # ax.set_yticks(ax.get_yticks()[::2])
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 2:
                        loc = plticker.MultipleLocator(base=0.0125)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.3f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 3:
                        plt.legend(loc='center left')
                        loc = plticker.MultipleLocator(base=0.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    if subplot_idx == 4:
                        plt.ylabel("Average Energy (mJ)")
                        loc = plticker.MultipleLocator(base=0.1)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%0.1f'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 5:
                        loc = plticker.MultipleLocator(base=0.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 6:
                        loc = plticker.MultipleLocator(base=12.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 7:
                        plt.ylabel("Flash memory usage (KB)")
                        loc = plticker.MultipleLocator(base=5)
                        ax.yaxis.set_major_locator(loc)
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        ylabels = plt.gca().get_yticklabels()
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 8:
                        loc = plticker.MultipleLocator(base=2.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    elif subplot_idx == 9:
                        loc = plticker.MultipleLocator(base=2.5)
                        ax.yaxis.set_major_locator(loc)
                        ylabels = plt.gca().get_yticklabels()
                        ax.yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
                        for i, label in enumerate(ylabels):
                            if i % 2 == 0:
                                label.set_visible(False)
                    # ax.set_yticklabels(np.arange(0,round(y_max*1.05,3), round((y_max/12),3)))

                # print(y_max)
                # loc = plticker.MultipleLocator(base=round(y_max/8,5))
                ax.yaxis.set_major_locator(loc)
                subplot_idx +=1
                ax.grid(axis='y', alpha=0.4)
                
        plt.subplots_adjust(left = 0.07, right = 0.98, top=0.955, wspace=0.9, hspace=0.07, bottom=0.075) 
        # plt.tight_layout()
        # plt.suptitle('Performance of the Top 10 NIST algorithms on Cortex-' + type.upper(), fontsize=16, fontweight='bold')
        fig.text(0.5, 0.01, 'Lightweight cryptography algorithm', ha='center', fontsize=14)
        plt.show()
        # break


