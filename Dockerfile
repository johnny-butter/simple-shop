# Pull python 3.6 image from docker hub
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev -y

RUN mkdir /current
WORKDIR /current

RUN pip install pip -U

COPY . /current/

RUN pip install -r requirements.txt
