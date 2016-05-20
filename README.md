# Django-Docker


## Development Environment


#### One-command setup with Docker

[docker installation doc](doc/docker-installation.md)

download the lastest code, go into the src path and run

```bash
$ docker-compose build
```

3 images are expected:

- Python 2.7 / Django 1.8
- Redis 3.0.7
- MySQL 5.7


#### Environment without Docker

Required:

- Python 2.7
- Redis 3.0.7

download the lastest code, go into the src path and run

```bash
pip install -r requirements.txt
```


#### Backend Database Migration

use either MySQL or SQLite3


#### MySQL

Env-with-Docker uses MySQL by default

```bash
$ docker-compose run backend /bin/bash
$ python manage.py migrate
$ python manage.py createsuperuser  --username=admin --email=i@jackon.me
# interactive input and output
# Password: (123)
# Password (again): (123)
# Superuser created successfully.
```

#### SQLite3

Env-without-Docker uses MySQL by default

run script in src path

```bash
./install.sh
```


#### run dev server

- without docker:

    `./run.sh`
- docker:

    `docker-compose up`
- go into docker

    - go into docker: `docker-compose run backend /bin/bash`
    - run server: `./run.sh`


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


## Built-in Tools

#### run crawler:

```bash
$ python manage.py runscript crawler
```
