FROM ubuntu:17.04

ENV TOP_DIR "/monetaryunit"
ENV BDB_SRCDIR "$TOP_DIR/bdb/src"
ENV BDB_TGTDIR "$TOP_DIR/bdb/build"
ENV BDB_VERSION "4.8.30"
ENV BDB_URL "http://download.oracle.com/berkeley-db/db-$BDB_VERSION.tar.gz"
ENV MUE_SRCDIR "$TOP_DIR/mue/src"
ENV MUE_CLI_TGTDIR "$TOP_DIR/mue/build"
ENV MUE_GUI_TGTDIR "$TOP_DIR/mue/build-gui"
ENV MUE_URL "https://github.com/muecoin/MUECore.git"
ENV MUE_VERSION "1.0.3.2"

COPY mue_cli_control /tmp
COPY mue_qt5_control /tmp

# update apt
RUN apt -q update && \
# install dependencies
    apt -qy install autoconf \
                   	bsdmainutils \
                    build-essential \
                    gawk \
                    gettext \
                    git \
                    libboost-all-dev \
                    libdb-dev \
                    libevent-dev \
                    libminiupnpc-dev \
                    libprotobuf-dev \
                    libqrencode-dev \
                    libssl-dev \
                    libtool \
                    libzmq3-dev \
                    libzmq5 \
                    lcov \
                    pkg-config \
                    protobuf-compiler \
                    qtbase5-dev \
                    qttools5-dev-tools \
                    wget

# create all the dirs
RUN for i in $TOP_DIR $BDB_SRCDIR $BDB_TGTDIR $MUE_SRCDIR $MUE_CLI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/usr/bin; do mkdir -p ${i}; done

# build libdb-dev v4.8 from source and install it in /tmp/db-$BDB_VERSION-build
RUN wget -qO $BDB_SRCDIR/db.tar.gz $BDB_URL && \
    cd $BDB_SRCDIR && \
    tar xzf db.tar.gz && \
    cd $BDB_SRCDIR/db-$BDB_VERSION/build_unix && \
    mkdir -p $BDB_TGTDIR && \
    ../dist/configure --disable-shared --enable-cxx --with-pic --prefix=$BDB_TGTDIR && \
    # get number of CPUs and use all of them to compile
    make -j$(lscpu | grep '^CPU(s):' | awk '{ print $2 }') && \
    make install

# clone the git repo
RUN git clone $MUE_URL $MUE_SRCDIR

# build MUECore with QT5 GUI from Github sources
RUN cd $MUE_SRCDIR && \
    sh ./autogen.sh && \
    ./configure --prefix=/usr --with-gui=qt5 CPPFLAGS="-I$BDB_TGTDIR/include -O2" LDFLAGS="-L$BDB_TGTDIR/lib" && \
    # get number of CPUs and use all of them to compile
    make -j$(lscpu | grep '^CPU(s):' | awk '{ print $2 }') && \
    make DESTDIR=$MUE_CLI_TGTDIR install && \
    strip $MUE_CLI_TGTDIR/usr/bin/* && \
    # move gui files to separate dir
    mv $MUE_CLI_TGTDIR/usr/bin/*qt $MUE_GUI_TGTDIR/usr/bin/ && \
    # create .deb from newly compiled MUE wallet files
    mv /tmp/mue_cli_control $MUE_CLI_TGTDIR/DEBIAN/control && \
    mv /tmp/mue_qt5_control $MUE_GUI_TGTDIR/DEBIAN/control && \
    cd $TOP_DIR && \
    dpkg-deb --build $MUE_CLI_TGTDIR monetaryunit-wallet-$MUE_VERSION-ubuntu_zesty-amd64.deb && \
    dpkg-deb --build $MUE_GUI_TGTDIR monetaryunit-wallet-qt5-$MUE_VERSION-ubuntu_zesty-amd64.deb
