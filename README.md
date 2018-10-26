This repo contains `Dockerfile`s for several Linux distributions to compile and package the Monetaryunit (MUE) wallet. It creates two packages: the CLI (`monetaryunit-wallet`) and the QT5 (`monetaryunit-wallet-qt5`) client.

# Howto
This example contains the steps to build Debian Stretch (v9) packages.

1. [install Docker](https://docs.docker.com/engine/installation/linux/docker-ce/debian/)
1. clone the repo: `git clone https://github.com/tterpelle/docker-monetaryunit-builder`
1. `cd docker-monetaryunit-builder/debian/stretch`
1. `docker build -t mue:debian9 .`
1. Wait for iiiiiit ... this entire build takes around 15 minutes on my Intel i5-6300U with all cores used.
1. `docker volume create --name monetaryunit_packages` (only needed once)
1. `docker run -v monetaryunit_packages:/packages mue:debian9`
1. the packaged binaries are in `/var/lib/docker/volumes/monetaryunit_packages/_data/debian9`
1. install the package(s) on your host:
    1. `dpkg -i /var/lib/docker/volumes/monetaryunit_packages/_data/debian9/monetaryunit-wallet*.deb`
    1. `apt -f install` in case you're missing dependencies

# Build all packages in one go
Run the `build_all.sh` script. This will take quite some time to finish!

# Installation notes

## ArchLinux
The build fails with `boost-1.66` and `boost-libs-1.66` packages. If you revert to version 1.65 it works fine. I've created [a bug report](https://github.com/muecoin/MUECore/issues/3).

## CentOS / Red Hat Enterprise Linux 7
Make sure you install the `epel-release` package first. After that you can install the MUE wallet with
```
yum localinstall monetaryunit-wallet-2.0.2-1.x86_64.rpm monetaryunit-wallet-qt5-2.0.2-1.x86_64.rpm
```
## Debian / Ubuntu
```
dpkg -i monetaryunit-wallet_2.0.2_amd64.deb monetaryunit-wallet-qt5_2.0.2_amd64.deb
apt -f install
```
## Fedora 27
```
dnf install monetaryunit-wallet-2.0.2-1.x86_64.rpm monetaryunit-wallet-qt5-2.0.2-1.x86_64.rpm
```

## Raspbian (Stretch) / `armhf` / Raspberry Pi 2 and up
```
dpkg -i monetaryunit-wallet_2.0.2_armhf.deb monetaryunit-wallet-qt5_2.0.2_armhf.deb
apt -f install
```

Note: these packages haven't been compiled from source. They are created from the binary release [mon-arm-linux-gnueabihf.tar.gz](https://github.com/muecoin/MUE/releases/tag/v2.0.2) by the Monetary Unit team.


# Donations
My MUE address is 7oEBoYVer3wCE3XqocXhWvNuHnLJFrY2fW. Feel free to send some over, or not, it's entirely up to you!
