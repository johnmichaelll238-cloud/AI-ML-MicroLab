import numpy as np
from data import t_matrix
from model import (detect_anomalies, calculate_Z_scores)

z_scores = calculate_Z_scores(t_matrix)
anomalies = detect_anomalies(t_matrix)
mean = np.mean(t_matrix)
std_dev = np.std(t_matrix)
print("Mean:")
print(mean)
print("Standard deviation:")
print(std_dev)
print("Traffic Matrix:")
print(t_matrix)
print("\nZ-score Matrix:")
print(z_scores)

print("\nAnomalies:")
print(anomalies)