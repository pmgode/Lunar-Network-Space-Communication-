import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv(
    r'D:\IMPORTANT\OMNET++\omnetpp-6.0.2-windows-x86_64\omnetpp-6.0.2\samples\final_task\results\HTTP_Interarrival\http_clients_interarrivaltime_warmup.csv',
    header=0, names=['time', 'bytes'])

# Convert the 'Time' column to numeric
df['time'] = pd.to_numeric(df['time'])

# Calculate interarrival times
df['InterarrivalTime'] = df['time'].diff()

# Drop rows with NaN in 'InterarrivalTime'
df = df.dropna(subset=['InterarrivalTime'])

# Convert interarrival times to milliseconds
df['InterarrivalTime_ms'] = df['InterarrivalTime'] * 1000

# Define bin width and create bins in milliseconds
bin_width = 5  # Bin width in milliseconds
max_value = 300  # Maximum value in milliseconds
bin_edges = np.arange(0, max_value + bin_width, bin_width)

# Calculate histogram data
hist_data, _ = np.histogram(df['InterarrivalTime_ms'], bins=bin_edges)

# Calculate mean interarrival time
mean_interarrival_time = df['InterarrivalTime_ms'].mean()

# Plot histogram with customized x-axis and y-axis
plt.figure(figsize=(12, 6))  # Increase the size for better visibility
plt.hist(df['InterarrivalTime_ms'], bins=bin_edges, edgecolor='black', alpha=0.7)
plt.title('Interarrival Time for HTTP Client (Warmup-period = 10s)')
plt.xlabel('Interarrival Time (milliseconds)')
plt.ylabel('Frequency (logarithm)')

# Add a vertical line for the mean
plt.axvline(mean_interarrival_time, color='red', linestyle='dashed', linewidth=1.5,
            label=f'Mean: {mean_interarrival_time:.2f} ms')

# Add text annotation for the mean
plt.text(mean_interarrival_time + 10, hist_data.max() * 0.7, f'Mean: {mean_interarrival_time:.2f} ms', color='red')

# Customize x-axis ticks with smaller step size
tick_step_size_x = 25
tick_positions_x = np.arange(0, max_value + tick_step_size_x, tick_step_size_x)
plt.xticks(ticks=tick_positions_x)

# Set y-axis to logarithmic scale
plt.yscale('log')

# Set x-axis and y-axis limits
plt.xlim(0, max_value)  # Ensure x-axis covers the data range
plt.ylim(1, hist_data.max() * 1.1)  # Set y-axis limits for better visibility on log scale

plt.grid(True, ls="--")  # Grid for both major and minor ticks
plt.show()
