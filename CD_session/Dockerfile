# Base image containing Python 3.10 on a lightweight Linux OS
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /flask-loan-app

# Copy the requirements file into the container
COPY artefacts/requirements.txt /flask-loan-app/requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the complete application into the container
COPY . /flask-loan-app

# Expose the application port
EXPOSE 9000

# Start the Flask application
CMD ["python", "-m", "flask", "--app", "Loan_app.py", "run", "--host=0.0.0.0", "--port=9000"]

# RUN commands execute only once while building the image.
# CMD executes every time a container is started from the image.