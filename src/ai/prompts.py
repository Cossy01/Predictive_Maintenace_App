def generate_failure_analysis_prompt(sensor_data, equipment_type, unit_name, unit_characteristics):
    return f"""
    You are an industrial maintenance expert analyzing equipment sensor data.
    Be specific, technical, and actionable in your recommendations.
    Focus on safety, root causes, and immediate actions needed.

    EQUIPMENT ANALYSIS REQUEST:
    Equipment: {unit_name} ({equipment_type})

    CURRENT READINGS:
    - Temperature: {sensor_data[0]:.1f}°C
    - Vibration: {sensor_data[1]:.2f} m/s²
    - Pressure: {sensor_data[2]:.1f} psi

    UNIT CHARACTERISTICS:
    - Temperature drift: {unit_characteristics['temp_drift']:+.1f}°C from baseline
    - Vibration drift: {unit_characteristics['vib_drift']:+.2f} m/s² from baseline
    - Pressure drift: {unit_characteristics['press_drift']:+.1f} psi from baseline

    Provide analysis in this exact format:
    TECHNICAL: [Detailed technical analysis for maintenance team]
    OPERATOR: [Simple instructions for equipment operator]
    """

def generate_maintenance_prediction_prompt(sensor_data, unit_name, unit_characteristics):
    return f"""
    You are a predictive maintenance specialist.
    Consider equipment age, usage patterns, and current condition.
    Provide realistic timeframes and clear reasoning.

    MAINTENANCE SCHEDULING REQUEST:
    Equipment: {unit_name}
    Current baseline prediction: {sensor_data['baseline_prediction']} days

    UNIT PROFILE:
    - Temperature trend: {unit_characteristics['temp_drift']:+.1f}°C deviation
    - Vibration trend: {unit_characteristics['vib_drift']:+.2f} m/s² deviation  
    - Pressure trend: {unit_characteristics['press_drift']:+.1f} psi deviation

    Based on this equipment's profile, should maintenance be:
    - ACCELERATED (more urgent than {sensor_data['baseline_prediction']} days)
    - STANDARD (keep {sensor_data['baseline_prediction']} days)
    - EXTENDED (can wait longer than {sensor_data['baseline_prediction']} days)

    Respond with: "ACCELERATED X" or "STANDARD" or "EXTENDED X" (where X is recommended days)
    Then explain your reasoning briefly.
    """

def generate_performance_insights_prompt(unit_name, unit_characteristics, sensor_data):
    return f"""
    You are an equipment performance analyst.
    Provide brief, actionable insights about equipment health.
    Focus on trends, risks, and operational recommendations.

    PERFORMANCE INSIGHTS REQUEST:
    Unit: {unit_name}

    CHARACTERISTICS:
    - Temperature: {unit_characteristics['temp_drift']:+.1f}°C from standard
    - Vibration: {unit_characteristics['vib_drift']:+.2f} m/s² from standard
    - Pressure: {unit_characteristics['press_drift']:+.1f} psi from standard

    LATEST READINGS:
    - Temperature: {sensor_data[-1][0]:.1f}°C
    - Vibration: {sensor_data[-1][1]:.2f} m/s²
    - Pressure: {sensor_data[-1][2]:.1f} psi

    Provide exactly 3 insights in this format:
    PERFORMANCE: [Brief performance summary]
    MAINTENANCE: [Maintenance recommendation]
    OPERATION: [Operational tip]
    """