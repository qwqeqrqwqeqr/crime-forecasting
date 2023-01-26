###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

WORKDIR /home/ncyc-admin/crime_forecasting/


COPY . .
###############################################
# install base
###############################################

RUN apt update
RUN apt-get install -y libpq-dev python-dev


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