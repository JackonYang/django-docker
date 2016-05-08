# -*- coding:utf-8 -*-
import time
import random

from django.conf import settings
from django_redis import get_redis_connection


url = 'http://jackon.me'

_conn = get_redis_connection("default")


def wait(f):
    lock_name = 'crawler-http-lock'

    def _wrap_func(*args, **kwargs):
        t = _conn.ttl(lock_name)
        if t > 0:
            print 'sleep %s second' % t
            time.sleep(t)

        n_t = int(random.uniform(settings.DELAY_BOTTOM, settings.DELAY_TOP))
        _conn.setex(lock_name, n_t, 'locking')
        return f(*args, **kwargs)
    return _wrap_func


@wait
def fetch():
    print 'fetch %s' % url


def run():
    """ entry point of runscript

    """
    while True:
        fetch()
