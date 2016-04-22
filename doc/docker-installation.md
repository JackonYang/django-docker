# Docker Installation


## Required

- docker (1.10.0)

    [https://docs.docker.com/engine/installation/](https://docs.docker.com/engine/installation/)
- docker-compose (1.6.2)

    [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/)

## Installation

It differs between operation systems.

#### Ubuntu 14.04

install Docker and create Docker user group

```bash
$ sudo apt-get update
$ sudo apt-get install docker-engine
# Optional configurations
$ sudo groupadd docker
$ sudo usermod -aG docker ubuntu
# Log out and log back in.
# This ensures your user is running with the correct permissions.
```

install docker-compose by root

```
$ sudo -i
# mkdir -p /opt/bin
# curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
# chmod +x /opt/bin/docker-compose
# docker-compose  -v
docker-compose version 1.6.2, build 4d72027
```

#### CoreOS

Docker-engine is installed on CoreOS by default.

docker 1.10 requires CoreOS Alpha version

`/usr/local/bin/` is not writable by default, use `/opt/bin/` instead

```
$ sudo -i
# mkdir -p /opt/bin
# curl -L https://github.com/docker/compose/releases/download/1.6.2/docker-compose-`uname -s`-`uname -m` > /opt/bin/docker-compose
# chmod +x /opt/bin/docker-compose
# docker-compose  -v
docker-compose version 1.6.2, build 4d72027
```


#### Mac

TODO
