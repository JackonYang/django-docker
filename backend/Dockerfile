# django APP
# do not operate database in APP's docker
# for there would be several apps, sharing one database
#
FROM daocloud.io/python:2.7
MAINTAINER jackon.me "i@jackon.me"

COPY . /backend
WORKDIR /backend

RUN pip install -r requirements.txt
