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

USA_2022 = 4221
China_2022 = 3655
Europe_2022 = 2809
Asia_Pacific_2022 = 2031
UK_2022 = 1490
ME_Africa_India_2022 = 968
Total_2022 = USA_2022 + China_2022 + Europe_2022 + Asia_Pacific_2022 + UK_2022 + ME_Africa_India_2022

USA_2021 = 4212
China_2021 = 4033
Europe_2021 = 2520
Asia_Pacific_2021 = 1651
UK_2021 = 1328
ME_Africa_India_2021 = 915
Total_2021 = USA_2021 + China_2021 + Europe_2021 + Asia_Pacific_2021 + UK_2021 + ME_Africa_India_2021

USA_2020 = 3035
China_2020 = 2880
Europe_2020 = 2193
Asia_Pacific_2020 = 1203
UK_2020 = 1160
ME_Africa_India_2020 = 735
Total_2020 = USA_2020 + China_2020 + Europe_2020 + Asia_Pacific_2020 + UK_2020 + ME_Africa_India_2020

USA_2019 = 2913
China_2019 = 1940
Europe_2019 = 2670
Asia_Pacific_2019 = 651 + 488
UK_2019 = 1492
ME_Africa_India_2019 = 852
Total_2019 = USA_2019 + China_2019 + Europe_2019 + Asia_Pacific_2019 + UK_2019 + ME_Africa_India_2019

USA_2018 = 2235
China_2018 = 2219
Europe_2018 = 2536
Asia_Pacific_2018 = 654 + 520
UK_2018 = 1356
ME_Africa_India_2018 = 974
Total_2018 = USA_2018 + China_2018 + Europe_2018 + Asia_Pacific_2018 + UK_2018 + ME_Africa_India_2018


USA = [USA_2018, USA_2019, USA_2020, USA_2021, USA_2022]
China = [China_2018, China_2019, China_2020, China_2021, China_2022]
Europe = [Europe_2018, Europe_2019, Europe_2020, Europe_2021, Europe_2022]
Asia_Pacific = [Asia_Pacific_2018, Asia_Pacific_2019, Asia_Pacific_2020, Asia_Pacific_2021, Asia_Pacific_2022]
UK = [UK_2018, UK_2019, UK_2020, UK_2021, UK_2022]
ME_Africa_India = [ME_Africa_India_2018, ME_Africa_India_2019, ME_Africa_India_2020, ME_Africa_India_2021, ME_Africa_India_2022]

Revenue = [1.259, 1.868, 1.717, 2.393, 2.905]


S_America = USA
S_Other = ME_Africa_India
S_Asia = []
S_Europe = []
for i in [0, 1, 2, 3, 4]:
    S_Asia.append(China[i] + Asia_Pacific[i])
    S_Europe.append(Europe[i] + UK[i])
    
    
H_Americas_2018 = 5.68 + 0.61
H_Americas_2019 = 6.30 + 0.62
H_Americas_2020 = 6.98 + 0.60
H_Americas_2021 = 7.90 + 0.59
H_Americas_2022 = 7.35 + 0.63
H_America = [H_Americas_2018, H_Americas_2019, H_Americas_2020, H_Americas_2021, H_Americas_2022]

H_Asia_2018 = 6.07
H_Asia_2019 = 6.53
H_Asia_2020 = 6.90
H_Asia_2021 = 7.20
H_Asia_2022 = 7.05
H_Asia = [H_Asia_2018, H_Asia_2019, H_Asia_2020, H_Asia_2021, H_Asia_2022]

H_Europe_2018 = 4.80
H_Europe_2019 = 5.22
H_Europe_2020 = 5.36
H_Europe_2021 = 5.72
H_Europe_2022 = 5.60
H_Europe = [H_Europe_2018, H_Europe_2019, H_Europe_2020, H_Europe_2021, H_Europe_2022]

H_Other_2018 = 0.69 + 0.17
H_Other_2019 = 0.76 + 0.18
H_Other_2020 = 0.81 + 0.18
H_Other_2021 = 0.86 + 0.19
H_Other_2022 = 0.88 + 0.20
H_Other = [H_Other_2018, H_Other_2019, H_Other_2020, H_Other_2021, H_Other_2022]

H_Am_M = statistics.mean(H_America)*1000000
S_Am_M = statistics.mean(S_America) 
CCR_Am = (str(S_Am_M/H_Am_M * 100))[:5]

H_As_M = statistics.mean(H_Asia)*1000000
S_As_M = statistics.mean(S_Asia) 
CCR_As = (str(S_As_M/H_As_M * 100))[:5]

H_Eu_M = statistics.mean(H_Europe)*1000000
S_Eu_M = statistics.mean(S_Europe) 
CCR_Eu = (str(S_Eu_M/H_Eu_M * 100))[:5]

H_Other_M = statistics.mean(H_Other)*1000000
S_Other_M = statistics.mean(S_Other) 
CCR_Ot = (str(S_Other_M/H_Other_M * 100))[:5]


Years = np.linspace(2018, 2022, 5)


fig, axs = plt.subplots(2,2,figsize=(15, 15))

fs = 12

axs_Am = axs[0,0].twinx()
axs[0,0].bar(Years, H_America, color = "lightgrey")
axs_Am.set_ylabel("Sales", fontsize = fs)
axs_Am.set_title("Americas (ACCR = " + CCR_Am + "%)", fontweight = "bold")
axs_Am.plot(Years, S_America, lw = 3)
axs_Am.set_ylim([0, 10000])
axs[0,0].set_ylim([0, 10])


axs_As = axs[0,1].twinx()
axs[0,1].bar(Years, H_Asia, color = "lightgrey")
axs_As.set_ylabel("Sales", fontsize = fs)
axs_As.set_title("Asia Pacific incl. China (ACCR = " + CCR_As + "%)", fontweight = "bold")
axs_As.plot(Years, S_Asia, lw = 3)
axs_As.set_ylim([0, 10000])
axs[0,1].set_ylim([0, 10])


axs_Eu = axs[1,0].twinx()
axs[1,0].bar(Years, H_Europe, color = "lightgrey")
axs_Eu.set_ylabel("Sales", fontsize = fs)
axs_Eu.set_title("Europe (ACCR = " + CCR_Eu + "%)", fontweight = "bold")
axs_Eu.plot(Years, S_Europe, lw = 3)
axs_Eu.set_ylim([0, 10000])
axs[1,0].set_ylim([0, 10])


axs_Ot = axs[1,1].twinx()
axs[1,1].bar(Years, H_Other, color = "lightgrey", label = "HNWIs (millions)")
axs_Ot.set_ylabel("Sales", fontsize = fs)
axs_Ot.set_title("Middle East, Africa & India (ACCR = " + CCR_Ot + "%)", fontweight = "bold")
axs_Ot.plot(Years, S_Other, lw = 3)
axs_Ot.set_ylim([0, 5000])
axs[1,1].set_ylim([0, 5])
axs[1,1].plot([-5,-4],[-4,-5], lw=3, label = "Sales")
axs[1,1].legend()


for i in [0, 1]:
    for j in [0, 1]:
        axs[i,j].set_box_aspect(0.9)
        axs[i,j].set_xlim([2017, 2023])
        axs[i,j].set_xticks([2018, 2019, 2020, 2021, 2022])
        axs[i,j].set_ylabel("Number of HNWIs (millions)", fontsize = fs)

'''
#plot1
col1 = "grey"
col2 = "darkgray"
col3 = "lightgrey"
col4 = "lightsteelblue"
col5 = "cadetblue"
col6 = "teal"
lw = 2

fig, axs = plt.subplots(1,1,figsize=(8, 8))
x_2018 = 0
x_2019 = 1
x_2020 = 2
x_2021 = 3
x_2022 = 4  
shift = 0.15

axs.bar(x_2018 - (shift*2.5), USA_2018, width = shift, color = col1)
axs.bar(x_2018 - (shift*1.5), China_2018, width = shift, color = col2)
axs.bar(x_2018 - (shift*0.5), Europe_2018, width = shift, color = col3)
axs.bar(x_2018 + (shift*0.5), Asia_Pacific_2018, width = shift, color = col4)
axs.bar(x_2018 + (shift*1.5), ME_Africa_India_2018, width = shift, color = col5)
axs.bar(x_2018 + (shift*2.5), UK_2018, width = shift, color = col6)

axs.bar(x_2019 - (shift*2.5), USA_2019, width = shift, color = col1)
axs.bar(x_2019 - (shift*1.5), China_2019, width = shift, color = col2)
axs.bar(x_2019 - (shift*0.5), Europe_2019, width = shift, color = col3)
axs.bar(x_2019 + (shift*0.5), Asia_Pacific_2019, width = shift, color = col4)
axs.bar(x_2019 + (shift*1.5), ME_Africa_India_2019, width = shift, color = col5)
axs.bar(x_2019 + (shift*2.5), UK_2019, width = shift, color = col6)

axs.bar(x_2020 - (shift*2.5), USA_2020, width = shift, color = col1)
axs.bar(x_2020 - (shift*1.5), China_2020, width = shift, color = col2)
axs.bar(x_2020 - (shift*0.5), Europe_2020, width = shift, color = col3)
axs.bar(x_2020 + (shift*0.5), Asia_Pacific_2020, width = shift, color = col4)
axs.bar(x_2020 + (shift*1.5), ME_Africa_India_2020, width = shift, color = col5)
axs.bar(x_2020 + (shift*2.5), UK_2020, width = shift, color = col6)

axs.bar(x_2021 - (shift*2.5), USA_2021, width = shift, color = col1)
axs.bar(x_2021 - (shift*1.5), China_2021, width = shift, color = col2)
axs.bar(x_2021 - (shift*0.5), Europe_2021, width = shift, color = col3)
axs.bar(x_2021 + (shift*0.5), Asia_Pacific_2021, width = shift, color = col4)
axs.bar(x_2021 + (shift*1.5), ME_Africa_India_2021, width = shift, color = col5)
axs.bar(x_2021 + (shift*2.5), UK_2021, width = shift, color = col6)

axs.bar(x_2022 - (shift*2.5), USA_2022, width = shift, color = col1, label = "Americas")
axs.bar(x_2022 - (shift*1.5), China_2022, width = shift, color = col2, label = "China")
axs.bar(x_2022 - (shift*0.5), Europe_2022, width = shift, color = col3, label = "Europe")
axs.bar(x_2022 + (shift*0.5), Asia_Pacific_2022, width = shift, color = col4, label = "Asia Pacific")
axs.bar(x_2022 + (shift*1.5), ME_Africa_India_2022, width = shift, color = col5, label = "Middle East, Africa & India")
axs.bar(x_2022 + (shift*2.5), UK_2022, width = shift, color = col6, label = "United Kingdom")

axs2 = axs.twinx()
axs2.plot([0,1,2,3,4], Revenue, lw = lw, color = "red")
axs2.scatter([0,1,2,3,4], Revenue, color = "red")
axs2.set_ylabel("Revenue (£ Billion)", fontsize = 14)
axs.plot([0,1], [-10, -10], color = "red", label = "Revenue") #for legend



axs.set_xlabel("Year", fontsize = 14)
axs.set_ylabel("Sales", fontsize = 14)
axs.set_xticks([0, 1, 2, 3, 4])
axs.set_xticklabels(["2018", "2019","2020","2021", "2022"])
axs2.set_yticks(np.linspace(0, 3, 7))
axs.legend(fontsize = 8)
axs.set_box_aspect(0.5)
axs.set_ylim([0, 5500])
'''

