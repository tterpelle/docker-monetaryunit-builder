FROM centos:7

ENV DISTRO "centos7"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"
ENV MUE_SRCDIR "$DISTRO_DIR/mue/src"
ENV MUE_CLI_TGTDIR "$DISTRO_DIR/mue/build"
ENV MUE_GUI_TGTDIR "$DISTRO_DIR/mue/build-gui"
ENV MUE_URL "https://github.com/muecoin/MUECore.git"
ENV MUE_VERSION "1.0.3.2"

COPY mue-wallet.spec /tmp

# update apt
RUN yum -y install epel-release && \
# install dependencies
    yum update && \
    yum -y upgrade && \
    yum -y install  boost-devel \
                    git \
                    libdb4-devel \
                    protobuf \
                    rpm-build \
                    rpmdevtools \
                    wget
                   	#bsdmainutils \
                    #build-essential \
                    #gawk \
                    #gettext \
                    #git \
                    #libboost-all-dev \
                    #libdb-dev \
                    #libevent-dev \
                    #libminiupnpc-dev \
                    #libprotobuf-dev \
                    #libqrencode-dev \
                    #libssl-dev \
                    #libtool \
                    #libzmq3-dev \
                    #libzmq5 \
                    #lcov \
                    #pkg-config \
                    #protobuf-compiler \
                    #qtbase5-dev \
                    #qttools5-dev-tools \
                    #wget

# create all the dirs
RUN for i in $DISTRO_DIR $BDB_SRCDIR $BDB_TGTDIR $MUE_SRCDIR $MUE_CLI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/DEBIAN $MUE_GUI_TGTDIR/usr/bin; do mkdir -p ${i}; done

# clone the git repo
#RUN git clone $MUE_URL $MUE_SRCDIR
#
## build MUECore with QT5 GUI from Github sources
#RUN cd $MUE_SRCDIR && \
#    sh ./autogen.sh && \
#    ./configure --prefix=/usr --with-gui=qt5 CPPFLAGS="-I$BDB_TGTDIR/include -O2" LDFLAGS="-L$BDB_TGTDIR/lib" && \
#    # get number of CPUs and use all of them to compile
#    make -j$(lscpu | grep '^CPU(s):' | awk '{ print $2 }') && \
#    make DESTDIR=$MUE_CLI_TGTDIR install && \
#    strip $MUE_CLI_TGTDIR/usr/bin/* && \
#    # move gui files to separate dir
#    mv $MUE_CLI_TGTDIR/usr/bin/*qt $MUE_GUI_TGTDIR/usr/bin/
#
## build list of dependencies for binaries with ldd
##RUN for so in $(ldd $MUE_CLI_TGTDIR/usr/bin/* | awk -F'*' "{ print $3 }"); do dpkg -S ${so}; done | sort > $MUE_SRCDIR/mue_cli.deps && \
#RUN for so in $(ldd $(find $MUE_CLI_TGTDIR/usr/bin/ -type f) | awk -F'*' "{ print $3 }"); do dpkg -S ${so}; done | sort > $MUE_SRCDIR/mue_cli.deps && \
#    #for so in $(ldd $MUE_GUI_TGTDIR/usr/bin/* | awk "{ print $3 }"); do dpkg -S ${so}; done | sort > $MUE_SRCDIR/mue_gui.deps && \
#    while read line; do sed -i -e '/${line}/d' $MUE_SRCDIR/mue_gui.deps; done < $MUE_SRCDIR/mue_cli.deps && \
#    #CLIDEPS=$(tr '\n' ',' < $MUE_SRCDIR/mue_cli.deps) && \
#    #GUIDEPS=$(tr '\n' ',' < $MUE_SRCDIR/mue_gui.deps) 
#    sed -i -e "s#Depends:.*#Depends: $(tr '\n' ',' < $MUE_SRCDIR/mue_cli.deps)#" -e 's#\(Depends:.*\),$#\1#' /tmp/mue_cli_control && \
#    cat /tmp/mue_cli_control && \
#    echo "------------" && \
#    sed -i -e 's#Depends:.*#Depends: $(tr '\n' ',' < $MUE_SRCDIR/mue_gui.deps)#' -e 's#\(Depends:.*\),$#\1#' /tmp/mue_qt5_control && \
#    cat /tmp/mue_qt5_control && \
#    #sed -i -e "s#Depends:.*#Depends: $GUIDEPS#" /tmp/mue_gui_control
#
## create .deb from newly compiled MUE wallet files
#RUN mv /tmp/mue_cli_control $MUE_CLI_TGTDIR/DEBIAN/control && \
#    mv /tmp/mue_qt5_control $MUE_GUI_TGTDIR/DEBIAN/control && \
#    cd $DISTRO_DIR && \
#    dpkg-deb --build $MUE_CLI_TGTDIR monetaryunit-wallet-$MUE_VERSION-debian_stretch-amd64.deb && \
#    dpkg-deb --build $MUE_GUI_TGTDIR monetaryunit-wallet-qt5-$MUE_VERSION-debian_stretch-amd64.deb

#ENTRYPOINT [ "/copy_packages.sh", "$DISTRO", "rpm" ]
