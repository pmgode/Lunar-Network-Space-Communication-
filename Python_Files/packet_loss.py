"""
This python file is used to plot the packet loss rate for different scenarios as required 
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#Packets sent 
packets_sent = 2251

'''
Packets received for Video Conference with different active HTTP users
SS = Science Station
CS = Control Station
http_x_cs/ss = x is the number of active http users
'''
http_0_ss = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]
http_0_cs = [2248, 2247, 2247, 2247, 2250, 2247, 2250, 2248, 2250, 2248]

http_5_ss = [2239, 2242, 2241, 2247, 2244, 2216, 2241, 2230, 2246, 2244]
http_5_cs = [2248, 2249, 2250, 2245, 2246, 2249, 2247, 2244, 2248, 2250]

http_10_ss = [2217, 2233, 2241, 2242, 2236, 2172, 2238, 2209, 2242, 2244]
http_10_cs = [2249, 2249, 2248, 2246, 2244, 2250, 2244, 2245, 2249, 2248]

http_20_ss = [2209, 2234, 2228, 2240, 2218, 2155, 2217, 2159, 2242, 2233]
http_20_cs = [2249, 2250, 2245, 2249, 2247, 2250, 2245, 2249, 2250, 2246]

http_30_ss = [2182, 2225, 2223, 2239, 2207, 2120, 2204, 2176, 2232, 2227]
http_30_cs = [2249, 2249, 2251, 2249, 2243, 2250, 2246, 2250, 2250, 2247]

'''
Packets received for Video Conference with Different MSS
SS = Science Station
CS = Control Station
http_x_y_cs/ss = x is the number of active http users and y is the multiplicative factor of MSS which give receiver advertised window
'''
http_0_10_ss = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]
http_0_1000_ss = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]
http_1_1000_ss = [2250, 2249, 2249, 2245, 2248, 2246, 2250, 2247, 2248, 2247]
http_1_10_ss = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]

http_0_10_cs = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]
http_0_1000_cs = [2248, 2247, 2247, 2247, 2250, 2247, 2250, 2248, 2250, 2248]
http_1_1000_cs = [2248, 2248, 2247, 2246, 2248, 2246, 2248, 2247, 2249, 2251]
http_1_10_cs = [2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250]


# Function to calculate packet loss rate
def loss_percent_calc(arr):
    for i in range(len(arr)):
        arr[i] = ((packets_sent - arr[i])/ packets_sent) * 100

loss_percent_calc(http_0_ss)
loss_percent_calc(http_0_cs)
loss_percent_calc(http_5_ss)
loss_percent_calc(http_5_cs)
loss_percent_calc(http_10_ss)
loss_percent_calc(http_10_cs)
loss_percent_calc(http_20_ss)
loss_percent_calc(http_20_cs)
loss_percent_calc(http_30_ss)
loss_percent_calc(http_30_cs)

loss_percent_calc(http_0_10_cs)
loss_percent_calc(http_1_10_cs)
loss_percent_calc(http_0_1000_cs)
loss_percent_calc(http_1_1000_cs)

# Function to calculate the mean and interval
def confidence_interval(data, confidence=0.95):
    mean = np.mean(data)
    sem = stats.sem(data)  # Standard error of the mean
    interval = sem * stats.t.ppf((1 + confidence) / 2., len(data) - 1)
    return mean, interval

# Mean and Interval calculation from previous received packets array 
mean1, interval1 = confidence_interval(http_0_ss)
mean2, interval2 = confidence_interval(http_5_ss)
mean3, interval3 = confidence_interval(http_10_ss)
mean4, interval4 = confidence_interval(http_20_ss)
mean5, interval5 = confidence_interval(http_30_ss)

mean6, interval6 = confidence_interval(http_0_10_cs)
mean7, interval7 = confidence_interval(http_0_1000_cs)
mean8, interval8 = confidence_interval(http_1_10_cs)
mean9, interval9 = confidence_interval(http_1_1000_cs)

x_labels = ["0_10xMSS", "0_1000xMSS", "1_10xMSS", "1_1000xMSS"]
# means = [mean1, mean2, mean3, mean4, mean5]
# errors = [interval1, interval2, interval3, interval4, interval5]

means = [mean6, mean7, mean8, mean9]
errors = [interval6, interval7, interval8, interval9]

plt.figure(figsize=(10, 6))
plt.errorbar(x_labels, means, yerr=errors, fmt='o', capsize=5, capthick=2)
plt.bar(x_labels, means, yerr=errors, align='center', alpha=0.7, capsize=10, color=['blue', 'green', 'blue', "green"])
plt.title('Active Http Users vs Packet Loss Rate at Control Station [Repetition = 10, Sim Time = 100s, Warm-Up = 10s]')
plt.xlabel('Number of Http Users')
plt.ylabel('Packet Loss Rate')
handles = [plt.Rectangle((0,0),1,1, color='blue', alpha=0.7), 
           plt.Rectangle((0,0),1,1, color='green', alpha=0.7)]
labels = ['10 Times MSS', '1000 Times MSS']
plt.legend(handles, labels)
plt.grid(True)

plt.show()
