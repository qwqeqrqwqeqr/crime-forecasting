###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

RUN mkdir /seoul
WORKDIR /seoul
COPY . /seoul

RUN chmod 644 /seoul/build/run/*
RUN chmod 644 /seoul/build/utils/move_file_by_month.sh
RUN chmod 644 /seoul/build/utils/move_file_by_year.sh
RUN chmod 777 /seoul/build/utils/cron.sh
RUN mv /seoul/build/run/*  /seoul
RUN mv /seoul/build/utils/move_file_by_month.sh  /seoul
RUN mv /seoul/build/utils/move_file_by_year.sh  /seoul

###############################################
# DB_ENV
###############################################
ENV DB_NAME='이름입력'
ENV DB_HOST='호스트입력'
ENV DB_PASSWORD='패스워드입력'
ENV DB_PORT=1234'숫자로입력할것'
ENV DB_USER='유저입력'


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


RUN python3 -m unittest /seoul/test/validator_test.py
###############################################
#  Entry Point
###############################################
ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]