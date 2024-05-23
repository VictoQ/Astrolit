# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY app/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the app directory into the container at /app
COPY app/ .

# Expose port 8501 to the outside world
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]