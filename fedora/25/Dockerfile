FROM fedora:25

ENV DISTRO "fedora25"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"

# update yum, install EPEL repo and the packages required to build the wallet
RUN yum -y update && \
    yum -y install epel-release && \
    yum -y upgrade && \
    yum -y groupinstall 'Development Tools' && \
    yum -y install boost-devel \
										libdb4-devel \
										libdb4-cxx-devel \
										libevent-devel \
										miniupnpc-devel \
										openssl-devel \
										protobuf-devel \
										qrencode-devel \
										qt5-qtbase-devel \
										qt5-qttools-devel \
										rpmdevtools \
										zeromq-devel

# create build user and set up the package build environment
RUN mkdir $TOP_DIR && \
    groupadd -g 1000 build && \
    useradd -g build -m -d $DISTRO_DIR -s /bin/bash -c "Build user" build && \
    su -c 'rpmdev-setuptree' - build

# copy the spec file to the Docker image
COPY monetaryunit-wallet.spec $DISTRO_DIR/rpmbuild/SPECS/

# build MUE packages from .spec file
RUN su -c "rpmbuild -ba $DISTRO_DIR/rpmbuild/SPECS/monetaryunit-wallet.spec" - build

# move monetaryunit-wallet-*.rpm to $DISTRO_DIR where they can be picked up by /copy_packages.sh
RUN mv $DISTRO_DIR/rpmbuild/*RPM/monetaryunit-wallet-*.rpm $DISTRO_DIR

ENTRYPOINT [ "/copy_packages.sh", "$DISTRO", "rpm" ]
