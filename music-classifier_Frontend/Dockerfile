# Use an official Node runtime as the base image
FROM node:20-alpine

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install Angular CLI and project dependencies
RUN npm install -g @angular/cli
RUN npm install

# Copy the entire project
COPY . .

# Expose the default Angular development port
EXPOSE 4200

# Command to run the application
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]