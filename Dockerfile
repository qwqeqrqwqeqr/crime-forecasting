###############################################
# version
###############################################
FROM python:3.9.16
FROM ubuntu:20.04

WORKDIR /seoul


COPY . /seoul

###############################################
# env
###############################################

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

###############################################
# install base tool
###############################################

RUN apt update
RUN apt-get install -y libpq-dev python-dev
RUN apt-get install -y vim
RUN apt-get install -y tzdata


###############################################
# set cron
###############################################
RUN apt-get install -y cron

###############################################
# install python package
###############################################
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r  requirements.txt



###############################################
#  Entry Point
###############################################
RUN chmod 777 /seoul/build/cron/cron.sh
ENTRYPOINT ["/seoul/build/cron/cron.sh"]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]
#ENTRYPOINT [""]