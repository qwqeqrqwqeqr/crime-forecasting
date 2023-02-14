###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

WORKDIR /
COPY . /

RUN chmod 644 /build/run/*
RUN chmod 644 /build/utils/move_file_by_month.sh
RUN chmod 644 /build/utils/move_file_by_year.sh
RUN chmod 777 /build/utils/cron.sh
RUN mv /build/run/*  /
RUN mv /build/utils/move_file_by_month.sh  /
RUN mv /build/utils/move_file_by_year.sh  /


RUN touch /log/report.log
RUN touch /log/hangang.log
RUN touch /log/tourist.log
RUN touch /log/subway.log
RUN touch /log/congestion.log
RUN touch /log/danger_index.log

RUN chmod 777 /log/*

###############################################
# DB_ENV (DB_PORT는 ''붙이지 말 것)
###############################################
ENV DB_NAME='NAME'
ENV DB_HOST='0.0.0.0'
ENV DB_PASSWORD='password'
ENV DB_PORT=1111
ENV DB_USER='user'


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
RUN apt-get install -y locales git
# Locale
RUN localedef -f UTF-8 -i ko_KR ko_KR.UTF-8
ENV LC_ALL ko_KR.UTF-8
ENV PYTHONIOENCODING=utf-8
RUN update-locale LANG=ko_KR.UTF-8

RUN touch database.ini
RUN echo "[database]\nDB_NAME =${DB_NAME} \nDB_HOST =${DB_HOST} \nDB_PASSWORD =${DB_PASSWORD} \nDB_PORT =${DB_PORT} \nDB_USER =${DB_USER} " > database.ini
RUN mv database.ini ./app/database/config/

###############################################
# setting cron
###############################################
RUN apt-get install -y cron
RUN cron
RUN /bin/sh /build/utils/cron.sh
###############################################
# setting python
###############################################
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt


RUN python3 -m unittest /test/validator_test.py
###############################################
#  Entry Point
###############################################
ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]