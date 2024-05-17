# Base image
FROM python:3.9-slim

# Set the working directory in the Docker container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

EXPOSE 5000

RUN python3 main.py create_db

# Command to execute when the container starts
CMD ["python3", "main.py"]
