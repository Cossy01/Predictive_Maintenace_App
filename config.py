# Configuration settings for the predictive maintenance application

# API configuration
API_CONFIG = {
    'endpoint': 'http://localhost:5000/api',
    'timeout': 10,
    'retries': 3
}

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'predictive_maintenance_db'
}

# AI model configuration
AI_MODEL_CONFIG = {
    'primary_model': 'gemma:2b',
    'backup_model': None,
    'fallback_model': None,
    'temperature': 0.3,
    'max_retries': 1
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'file': 'app.log',
    'format': '%(asctime)s - %(levelname)s - %(message)s'
}

# Other application settings
APP_SETTINGS = {
    'debug': True,
    'port': 5000,
    'host': '0.0.0.0'
}