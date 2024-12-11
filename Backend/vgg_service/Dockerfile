# Use an official Python image as the base image
FROM python:3.9-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (for TensorFlow, etc.)
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt first to cache dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest for testing (optional, if tests are to be run in the container)
RUN pip install --no-cache-dir pytest

# Copy the entire Flask application into the container
COPY . .

# Expose the port the app will run on (default is 5000)
EXPOSE 5000

# Set environment variable to indicate Flask is in production
ENV FLASK_ENV=production

# Ensure the shared volume is accessible to the application
ENV MODEL_PATH=/app/models/vgg19_music_genre_classification.h5

# Command to run the Flask application
CMD ["python", "app.py"]
