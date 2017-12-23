This is a `Dockerfile` that will compile and package the Monetaryunit (MUE) wallet for Debian 9 (Stretch). It creates two packages: the CLI and the QT5 client.

# Howto
1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-mue-debian9.git`
1. `cd docker-mue-debian9`
1. `docker build -t mue-debian9:1.0.3.2-1 .`
1. Wait for iiiiiit ...
1. `docker run -it mue-debian9:1.0.3.2-1 /bin/bash` and copy the container ID (e.g. `12345689abc`)
1. in a different terminal, copy the `.deb` files out of the container: 
    1. `docker cp 12345689abc:/mue/monetaryunit-wallet-1.0.3.2-1-amd64.deb .`
    1. `docker cp 12345689abc:/mue/monetaryunit-wallet-1.0.3.2-1-qt5-amd64.deb .`
1. install the package(s): 
    1. `dpkg -i monetaryunit-wallet-1.0.3.2-1-amd64.deb`
    1. `dpkg -i monetaryunit-wallet-1.0.3.2-1-qt5-amd64.deb`

# Todo
1. find a better way to get the `.deb`s out of the container
1. add support for building for other distributions, starting with deb derivatives likes Ubuntu
