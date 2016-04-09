# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response
import socket

from django_redis import get_redis_connection


redis = get_redis_connection("default")
host = socket.gethostname()


@api_view(['GET'])
def home(request):
    key = 'test:hits'
    redis.incr(key)
    return Response('Hello World!'
                    'I have been seen %s times.'
                    'My Host name is %s.' % (redis.get(key), host))
