FROM dockerhub.nicleary.com/python:3.10.2-slim-buster

RUN apt update && apt upgrade -y

WORKDIR /demoapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# create an unprivledged user
RUN adduser --disabled-password --gecos '' app

COPY app/requirements.txt .
RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt
RUN mkdir /demoapp/app

COPY app/demo /demoapp/app/demo
WORKDIR /demoapp/app/demo