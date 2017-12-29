This repo contains `Dockerfile`s for several Linux distributions to compile and package the Monetaryunit (MUE) wallet. It creates two packages: the CLI (`monetaryunit-wallet`) and the QT5 (`monetaryunit-wallet-qt5`) client.

# Howto
This example contains the steps to build Debian Stretch (v9) packages.

1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-monetaryunit-builder`
1. `cd docker-monetaryunit-builder/debian/stretch`
1. `docker build -t mue-debian9:1.0.3.2-1 .`
1. Wait for iiiiiit ... this entire build takes around 15 minutes on my Intel i5-6300U:
```
docker build -t mue-debian9:1.0.3.2 .  0.41s user 0.24s system 0% cpu 15:11.16 total
```
1. `docker volume create --name monetaryunit_packages`
1. `docker run mue-debian9:1.0.3.2-1 -v monetaryunit_packages:/monetaryunit`
1. the packaged binaries are in `/var/lib/docker/volumes/mue-debian9/_data/debian9`
1. install the package(s) on your host:
    1. `dpkg -i /var/lib/docker/volumes/mue-debian9/_data/debian9/monetaryunit-wallet-1.0.3.2-1-debian_stretch-amd64.deb`
    1. `dpkg -i /var/lib/docker/volumes/mue-debian9/_data/debian9/monetaryunit-wallet-qt5-1.0.3.2-1-debian_stretch-amd64.deb`
    1. `apt -f install` in case you're missing dependencies

# Build parameters
You can specify the number of CPUs `make` should use for compilation. If nothing is specified (default), all of the detected CPUs will be used. To change this, use the `--build-args NUMCPU` option, e.g. 

```
docker build --build-args NUMCPU=3 -t mue-debian9:1.0.3.2 .
```

# Todo
1. Generate dependencies in `DEBIAN/control` and `PKGBUILD` automatically after compilation.
1. Add RPM based distros

# Donations
My MUE address is 7obzc8c7GYfNuFotKNBoKtricCwP25XEk6. Feel free to send some over, or not, it's entirely up to you!
