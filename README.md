This repo contains `Dockerfile`s for several Linux distributions to compile and package the Monetaryunit (MUE) wallet. It creates two packages: the CLI (`monetaryunit-wallet`) and the QT5 (`monetaryunit-wallet-qt5`) client.

# Howto
This example contains the steps to build Debian Stretch (v9) packages. 

1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-monetaryunit-builder`
1. `cd docker-monetaryunit-builder/debian/stretch`
1. `docker build -t mue-debian9:1.0.3.2-1 .`
1. Wait for iiiiiit ... this entire build took around 15 minutes on my Intel i5-6300U:
```
docker build -t mue-debian9:1.0.3.2 .  0.41s user 0.24s system 0% cpu 15:11.16 total
```
1. `docker run -it mue-debian9:1.0.3.2-1 /bin/bash` and copy the container's ID (e.g. `12345689abc`)
1. in a different terminal, copy the `.deb` files out of the container:
    1. `docker cp 12345689abc:/monetaryunit/monetaryunit-wallet-1.0.3.2-1-debian_squeeze-amd64.deb .`
    1. `docker cp 12345689abc:/monetaryunit/monetaryunit-wallet-qt5-1.0.3.2-1-debian_squeeze-amd64.deb .`
1. install the package(s) on your host:
    1. `dpkg -i monetaryunit-wallet-1.0.3.2-1-debian_squeeze-amd64.deb`
    1. `dpkg -i monetaryunit-wallet-qt5-1.0.3.2-1-debian_squeeze-amd64.deb`

# Todo
1. find a better way to get the `.deb`s out of the container
1. add support for building for other distributions, starting with deb derivatives likes Ubuntu

# Donations
My MUE address is 7obzc8c7GYfNuFotKNBoKtricCwP25XEk6. Feel free to send some over, or not, it's entirely up to you!
