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

NPV_1_20 = [-2300000]
NPV_2_20 = [-2300000*4]

NPV_1_15 = [-2300000]
NPV_2_15 = [-2300000*4]

NPV_1_25 = [-2300000]
NPV_2_25 = [-2300000*4]

for n in [1, 2, 3, 4, 5, 6, 7]:
    NPV_1_20.append((4770000 * (1.2**n) * 0.4) - 660000)
    NPV_2_20.append((4770000 * (1.2**n) * 0.7) - 660000)
    
    NPV_1_15.append((4770000 * (1.15**n) * 0.4) - 660000)
    NPV_2_15.append((4770000 * (1.15**n) * 0.7) - 660000)
    
    NPV_1_25.append((4770000 * (1.25**n) * 0.4) - 660000)
    NPV_2_25.append((4770000 * (1.25**n) * 0.7) - 660000)
    
fig, axs = plt.subplots(1,1,figsize=(10, 10))
fs = 14
axs.axhline(0, color = "black", ls = "--")

Years = [0,1,2,3,4,5,6,7]
axs.plot(Years, np.cumsum(NPV_1_20), color = "blue", label = "Option A")
axs.fill_between(Years, np.cumsum(NPV_1_15), np.cumsum(NPV_1_25), color = "blue", ec = None, alpha = 0.2, label = "+/- 5% Revenue Growth Uncertainty")

axs.plot(Years, np.cumsum(NPV_2_20), color = "orange", label = "Option B")
axs.fill_between(Years, np.cumsum(NPV_2_15), np.cumsum(NPV_2_25), color = "orange", ec = None, alpha = 0.2, label = "+/- 5% Revenue Growth Uncertainty")

axs.legend(loc = "upper left", fontsize = 13)
axs.set_xlabel("Year", fontsize = 14)
axs.set_ylabel("NPV (£ millions)", fontsize = 14)
axs.set_box_aspect(0.45)
axs.set_yticks([-1e7, 0, 1e7, 2e7, 3e7, 4e7, 5e7, 6e7, 7e7])
axs.set_yticklabels([-10, 0, 10, 20, 30, 40, 50, 60, 70])