###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

WORKDIR /seoul


COPY . /seoul
###############################################
# install base
###############################################

RUN apt update
RUN apt-get install -y libpq-dev python-dev
RUN apt-get install -y vim


###############################################
# set cron
###############################################


###############################################
# install python package
###############################################
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt



###############################################
#  Entry Point
###############################################
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]