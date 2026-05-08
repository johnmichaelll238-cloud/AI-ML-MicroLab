from data import t_matrix
from model import detect_anomalies

anomalies = detect_anomalies(t_matrix)

print("Traffic Matrix:")
print(t_matrix)

print("\nAnomalies:")
print(anomalies)