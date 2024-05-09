import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as plticker
import numpy as np
from scipy.stats import norm

AUT = ["A", "AOpt", "A'", "AOpt'", "E", "Gi", "Gr", "I", "I'", "IOpt'", "IOpt", "P", "R", "ROpt", "S", "Sopt", "S'", "SOpt'", "T", "TOpt", "X"]
#   m4
err_m4 = [1.55076E-07, 2.44767E-07, 2.19307E-07, 1.28573E-07, 1.16644E-06, 4.93839E-07, 2.19592E-05, 4.47819E-07, 1.37603E-06, 3.79664E-07, 1.93046E-06, 2.13041E-05, 3.40861E-06, 3.47202E-07, 2.16707E-06, 2.03314E-07, 1.0802E-06, 2.32094E-07, 1.85892E-07, 2.22459E-07, 7.52943E-07]
#   m7
err_m7 =[3.32E-07, 2.69E-07, 2.51574E-07, 2.39981E-07, 4.69697E-06, 7.83495E-07, 1.74896E-05, 5.77895E-07, 5.17668E-07, 3.20594E-07, 2.869E-07, 3.23213E-06, 2.68074E-06, 2.53223E-07, 4.90214E-07, 2.13562E-07, 2.28353E-06, 2.95599E-07, 2.3572E-07, 5.60613E-07, 2.03665E-05]
#   m33
err_m33 = [4.97E-07, 1.05E-06, 6.93794E-07, 1.17653E-06, 4.85609E-07, 3.71292E-07, 1.52333E-06, 4.24686E-07, 4.19905E-07, 1.4136E-06, 1.7931E-06, 1.089E-06, 6.07518E-07, 7.05684E-07, 3.64442E-07, 5.50702E-07, 3.48241E-07, 6.61442E-07, 1.6014E-07, 1.45665E-07, 4.42545E-07]

# # m7
r_e= [1.60E-07, 2.78E-07, 1.86E-07, 2.39E-07, 2.16E-07, 2.29E-07, 2.76E-07, 2.47E-07, 3.57E-07, 2.38E-07, 2.03E-07, 3.52E-07, 6.28E-07, 2.94E-07, 2.91E-07, 3.36E-07, 3.15E-07, 2.51E-07, 1.10E-06, 3.31E-07, 2.90E-07, 4.52E-07, 5.58E-06, 2.29E-06, 1.39E-07, 2.69E-07, 1.95E-07, 3.74E-07, 3.20E-07, 7.50E-07, 2.51E-07, 2.66E-07, 2.22E-07, 2.30E-07, 3.73E-07, 3.99E-07, 3.37E-05, 2.35E-05, 5.77E-07, 6.21E-07, 5.62E-07, 4.07E-07, 6.68E-07, 1.10E-06, 1.06E-06, 8.17E-07, 1.63E-06, 5.10E-06, 2.87E-06, 3.75E-06, 8.78E-06, 7.62E-06, 3.47E-05, 3.71E-06, 3.61E-06, 2.08E-06, 7.13E-06, 0.000007]
t = [0.006027, 0.006310, 0.006596, 0.009246, 0.009259, 0.009347, 0.009358, 0.009461, 0.009555, 0.010851, 0.018149, 0.024098, 0.027713, 0.030064, 0.030173, 0.034040, 0.034455, 0.034984, 0.035253, 0.035408, 0.035690, 0.037278, 0.037372, 0.038198, 0.043962, 0.046757, 0.047831, 0.048245, 0.050356, 0.051799, 0.053589, 0.054998, 0.056030, 0.057863, 0.097341, 0.120019, 0.121474, 0.121845, 0.169662, 0.192122, 0.208715, 0.235284, 0.241133, 0.346400, 0.560318, 0.688880, 1.021306, 1.551468, 4.662707, 5.153526, 6.011897, 6.425501, 7.245181, 8.087112, 10.294661, 10.724458, 11.457243, 11.45724342]
# # r_e = [0.010849755, 0.010850593, 0.01085044, 0.010850486, 0.010850449, 0.010850648, 0.010850486, 0.010850759, 0.010850454, 0.010850588, 0.010850412, 0.010850584, 0.010850518, 0.010850356, 0.010851013, 0.010850764, 0.01085044, 0.010850704, 0.010850537, 0.010850949]

# # normalise
min_val = np.min(t)
max_val = np.max(t)
t_n = (t - min_val) / (max_val - min_val)

# # # m4
r_e4= [1.29355E-07, 2.06132E-07, 2.58187E-07, 8.87778E-07, 2.90829E-06, 1.76136E-07, 2.48665E-07, 2.5291E-07, 2.53174E-06, 1.28472E-07, 9.45631E-08, 2.25766E-07, 1.52395E-07, 1.83645E-07, 1.8382E-06, 8.30891E-07, 2.29128E-07, 1.89052E-07, 9.87531E-08, 2.31399E-07, 3.67783E-07, 3.19631E-07, 1.18975E-07, 4.85071E-07, 2.62121E-07, 1.61706E-07, 3.5691E-07, 4.67221E-07, 2.84483E-07, 9.73769E-07, 9.05182E-07, 7.25015E-07, 3.87261E-07, 5.04775E-07, 3.41825E-07, 3.53842E-07, 3.18158E-07, 7.07241E-07, 7.72032E-07, 3.74618E-07, 2.52093E-06, 4.74488E-06, 4.82821E-06, 3.64105E-07, 5.61131E-07, 5.16768E-07, 3.94951E-06, 1.17539E-06, 5.8823E-05, 4.33236E-07, 3.32504E-05, 6.16858E-06, 2.09042E-06, 2.47014E-05, 1.29437E-06, 1.9313E-06, 1.04144E-06]
t4 = [0.005031935, 0.005215941, 0.005232651, 0.006249033, 0.006319476, 0.006320001, 0.008088749, 0.008105341, 0.008136616, 0.010660914, 0.014312808, 0.014490209, 0.015493107, 0.016487089, 0.019719651, 0.020133246, 0.021261664, 0.022936308, 0.023834231, 0.023988924, 0.02409947, 0.024099819, 0.024390579, 0.02815608, 0.028371851, 0.031974106, 0.032328332, 0.03248339, 0.03295561, 0.039238047, 0.045285111, 0.046493943, 0.046560892, 0.046666629, 0.076619408, 0.078046883, 0.082556668, 0.09785285, 0.114802198, 0.136477976, 0.142077926, 0.166407841, 0.189659003, 0.212824899, 0.403683189, 0.422477239, 0.566620786, 0.690931751, 2.462203538, 3.914223963, 4.197076321, 4.721039486, 5.489943385, 5.725511101, 6.042226338, 6.190936542, 7.400717163]

min_val = np.min(t4)
max_val = np.max(t4)
t4_n = (t4 - min_val) / (max_val - min_val)

# # # m33
r_e33= [4.44293E-07, 6.25604E-07, 5.38146E-07, 1.22141E-06, 1.19504E-06, 1.019E-06, 7.47907E-07, 7.01077E-07, 4.82416E-07, 8.56728E-07, 2.93548E-07, 9.23642E-07, 4.29685E-07, 3.40933E-07, 2.84232E-07, 2.68347E-07, 3.47834E-07, 3.84793E-07, 1.29493E-06, 1.42206E-06, 1.2894E-07, 1.40463E-07, 1.4107E-06, 1.55937E-07, 4.37431E-07, 1.46236E-07, 1.70275E-06, 1.70795E-06, 1.82514E-06, 1.22883E-07, 1.98487E-07, 7.55794E-07, 7.02744E-07, 6.0205E-07, 4.28379E-07, 4.25684E-07, 4.29111E-07, 4.10994E-07, 4.44466E-07, 4.65988E-07, 3.53271E-07, 3.63095E-07, 4.58843E-07, 5.96291E-07, 2.99025E-07, 3.263E-07, 5.47702E-07, 6.29949E-07, 9.77846E-07, 2.85182E-07, 1.03172E-06, 1.1703E-06, 1.40104E-06, 1.5511E-06, 3.70123E-07, 1.49088E-06, 7.62667E-07]
t33 = [0.005031935, 0.005215941, 0.005232651, 0.006249033, 0.006319476, 0.006320001, 0.008088749, 0.008105341, 0.008136616, 0.010660914, 0.014312808, 0.014490209, 0.015493107, 0.016487089, 0.019719651, 0.020133246, 0.021261664, 0.022936308, 0.023834231, 0.023988924, 0.02409947, 0.024099819, 0.024390579, 0.02815608, 0.028371851, 0.031974106, 0.032328332, 0.03248339, 0.03295561, 0.039238047, 0.045285111, 0.046493943, 0.046560892, 0.046666629, 0.076619408, 0.078046883, 0.082556668, 0.09785285, 0.114802198, 0.136477976, 0.142077926, 0.166407841, 0.189659003, 0.212824899, 0.403683189, 0.422477239, 0.566620786, 0.690931751, 2.462203538, 3.914223963, 4.197076321, 4.721039486, 5.489943385, 5.725511101, 6.042226338, 6.190936542, 7.400717163]

min_val = np.min(t33)
max_val = np.max(t33)
t33_n = (t33 - min_val) / (max_val - min_val)

# # convert to us
err_m7 = np.array(err_m7)*1e6
err_m4 = np.array(err_m4) *1e6
err_m33 = np.array(err_m33)*1e6
r_e = np.array(r_e)*1e6
r_e4 = np.array(r_e4) *1e6
r_e33 = np.array(r_e33)*1e6

# standardise
# r_e_st = (r_e - np.mean(r_e))/np.std(r_e)
# r_e_st4 = (r_e4 - np.mean(r_e4))/np.std(r_e4)
# r_e_st33 = (r_e33 - np.mean(r_e33))/np.std(r_e33)

# rms_m7 = np.sqrt(np.mean(np.array(r_e) ** 2))
# rms_m4 = np.sqrt(np.mean(np.array(r_e4) ** 2))
# rms_m33 = np.sqrt(np.mean(np.array(r_e33) ** 2))
# var_m7 = np.var(np.array(r_e))
# var_m4 = np.var(np.array(r_e4))
# var_m33 = np.var(np.array(r_e33))

print("M7 Average STD:", round(np.mean(r_e), 2))
print("M4 Average STD:", round(np.mean(r_e4), 2))
print("M33 Average STD:", round(np.mean(r_e33), 2))
# print("M4"RMS:", round(rms_m4, 2), " Var: ",  round(var_m4, 2))
# print("M33", len(t33), "RMS:", round(rms_m33, 2), " Var: ",  round(var_m33, 2))
# print(np.mean(np.array(r_e)))

# min_val = np.min(t33)
# max_val = np.max(t33)
# t33_n = (t33 - min_val) / (max_val - min_val)


bar_width = 0.2  # Width of each bar
bar_space = 0  # Space between each group of bars
x_axis = np.arange(len(AUT))
# colors = ["skyblue", "Green", "Orange"]
colors = ["#000080", "skyblue", "#1e90ff", "#87cefa"]
plt.figure(figsize=(12,8))
plt.subplot(2,1,1)

plt.bar(x_axis - bar_width - bar_space, err_m7, width=bar_width, color=colors[0], label='M7')
plt.bar(x_axis, err_m4, width=bar_width, color=colors[1], label='M4')
plt.bar(x_axis + bar_width + bar_space, err_m33, width=bar_width, color=colors[2], label='M33')
plt.xlim([x_axis[0]-bar_width-0.1, x_axis[20]+bar_width+0.1])
plt.xticks([])
plt.xlabel('')
plt.ylim([6,23])
plt.ylabel('deviation (us) ', fontsize=11, verticalalignment='bottom')

# plt.plot(t_n, r_e, color=colors[0], label='M7')
# plt.plot(t4_n, r_e4, color=colors[1], label='M4')
# plt.plot(t33_n, r_e33, color=colors[2], label='M33')
# plt.axvline(x=t_n[round(np.percentile(np.arange(0 , len(t_n)), 75))], color='red', linestyle='--', label='75th percentile index - M7')
# plt.axvline(x=t4_n[round(np.percentile(np.arange(0 , len(t4_n)), 75))], color='blue', linestyle='--', label='75th percentile index - M4')
# plt.axvline(x=t33_n[round(np.percentile(np.arange(0 , len(t33_n)), 75))], color='green', linestyle='--', label='75th percentile index - M33')
# plt.xlim((0,1))
# plt.ylabel('Standard deviation (us)', fontsize=11)
# plt.text(-0.03, 0, "a)", fontsize=11,  weight='bold',va='top', ha='right')
plt.grid(axis='y', alpha=0.4)
plt.legend(loc='upper left')

plt.subplot(2,1,2)
plt.bar(x_axis - bar_width - bar_space, err_m7, width=bar_width, color=colors[0], label='M7')
plt.bar(x_axis, err_m4, width=bar_width, color=colors[1], label='M4')
plt.bar(x_axis + bar_width + bar_space, err_m33, width=bar_width, color=colors[2], label='M33')
plt.xticks(x_axis, AUT )
plt.xlim([x_axis[0]-bar_width-0.1, x_axis[20]+bar_width+0.1])
plt.ylim([0,5])
# plt.plot(t_n, r_e, color=colors[0], label='M7')
# plt.plot(t4_n, r_e4, color=colors[1], label='M4')
# plt.plot(t33_n, r_e33, color=colors[2], label='M33')
# plt.axvline(x=t_n[round(np.percentile(np.arange(0 , len(t_n)), 75))], color='red', linestyle='--', label='75th percentile index - M7')
# plt.axvline(x=t4_n[round(np.percentile(np.arange(0 , len(t4_n)), 75))], color='blue', linestyle='--', label='75th percentile index - M4')
# plt.axvline(x=t33_n[round(np.percentile(np.arange(0 , len(t33_n)), 75))], color='green', linestyle='--', label='75th percentile index - M33')
# plt.xlim((0,1))
# plt.xscale("log")
# plt.xlabel('Logarithmic normalised time (s)', fontsize=11)
plt.subplots_adjust(left = 0.07, right = 0.98, top=0.96, wspace=0.9, bottom=0.11, hspace=0.04)
plt.ylabel('Standard ', fontsize=11, verticalalignment='bottom', labelpad=10)
plt.xlabel('Lightweight Cryptography Algorithm', fontsize=11)
plt.grid(axis='y', alpha=0.4)
plt.show()


# x = np.linspace(-3, 3, len(r_e))  # Generate 100 points from -3 to 3
# plt.plot(x, norm.pdf(r_e,0,1), color=colors[0], label='M7')
# plt.ylim((0, 2e-20))
# plt.bar(x_axis - bar_width - bar_space, err_m7, width=bar_width, color=colors[0], label='M7')
# plt.bar(x_axis, err_m4, width=bar_width, color=colors[1], label='M4')
# plt.bar(x_axis + bar_width + bar_space, err_m33, width=bar_width, color=colors[2], label='M33')
# plt.xticks(x_axis, AUT )
# plt.yticks(np.arange(0 , 23, 0.5, dtype=float))
# ylabels = plt.gca().get_yticklabels()
# # ax.set_yticks(ax.get_yticks()[::2])
# for i, label in enumerate(ylabels):
#     if i % 2 != 0:
#         label.set_visible(False)
# plt.gca().yaxis.set_major_formatter(plticker.FormatStrFormatter('%d'))
# plt.xticks(np.arange(0,1.1, 0.1))
# plt.xscale("log")