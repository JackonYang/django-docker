# -*- coding:utf-8 -*-
import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")

current_dir = os.path.dirname(__file__)
if current_dir not in sys.path:
    sys.path.append(current_dir)

application = get_wsgi_application()
