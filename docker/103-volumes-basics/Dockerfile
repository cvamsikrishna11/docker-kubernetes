FROM python:3.9-slim

# Install Flask
RUN pip install Flask

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app to the container
COPY app.py /app/

# Tell Docker to expose port 5000
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
