# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.8.0-alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=fizzbuzz Version=0.0.1
EXPOSE 5000

# set work directory
WORKDIR /fizzbuzz 

# copy project
COPY . /fizzbuzz

# set environment variables
# Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    mariadb-dev \
    python3-dev \
    postgresql-dev \
    ;

RUN apk add --no-cache mysql-client


# Using pip:
RUN pip install -r requirements.txt 

ENTRYPOINT ["mysql"]
