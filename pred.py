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

ROS_2022 = 33.8
ROS_2021 = 33.0
ROS_2020 = 19.46
ROS_2019 = 22.11
ROS_2018 = 4.59
ROS_2017 = 17.81
ROS_2016 = 22.52
ROS_2015 = 25.11
ROS_2014 = 4.1
ROS_2013 = 13.6

REV_2022 = 2905.6
REV_2021 = 2392.9
REV_2020 = 1717
REV_2019 = 1868.8
REV_2018 = 1259.8
REV_2017 = 1593.8
REV_2016 = 1660.6
REV_2015 = 1397.7
REV_2014 = 1379.7
REV_2013 = 1398.8


ROS = [ROS_2022, ROS_2021, ROS_2020, ROS_2019, ROS_2018, ROS_2017, ROS_2016, ROS_2015, ROS_2014, ROS_2013]
REV = [REV_2022, REV_2021, REV_2020, REV_2019, REV_2018, REV_2017, REV_2016, REV_2015, REV_2014, REV_2013]
ROS.reverse()
REV.reverse()

fig, axs = plt.subplots(2,1,figsize=(10, 10))
fontsize = 13
Years_1 = np.linspace(2013, 2022, 10)
Years_2 = np.linspace(2023.5, 2031.5, 5)
Years_full = np.linspace(2013, 2032, 20)

axs[0].bar(Years_1, ROS, color = "darkgrey", label = "Observed")

avg_ros = statistics.mean(ROS)
axs[0].axhline(avg_ros, color = "red", label = "10 Year Average (2013-2022)")
axs[0].bar(Years_2, [avg_ros, avg_ros, avg_ros, avg_ros, avg_ros], width = 1.75, color = "cadetblue", label = "Predicted")
axs[0].set_yticks([0, 5, 10, 15, 20, 25, 30, 35, 40])
axs[0].set_yticklabels(["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%"])
axs[0].set_ylabel("Operating Profit Margin (excl. R&D)", fontsize = fontsize)


axs[1].bar(Years_1, REV, color = "darkgrey", label = "Observed")

a_rev, b_rev = np.polyfit(Years_1, REV, 1)
axs[1].plot([2010, 2035],[2010*a_rev+b_rev, 2035*a_rev+b_rev], color = "red", label = "Predicted Growth Rate")

rev_pred = []
for y in Years_2:
    rev_pred.append(a_rev*y+b_rev)
axs[1].bar(Years_2, rev_pred, width = 1.75, color = "orange", label = "Predicted")
axs[1].set_ylabel("Revenue (£ Millions)", fontsize = fontsize)

for i in [0,1]:
    axs[i].set_xlim([2012,2033])
    axs[i].set_xticks(Years_full)
    axs[i].set_xlabel("Year", fontsize = fontsize)
    axs[i].legend()

for i in [1, 2, 3, 4, 5]:
    rev = rev_pred[i-1] * 2
    gms = ((495104 * ((1+0.069)**(2*i - 1))) + (495104 * ((1+0.069)**(2*i))))/2
    print((str(rev))[:4], (str(gms))[:6], (str(rev/gms*100))[:5])
    
UKMS = 770000000
print(0.00941 * UKMS * 0.025 * 0.1961)
print(0.00911 * UKMS * 0.135 * 0.1961)
print(0.00873 * UKMS * 0.34 * 0.1961)
print(0.00831 * UKMS * 0.34 * 0.1961)
print(0.00786 * UKMS * 0.16 * 0.1961) 