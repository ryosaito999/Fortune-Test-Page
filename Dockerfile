# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

#Copy Files in flask App
RUN mkdir templates
COPY templates/ ./templates
COPY config.py .
COPY fortune.py .

EXPOSE 5000/tcp

# command to run on container start
CMD [ "python", "./fortune.py" ]