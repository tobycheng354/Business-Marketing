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

CUL_2018 = 67
CUL_2019 = 406
CUL_2020 = 303
CUL_2021 = 269
CUL_2022 = 529

URUS_2018 = 290
URUS_2019 = 967
URUS_2020 = 1087
URUS_2021 = 1280
URUS_2022 = 1439

BENT_2018 = 1217
BENT_2019 = 991
BENT_2020 = 975
BENT_2021 = 1180
BENT_2022 = 1476

CC_2018 = (CUL_2018 * 298) / ((CUL_2018 * 298) + (URUS_2018 * 188) + (BENT_2018 * 169))
CC_2019 = (CUL_2019 * 298) / ((CUL_2019 * 298) + (URUS_2019 * 188) + (BENT_2019 * 169))
CC_2020 = (CUL_2020 * 298) / ((CUL_2020 * 298) + (URUS_2020 * 188) + (BENT_2020 * 169))
CC_2021 = (CUL_2021 * 298) / ((CUL_2021 * 298) + (URUS_2021 * 188) + (BENT_2021 * 169))
CC_2022 = (CUL_2022 * 298) / ((CUL_2022 * 298) + (URUS_2022 * 188) + (BENT_2022 * 169))
CC = [CC_2018, CC_2019, CC_2020, CC_2021, CC_2022]

UC_2018 = (URUS_2018 * 188) / ((CUL_2018 * 298) + (URUS_2018 * 188) + (BENT_2018 * 169))
UC_2019 = (URUS_2019 * 188) / ((CUL_2019 * 298) + (URUS_2019 * 188) + (BENT_2019 * 169))
UC_2020 = (URUS_2020 * 188) / ((CUL_2020 * 298) + (URUS_2020 * 188) + (BENT_2020 * 169))
UC_2021 = (URUS_2021 * 188) / ((CUL_2021 * 298) + (URUS_2021 * 188) + (BENT_2021 * 169))
UC_2022 = (URUS_2022 * 188) / ((CUL_2022 * 298) + (URUS_2022 * 188) + (BENT_2022 * 169))
UC = [UC_2018, UC_2019, UC_2020, UC_2021, UC_2022]

BC_2018 = (BENT_2018 * 169) / ((CUL_2018 * 298) + (URUS_2018 * 188) + (BENT_2018 * 169))
BC_2019 = (BENT_2019 * 169) / ((CUL_2019 * 298) + (URUS_2019 * 188) + (BENT_2019 * 169))
BC_2020 = (BENT_2020 * 169) / ((CUL_2020 * 298) + (URUS_2020 * 188) + (BENT_2020 * 169))
BC_2021 = (BENT_2021 * 169) / ((CUL_2021 * 298) + (URUS_2021 * 188) + (BENT_2021 * 169))
BC_2022 = (BENT_2022 * 169) / ((CUL_2022 * 298) + (URUS_2022 * 188) + (BENT_2022 * 169))
BC = [BC_2018, BC_2019, BC_2020, BC_2021, BC_2022]


fig, axs = plt.subplots(2,1,figsize=(15, 15))
lw = 3

x_2018 = 0
x_2019 = 1
x_2020 = 2
x_2021 = 3
x_2022 = 4  
shift = 0.3
fs = 14

col1 = "cadetblue"
col3 = 'orange'
col2 = 'silver'

axs[0].bar(x_2018 + (shift*1), BENT_2018, width = shift, color = col1)
axs[0].bar(x_2018 - (shift*1), CUL_2018, width = shift, color = col2)
axs[0].bar(x_2018 - (shift*0), URUS_2018, width = shift, color = col3)

axs[0].bar(x_2019 + (shift*1), BENT_2019, width = shift, color = col1)
axs[0].bar(x_2019 - (shift*1), CUL_2019, width = shift, color = col2)
axs[0].bar(x_2019 - (shift*0), URUS_2019, width = shift, color = col3)

axs[0].bar(x_2020 + (shift*1), BENT_2020, width = shift, color = col1)
axs[0].bar(x_2020 - (shift*1), CUL_2020, width = shift, color = col2)
axs[0].bar(x_2020 - (shift*0), URUS_2020, width = shift, color = col3)

axs[0].bar(x_2021 + (shift*1), BENT_2021, width = shift, color = col1)
axs[0].bar(x_2021 - (shift*1), CUL_2021, width = shift, color = col2)
axs[0].bar(x_2021 - (shift*0), URUS_2021, width = shift, color = col3)

axs[0].bar(x_2022 + (shift*1), BENT_2022, width = shift, color = col1)
axs[0].bar(x_2022 - (shift*1), CUL_2022, width = shift, color = col2)
axs[0].bar(x_2022 - (shift*0), URUS_2022, width = shift, color = col3)

axs[0].set_xticks([0, 1, 2, 3, 4])
axs[0].set_xticklabels(["2018", "2019","2020","2021", "2022"])

axs[0].set_box_aspect(0.4)
axs[0].set_xlabel("Year", fontsize = fs)
axs[0].set_ylabel("European Sales", fontsize = fs)

Years = np.linspace(2018, 2022, 5)


axs[1].plot(Years, BC, color=col1, lw = lw, label = "Bentley Benteyga")
axs[1].plot(Years, CC, color=col2, lw = lw, label = "Rolls-royce Cullinan")
axs[1].plot(Years, UC, color=col3, lw = lw, label = "Lamborghini Urus")
axs[1].axvline(2020, color = col1, ls = "--", lw = 1)
axs[1].annotate("BENTEYGA FACELIFT", [2020-0.1, 0.5], rotation = 90, fontsize = 7)
axs[1].set_xlabel("Year", fontsize = fs)
axs[1].set_ylabel("Market Share (High-end luxury SUVs)", fontsize = fs)

axs[1].set_yticks(np.linspace(0, 1, 11))
axs[1].set_yticklabels(["0%", "10%", "20%", "30%", "40%", "50%", "60%" ,"70%", "80%", "90%", "100%"])


axs[1].set_xticks(Years)
axs[1].set_ylim([0,1])
axs[1].set_box_aspect(0.4)
axs[1].legend()


