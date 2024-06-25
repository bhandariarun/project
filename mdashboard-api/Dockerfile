FROM python:3.10.12-slim-bullseye

# Set the working directory in the container
WORKDIR /mdashboard-api

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x entrypoint.sh

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run the application
ENTRYPOINT ["./entrypoint.sh"]