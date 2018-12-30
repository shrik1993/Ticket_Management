FROM python:3.5

MAINTAINER Shrikant Chaudhari "shrikantchaudhari6548@gmail.com"

EXPOSE 9090

# Update OS
RUN apt-get update -y

# Install pip, python essentials
#RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip

# Copy current flask application in container
COPY requirements.txt /opt/flask_app/requirements.txt
WORKDIR /opt/flask_app
# Install required python packages
RUN pip install -r requirements.txt

COPY uwsgi.ini /opt/flask_app/uwsgi.ini

COPY . /opt/flask_app

#ENTRYPOINT ["python"]
# Run Flask application using uwsgi server
ENTRYPOINT ["bash", "dbmigrate.sh"]
#CMD ["uwsgi", "--ini", "uwsgi.ini"]
