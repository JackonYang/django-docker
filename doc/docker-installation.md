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

Some DIFFERENCES from Linux

1. Because the Docker daemon uses Linux-specific kernel features,
    you can’t run Docker natively in OS X.
    Instead, you must use docker-machine to create and attach to a virtual machine (VM).
    This machine is a Linux VM that hosts Docker for you on your Mac.
2. the website is not available through 127.0.0.1,
    use VM IP instead.

e.g. VM name is `django-vm`

```bash
$ brew install docker
$ brew install Caskroom/cask/dockertoolbox
$ docker-machine create django-vm --driver virtualbox
# export env to configure your shell
$ eval $(docker-machine env django-vm)
# get ip of VM by vm name
$ docker-machine ip django-vm
```
