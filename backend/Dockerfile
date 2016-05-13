# django APP
# do not operate database in APP's docker
# for there would be several apps, sharing one database
#
FROM daocloud.io/python:2.7
MAINTAINER jackon.me "i@jackon.me"


# python packages
RUN pip install --upgrade pip
RUN pip install django==1.8
RUN pip install django-grappelli==2.7.1

RUN pip install djangorestframework==3.3.2
# Markdown support for the browsable API.
RUN pip install markdown==2.3.1
RUN pip install django-filter==0.12.0

# http://djangothumbnails.com/
RUN pip install django-thumbs==0.4

# http://django-extensions-zh.readthedocs.io/
RUN pip install django-extensions==1.6.7

RUN pip install redis==2.10.5
RUN pip install django-redis==4.2.0
RUN pip install MySQL-python==1.2.5

RUN pip install uWSGI==2.0.13

COPY . /backend
WORKDIR /backend

RUN pip install -r requirements.txt
