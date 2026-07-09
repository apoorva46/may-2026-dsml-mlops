FROM python:3.10-slim
#this contains OS + python 3.10 installed into it.

#Set the working directory in the container
WORKDIR /flask-loan-app 



##Copy the requirements file into the container
COPY artefacts/requirements.txt /flask-loan-app/requirements.txt 

#Install the dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt


#Copy the rest of the application code into the container
COPY . /flask-loan-app


#Make a port available to the world outside this container
CMD ["python", "-m", "flask", "--app", "Loan_app.py", "run", "--host=0.0.0.0", "--port=9000"]

#RUN COMMAND runs only once when the container is being built. 
#CMD COMMAND runs every time the container is started. 