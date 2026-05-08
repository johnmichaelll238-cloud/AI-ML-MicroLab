import numpy as np

def calculate_threshold(matrix):
    print("Threshold:")
    print(np.mean(matrix))
    return np.mean(matrix)
def detect_anomalies(matrix):
    threshold = calculate_threshold(matrix)
    return matrix[matrix > threshold]