FROM ubuntu:latest

RUN apt-get update -y && apt-get upgrade -y && apt-get install python3-pip -y
RUN apt-get install python3 -y
RUN apt-get install libpq-dev -y 
RUN apt-get install libgl1 -y
RUN apt-get install libglib2.0-0 -y
RUN pip install gunicorn
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app


