FROM fedora:27

ENV DISTRO "fedora27"

ENV TOP_DIR "/monetaryunit"
ENV DISTRO_DIR "$TOP_DIR/$DISTRO"

ENV OPENSSL_URL "https://www.openssl.org/source/openssl-1.0.2p.tar.gz"
ENV OPENSSL_SUM "50a98e07b1a89eb8f6a99477f262df71c6fa7bef77df4dc83025a2845c827d00"

# update dnf, install EPEL repo and the packages required to build the wallet
RUN dnf -y update && \
    dnf -y upgrade && \
    dnf -y install autoconf \
										automake \
										binutils \
										bison \
										boost-devel \
										flex \
										gcc \
										gcc-c++ \
										gettext \
										libdb4-cxx-devel \
										libdb4-devel \
										libevent-devel \
										libtool \
										make \
										miniupnpc-devel \
										openssl-devel \
										patch \
										pkgconfig \
										protobuf-devel \
										qrencode-devel \
										qt5-qtbase-devel \
										qt5-qttools-devel \
										redhat-rpm-config \
										rpm-build \
										rpm-sign \
										rpmdevtools \
										which \
										wget \
										zeromq-devel

# create build user and set up the package build environment
RUN mkdir $TOP_DIR && \
    groupadd -g 1000 build && \
    useradd -g build -m -d $DISTRO_DIR -s /bin/bash -c "Build user" build && \
    su -c 'rpmdev-setuptree' - build && \
    # run one job less than the number of available CPUs concurrently
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    echo "%__make     /usr/bin/make -j${BUILDJOBS}" >> /etc/rpm/macros


# build OpenSSL-1.0
RUN mkdir -vp ${DISTRO_DIR}/src/openssl10 && \
    wget -O ${DISTRO_DIR}/src/openssl10.tar.gz ${OPENSSL_URL} && \
    sha256sum ${DISTRO_DIR}/src/openssl10.tar.gz | grep -q "^${OPENSSL_SUM} " && \
    tar xvzf ${DISTRO_DIR}/src/openssl10.tar.gz -C ${DISTRO_DIR}/src/openssl10 --strip-components 1 && \
    cd ${DISTRO_DIR}/src/openssl10 && \
    ./Configure --prefix=/opt/openssl-1.0 --openssldir=/etc/ssl --libdir=lib shared no-ssl3-method enable-ec_nistp_64_gcc_128 linux-x86_64 enable-ec enable-ecdh enable-ecdsa -Wa,--noexecstack && \
    make depend && \
    BUILDJOBS="$(($(nproc)-1))" && \
    if [ "${BUILDJOBS}" -lt 1 ]; then BUILDJOBS=1; fi && \
    make -j ${BUILDJOBS} && \
    make install

# copy the spec file to the Docker image
COPY monetaryunit-wallet.spec $DISTRO_DIR/rpmbuild/SPECS/
COPY pivx_issue_601.patch $DISTRO_DIR/rpmbuild/SOURCES/

# build MUE packages from .spec file
RUN su -c "rpmbuild -ba --noclean $DISTRO_DIR/rpmbuild/SPECS/monetaryunit-wallet.spec" - build

# move monetaryunit-wallet-*.rpm to $DISTRO_DIR where they can be picked up by /copy_packages.sh
RUN find $DISTRO_DIR/rpmbuild/ -name 'monetaryunit-wallet-*.rpm' -exec mv {} $DISTRO_DIR \;

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh" ]
