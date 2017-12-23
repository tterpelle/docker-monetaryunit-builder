This repo contains `Dockerfile`s for several Linux distributions to compile and package the Monetaryunit (MUE) wallet. It creates two packages: the CLI and the QT5 client.

# Howto
This example contains the steps to build Debian Stretch (v9) packages.
1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-monetaryunit-builder`
1. `cd docker-monetaryunit-builder/debian/stretch`
1. `docker build -t mue-debian9:1.0.3.2-1 .`
1. Wait for iiiiiit ...
1. `docker run -it mue-debian9:1.0.3.2-1 /bin/bash` and copy the container's ID (e.g. `12345689abc`)
1. in a different terminal, copy the `.deb` files out of the container: 
    1. `docker cp 12345689abc:/monetaryunit/monetaryunit-wallet-1.0.3.2-1-debian_squeeze-amd64.deb .`
    1. `docker cp 12345689abc:/monetaryunit/monetaryunit-wallet-1.0.3.2-1-qt5-debian_squeeze-amd64.deb .`
1. install the package(s): 
    1. `dpkg -i monetaryunit-wallet-1.0.3.2-1-debian_squeeze-amd64.deb`
    1. `dpkg -i monetaryunit-wallet-1.0.3.2-1-qt5-debian_squeeze-amd64.deb`

# Todo
1. find a better way to get the `.deb`s out of the container
1. add support for building for other distributions, starting with deb derivatives likes Ubuntu
