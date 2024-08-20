"""
This python file is used to read the trace file and validate its statistical behaviour" 
"""

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Defining the file path
trace_file = 'Final_Task/trace_file.txt'

# Reading the file into a list
with open(trace_file, 'r') as file:
    values = [float(line.strip()) for line in file]

# Converting the list to a pandas DataFrame for easier analysis
data = pd.DataFrame(values, columns=['reading_time'])

# Extracting reading times
reading_times = data['reading_time']

print('mean: ', np.mean(reading_times))

# Fitting the exponential distribution to the data
lambda_est = 1 / np.mean(reading_times)

# Scipy to get the parameters (loc, scale)
loc, scale = stats.expon.fit(reading_times, floc=0)  # fixing loc=0 for negative exponential

# Defines the negative exponential distribution with the fitted parameter
negative_exponential = stats.expon(scale=scale)

# Defines the number of bins
num_bins = 10

# Defines the bins for the histogram
bins = np.linspace(reading_times.min(), reading_times.max(), num_bins + 1)

# Calculates observed frequencies
observed_frequencies, _ = np.histogram(reading_times, bins)

# Calculates expected frequencies assuming a negative exponential distribution
expected_frequencies = []
for i in range(len(bins) - 1):
    expected_frequency = len(reading_times) * (negative_exponential.cdf(bins[i+1]) - negative_exponential.cdf(bins[i]))
    expected_frequencies.append(expected_frequency)

expected_frequencies = np.array(expected_frequencies)

# Calculates the Chi-Squared statistic
chi_squared_statistic = ((observed_frequencies - expected_frequencies) ** 2 / expected_frequencies).sum()

# Degrees of freedom: number of bins - 1 - number of estimated parameters (scale in this case)
dof = num_bins - 1 - 1

# Calculates the p-value
p_value = 1 - stats.chi2.cdf(chi_squared_statistic, dof)

print(f"Chi-Squared Statistic: {chi_squared_statistic}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p_value}")

if p_value > 0.05:
    print("Data follows the exponential distribution.")
else:
    print("The null hypothesis is rejected; data does not follow the exponential distribution.")


# Generates values for the fitted distribution
x = np.linspace(reading_times.min(), reading_times.max(), 100)
pdf = negative_exponential.pdf(x)

# Plots histogram of the data and the fitted distribution
plt.hist(reading_times, bins=30, density=True, alpha=0.6, color='g', label='Data')
plt.plot(x, pdf, 'k', linewidth=2, label=f'Fitted Exponential\nLambda={1/scale:.2f}')
plt.title('Exponential Fit')
plt.xlabel('Reading Times (in seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.show()