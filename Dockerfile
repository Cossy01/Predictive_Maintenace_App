FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY src/ ./src/

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "src/app.py"]