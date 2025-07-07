from flask import Flask, request, jsonify
from src.data.sensors import SensorDataManager
from src.analysis.anomaly_detection import detect_anomalies
from src.analysis.maintenance_prediction import predict_maintenance
from src.visualization.charts import generate_charts
from src.visualization.gauges import create_gauges

app = Flask(__name__)

@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    data = SensorDataManager.get_latest_data()
    return jsonify(data)

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    sensor_data = request.json.get('sensor_data')
    anomalies = detect_anomalies(sensor_data)
    maintenance_prediction = predict_maintenance(sensor_data)
    return jsonify({
        'anomalies': anomalies,
        'maintenance_prediction': maintenance_prediction
    })

@app.route('/api/visualize', methods=['POST'])
def visualize_data():
    sensor_data = request.json.get('sensor_data')
    charts = generate_charts(sensor_data)
    gauges = create_gauges(sensor_data)
    return jsonify({
        'charts': charts,
        'gauges': gauges
    })

if __name__ == '__main__':
    app.run(debug=True)