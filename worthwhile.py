import numpy  as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random
import matplotlib as mpl
import statistics
from scipy.stats import norm
plt.style.use('default')
plt.rcParams["font.family"] = "Times New Roman"
from scipy.stats import norm

NCF1 = 1481455
NCF2 = 1725223
NCF3 = 1981235

I_0 = 2300000
rs = np.linspace(1, 0, 1001)
sum_DCFs = []
for r in rs:
    sum_DCS = (NCF1 * (1/(1+r)**1)) + (NCF2 * (1/(1+r)**2)) + (NCF3 * (1/(1+r)**3))
    sum_DCFs.append(sum_DCS)
NPVs_high = []
NPVs_low = []
for i in sum_DCFs:
    if i - I_0 > 0:
        NPVs_high.append(i - I_0)
    elif i - I_0 < 0:
        NPVs_low.append(i - I_0)


MARR5 = I_0 * 0.05
MARR10 = I_0 * 0.10
MARR15 = I_0 * 0.15

ww = False
ww5 = False
ww10 = False
ww15 = False

NPVs = NPVs_low + NPVs_high 

for NPV in NPVs:
    if ww == False:
        if NPV > 0:
            NPV_0 = NPV
            idx_0 = NPVs.index(NPV)
            r_0 = rs[idx_0]
            ww = True
    if ww5 == False:
        if NPV > MARR5:
            NPV_5 = NPV
            idx_5 = NPVs.index(NPV)
            r_5 = rs[idx_5]
            ww5 = True
    if ww10 == False:
        if NPV > MARR10:
            NPV_10 = NPV
            idx_10 = NPVs.index(NPV)
            r_10 = rs[idx_10]
            ww10 = True
    if ww15 == False:
        if NPV > MARR15:
            NPV_15 = NPV
            idx_15 = NPVs.index(NPV)
            r_15 = rs[idx_15]
            ww15 = True
            

fig, axs = plt.subplots(1,1,figsize=(8, 8))        
axs.set_xlabel("Discount Rate (%)", fontsize = 14)
axs.set_ylabel("NPV (£ Millions)", fontsize = 14)
axs.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
axs.set_xticklabels(["0%", "20%", "40%", "60%", "80%", "100%"])
axs.set_yticks([ -1e6, -0.5e6, 0, 0.5e6, 1e6, 1.5e6, 2e6, 2.5e6, 3e6])
axs.set_yticklabels([-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])
axs.set_xlim([0,1])
axs.set_ylim([-1e6, 3e6])


axs.axhline(0, color = "black", lw = 1)
axs.axhline(MARR5, 0, r_5, color = "r", lw = 1, ls = "--")
axs.axhline(MARR10, 0, r_10, color = "orange", lw = 1, ls = "--")
axs.axhline(MARR15, 0, r_15,color = "green", lw = 1, ls = "--")
axs.axvline(r_5, 0, (1e6 + NPV_5)/4e6, color = "r", lw = 1, ls = "--", label = ("Discount Rate for MARR = 5%: " + (str(r_5*100))[:4] + "%"))
axs.axvline(r_10, 0, (1e6 + NPV_10)/4e6, color = "orange", lw = 1, ls = "--", label = ("Discount Rate for MARR = 10%: " + (str(r_10*100))[:4] + "%"))
axs.axvline(r_15, 0, (1e6 + NPV_15)/4e6, color = "green", lw = 1, ls = "--", label = ("Discount Rate for MARR = 15%: " + (str(r_15*100))[:4] + "%"))
axs.axvline(r_0, color = "black", lw = 1, ls = "dotted", label = ("Discount Rate for IRR: " + (str(r_0*100))[:4] + "%"))

axs.plot(rs[len(NPVs_low):], NPVs_high, color = "purple", lw = 3, label = "NPV > 0")
axs.plot(rs[:len(NPVs_low)], NPVs_low, color = "b", lw = 3, label = "NPV < 0")
axs.legend(fontsize = 14)
axs.set_box_aspect(0.7)


    
