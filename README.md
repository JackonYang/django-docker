# Django-Docker

[docker installation doc](doc/docker-installation.md)

## Development Environment

#### building docker images

download the lastest code and run

```bash
$ cd /path/to/canting
$ docker-compose up
```

3 images are expected:

- Python 2.7 / Django 1.8
- Redis 3.0.7
- MySQL 5.7

#### Backend Database Migration

```bash
$ docker-compose run backend /bin/bash
$ python manage.py migrate
$ python manage.py createsuperuser  --username=admin --email=i@jackon.me
# interactive input and output
# Password: (123)
# Password (again): (123)
# Superuser created successfully.
```

#### Testing

1. Backend basic testing

    - operation: visit `127.0.0.1:8000` in browser
    - expection: home page is opened

2. Redis Connection

    - operation: visit `127.0.0.1:8000` in browser, and refresh it 
    - expection: `I have been seen xxx times.` is shown and xxx increase by refreshing
3. MySQL Connection

    - operation: visit `127.0.0.1:8000/admin` in browser, login in by username / password
    - expection: logined and admin page is opened.


## Production Environment
