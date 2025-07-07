def format_timestamp(timestamp):
    """Format a timestamp into a readable string."""
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def log_message(message, level="INFO"):
    """Log a message with a specified log level."""
    levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    if level not in levels:
        raise ValueError("Invalid log level")
    print(f"{format_timestamp(datetime.now())} - {level}: {message}")

def calculate_average(data):
    """Calculate the average of a list of numbers."""
    if not data:
        return 0
    return sum(data) / len(data)

def validate_sensor_data(sensor_data):
    """Validate sensor data to ensure it meets expected criteria."""
    if not isinstance(sensor_data, (list, tuple)) or len(sensor_data) != 3:
        raise ValueError("Sensor data must be a list or tuple of three values (temp, vibration, pressure)")
    return True

def extract_unit_name(unit):
    """Extract and format the unit name from a given input."""
    return unit.strip().title() if isinstance(unit, str) else "Unknown Unit"