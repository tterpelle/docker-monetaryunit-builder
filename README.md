This repo contains `Dockerfile`s for several Linux distributions to compile and package the Monetaryunit (MUE) wallet. It creates two packages: the CLI (`monetaryunit-wallet`) and the QT5 (`monetaryunit-wallet-qt5`) client.

# Howto
This example contains the steps to build Debian Stretch (v9) packages.

1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-monetaryunit-builder`
1. `cd docker-monetaryunit-builder/debian/stretch`
1. `docker build -t mue:debian9 .`
1. Wait for iiiiiit ... this entire build takes around 15 minutes on my Intel i5-6300U with all cores used.
1. `docker volume create --name monetaryunit_packages`
1. `docker run -v monetaryunit_packages:/packages mue:debian9`
1. the packaged binaries are in `/var/lib/docker/volumes/monetaryunit_packages/_data/debian9`
1. install the package(s) on your host:
    1. `dpkg -i /var/lib/docker/volumes/monetaryunit_packages/_data/debian9/monetaryunit-wallet*.deb`
    1. `apt -f install` in case you're missing dependencies

# Build all packages in one go
```
git clone https://github.com/tterpelle/docker-monetaryunit-builder &&
cd docker-monetaryunit-builder &&
docker volume create --name monetaryunit_packages &&
for i in $(find -name 'Dockerfile')
do
  _DIRNAME=$(dirname ${i})
  _DISTRO=$(grep " DISTRO " ${i} | cut -f2 -d\")
  cd ${_DIRNAME}
  docker build -t mue:${_DISTRO} . &&
  docker run -v monetaryunit_packages:/packages mue:${_DISTRO}
  cd -
done
```
# Installation notes

## CentOS / Red Hat Enterprise Linux 7
Make sure you install the `epel-release` package first. After that you can install the MUE wallet with
```
yum localinstall monetaryunit-wallet*.rpm
```

# Donations
My MUE address is 7obzc8c7GYfNuFotKNBoKtricCwP25XEk6. Feel free to send some over, or not, it's entirely up to you!
