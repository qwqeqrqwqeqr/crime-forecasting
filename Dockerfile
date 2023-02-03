###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

RUN mkdir /seoul
WORKDIR /seoul
COPY . /seoul

RUN chmod 644 /seoul/build/run/*
RUN chmod 644 /seoul/build/utils/movefile.sh
RUN chmod 777 /seoul/build/utils/cron.sh
RUN mv /seoul/build/run/*  /seoul
RUN mv /seoul/build/utils/movefile.sh  /seoul

###############################################
# DB_ENV
###############################################
ENV DB_NAME='postgres'
ENV DB_HOST='121.131.185.164'
ENV DB_PASSWORD='ncyc0078'
ENV DB_PORT=5435
ENV DB_USER='ncyc'


###############################################
# install base tool
###############################################

RUN apt update
RUN apt-get install -y libpq-dev python-dev
RUN apt-get install -y vim
RUN apt-get install -y tzdata

######################################어########
# env
###############################################
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul
RUN export LANGUAGE=ko| \
    apt-get install -y language-pack-ko | \
    apt-get install -y locales | \
    localedef -f UTF-8 -i ko_KR ko_KR.UTF-8 | \
    locale-gen ko_KR.UTF-8 | \
    export LC_ALL=ko_KR.UTF-8 |LC_ALL=ko_KR.UTF-8 bash

RUN touch database.ini
RUN echo "[database]\nDB_NAME =$DB_NAME \nDB_HOST =$DB_HOST` \nDB_PASSWORD =$DB_PASSWORD` \nDB_PORT =$DB_PORT` \nDB_USER =$DB_USER`" > database.ini
RUN mv database.ini ./app/database/config/

###############################################
# setting cron
###############################################
RUN apt-get install -y cron
RUN cron
RUN /bin/sh /seoul/build/utils/cron.sh
###############################################
# setting python
###############################################
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt

RUN python3 -m unittest
###############################################
#  Entry Point
###############################################
ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]