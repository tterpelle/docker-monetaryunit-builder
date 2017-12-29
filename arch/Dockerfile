FROM archlinux/base

ARG NUMCPU=-1

ENV DISTRO "arch"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"
ENV BDB_SRCDIR "$DISTRO_DIR/bdb/src"
ENV BDB_TGTDIR "$DISTRO_DIR/bdb/build"
ENV BDB_VERSION "4.8.30"
ENV BDB_URL "http://download.oracle.com/berkeley-db/db-$BDB_VERSION.tar.gz"
ENV MUE_SRCDIR "$DISTRO_DIR/mue/src"
ENV MUE_CLI_TGTDIR "$DISTRO_DIR/mue/build"
ENV MUE_GUI_TGTDIR "$DISTRO_DIR/mue/build-gui"
ENV MUE_URL "https://github.com/muecoin/MUECore.git"
ENV MUE_VERSION "1.0.3.2"

## update pacman and create normal user for package build
RUN pacman -Syu --noconfirm && \
## install dependencies
    pacman -S --noconfirm base-devel \
                    boost \
                    git \
                    libevent \
                    miniupnpc \
                    protobuf \
                    qrencode \
                    qt5-base \
                    qt5-tools \
                    tar \
                    wget \
                    zeromq && \
    mkdir -p $TOP_DIR && \
    useradd -s /bin/bash -d $DISTRO_DIR -m build && \
    echo 'build ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers && \
    # Enable ALL CPUs for compiling
    if [ $NUMCPU -lt 1 ]; then NUMCPU=$(lscpu | grep '^CPU(s):' | awk '{ print $2 }'); fi && \
    sed -i -e "s;#MAKEFLAGS=.*;MAKEFLAGS=-j$NUMCPU;" /etc/makepkg.conf && \
    # Set path for built packages
    sed -i -e "s;#PKGDEST=.*;PKGDEST=$TOP_DIR/$DISTRO;" /etc/makepkg.conf

## Install Yaourt
RUN su -c "git clone https://aur.archlinux.org/package-query.git && \
          cd package-query && \
          makepkg -si --noconfirm && \
          cd .. && \
          git clone https://aur.archlinux.org/yaourt.git && \
          cd yaourt && \
          makepkg -si --noconfirm && \
          cd .." - build
#
## create all the dirs
RUN for i in $BDB_SRCDIR $BDB_TGTDIR $MUE_SRCDIR $MUE_CLI_TGTDIR $MUE_GUI_TGTDIR $MUE_GUI_TGTDIR/usr/bin; do mkdir -p ${i}; done && \
    chown -R build:build $DISTRO_DIR && \
# Set path for built packages
    sed -i -e "s;#EXPORT=0\(.*\);EXPORT=1\1;" /etc/yaourtrc

COPY PKGBUILD $MUE_SRCDIR

## build libdb-dev v4.8 from source and install it
RUN su -c "yaourt -Sy --noconfirm db4.8" - build

## build the packages from PKGBUILD
RUN su -c "cd $MUE_SRCDIR && \
          makepkg -si --noconfirm" - build

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh", "arch", "pkg.tar.xz" ]
