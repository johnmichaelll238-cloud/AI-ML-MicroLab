import numpy as np

def calculate_Z_scores(matrix):
    mean = np.mean(matrix)
    std_dev = np.std(matrix)
    z_scores = (matrix - mean)/std_dev
    return z_scores
def detect_anomalies(matrix, threshold = 2):
   z_scores = calculate_Z_scores(matrix)
   mask = np.abs(z_scores) > threshold
   return matrix[mask]