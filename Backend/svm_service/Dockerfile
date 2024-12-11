# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set environment variables for non-interactive installation
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt


# Install pytest and any other testing tools
RUN pip install --no-cache-dir pytest

# Expose port 5001 for the Flask app
EXPOSE 5001

# Define the command to run the app
CMD ["python", "app.py"]
