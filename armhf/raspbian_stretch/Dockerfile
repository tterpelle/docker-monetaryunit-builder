FROM debian:9

ENV ARCH armhf
ENV VERSION 2.0.2
ENV URL https://github.com/muecoin/MUE/releases/download/v2.0.2/mon-arm-linux-gnueabihf.tar.gz

RUN apt update && \
    apt -y install wget

# Download and extract MUE software
RUN wget -nv -O /tmp/muecore-armhf.tar.gz ${URL} && \
    tar xzf /tmp/muecore-armhf.tar.gz -C /tmp

# Create package dirs
RUN mkdir -p /tmp/monetaryunit-daemon/usr/bin && \
    mkdir -p /tmp/monetaryunit-daemon/DEBIAN && \
    mkdir -p /tmp/monetaryunit-qt5/usr/bin && \
    mkdir -p /tmp/monetaryunit-qt5/DEBIAN && \
    cd /tmp/mon/bin && \
  # PKG monetaryunitd
    mv monetaryunitd monetaryunit-cli monetaryunit-tx /tmp/monetaryunit-daemon/usr/bin/ && \
  # PKG monetaryunit-qt5
    mv monetaryunit-qt /tmp/monetaryunit-qt5/usr/bin/

COPY monetaryunit-daemon.control /tmp/monetaryunit-daemon/DEBIAN/control
COPY monetaryunit-qt5.control /tmp/monetaryunit-qt5/DEBIAN/control

RUN dpkg-deb --build /tmp/monetaryunit-daemon monetaryunit-daemon_${VERSION}_${ARCH}.deb && \
    dpkg-deb --build /tmp/monetaryunit-qt5 monetaryunit-qt5_${VERSION}_${ARCH}.deb

COPY copy_packages.sh /

ENTRYPOINT [ "/copy_packages.sh" ]
