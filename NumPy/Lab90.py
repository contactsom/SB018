import numpy as np
from scipy import stats

data = np.array([10, 20, 30, 40, 50])

mean_val = np.mean(data)
median_val = np.median(data)
mode_val = stats.mode(data)
std_dev = np.std(data)
min_val = np.min(data)
max_val = np.max(data)
percentile_75 = np.percentile(data, 75)


print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")
print(f"Standard Deviation: {std_dev}")
print(f"Minimum: {min_val}")
print(f"Maximum: {max_val}")
print(f"75th Percentile: {percentile_75}")