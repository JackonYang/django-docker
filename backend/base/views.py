# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django_redis import get_redis_connection


redis = get_redis_connection("default")


@api_view(['GET'])
def home(request):
    key = 'test:hits'
    redis.incr(key)
    return Response('Hello World! I have been seen %s times.' % redis.get(key))
