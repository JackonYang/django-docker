#!/bin/bash

cd `dirname $0`

# render nginx config file
sudo python render.py 

# collect static files
cd ../backend
rm -rf static
python manage.py collectstatic

sudo nginx -s reload
