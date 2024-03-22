# Use the official Python 3.10 image as base
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . /app/

# Copy the test and server startup script
COPY docker-entrypoint.sh /app/

# Run the tests and start the server if tests pass
CMD ["./docker-entrypoint.sh"]