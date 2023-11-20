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

y1_10 = 1308000
y1_20 = 1481455
y1_30 = 1654909

y2_10 = 1362545
y2_20 = 1725223
y2_30 = 2119438

y3_10 = 1412132
y3_20 = 1981235
y3_30 = 2653551

IC = -2300000

NPV_10 = [IC + y1_10, IC + y1_10 + y2_10, IC + y1_10 + y2_10 + y3_10]
NPV_20 = [IC + y1_20, IC + y1_20 + y2_20, IC + y1_20 + y2_20 + y3_20]
NPV_30 = [IC + y1_30, IC + y1_30 + y2_30, IC + y1_30 + y2_30 + y3_30]

fig, axs = plt.subplots(1,1,figsize=(10, 10))
fs = 14

Years = [1,2,3]
axs.fill_between(Years, NPV_20, NPV_30, color = "green", alpha = 0.2, ec = None, label = "Upper Bound (<30% Revenue Growth per Year)")
axs.plot(Years, NPV_20, color = "black", ls = "--", lw = 2, label = "Predicted (20% Revenue Growth per Year)")
axs.fill_between(Years, NPV_10, NPV_20, color = "red", alpha = 0.2, ec = None, label = "Lower Bound (>10% Revenue Growth per Year)")
axs.set_xlabel("Year", fontsize = fs)
axs.set_ylabel("NPV (£ millions)", fontsize = fs)
axs.axhline(0, color = "black", lw = 0.5)
axs.set_xticks([1,2,3])
axs.set_yticks([-1e6, 0, 1e6, 2e6, 3e6, 4e6, 5e6, 6e6])
axs.set_yticklabels([-1, 0, 1, 2, 3, 4, 5, 6])
axs.set_box_aspect(0.4)
axs.legend()