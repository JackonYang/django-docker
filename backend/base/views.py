# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    return Response('hello, django startup')
