from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(sensor_data, contamination=0.1):
    """
    Detect anomalies in sensor data using Isolation Forest.
    
    Parameters:
    - sensor_data: A 2D array-like structure where each row represents a reading
      and each column represents a different sensor.
    - contamination: The proportion of outliers in the data set.
    
    Returns:
    - An array of predictions where -1 indicates an anomaly and 1 indicates normal.
    """
    model = IsolationForest(contamination=contamination, random_state=42)
    predictions = model.fit_predict(sensor_data)
    return predictions

def detect_anomalies_with_threshold(sensor_data, thresholds):
    """
    Detect anomalies based on predefined thresholds for each sensor.
    
    Parameters:
    - sensor_data: A 2D array-like structure where each row represents a reading
      and each column represents a different sensor.
    - thresholds: A dictionary containing the threshold values for each sensor.
    
    Returns:
    - A list of boolean values indicating whether each reading is an anomaly.
    """
    anomalies = []
    for reading in sensor_data:
        is_anomaly = any(reading[i] > thresholds[i] for i in range(len(reading)))
        anomalies.append(is_anomaly)
    return anomalies

def preprocess_sensor_data(raw_data):
    """
    Preprocess raw sensor data for anomaly detection.
    
    Parameters:
    - raw_data: A list of raw sensor readings.
    
    Returns:
    - A 2D numpy array suitable for model input.
    """
    return np.array(raw_data)