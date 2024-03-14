FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements files
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application
COPY . /app

# Expose the application port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
