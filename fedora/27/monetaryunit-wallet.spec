Name: monetaryunit-wallet
Version: 2.0.2
Release: 1
%undefine _disable_source_fetch
Source: https://github.com/muecoin/MUE/archive/v%{version}.tar.gz
%define     SHA256SUM0 c525dc89f76a8836c031bb7ef05bbcdfdb72feef1930a292eaaddea31037b18d
# https://github.com/PIVX-Project/PIVX/issues/601
Patch0: pivx_issue_601.patch
License: MIT
Summary: Monetary Unit (MUE) wallet
Group: Applications/System
BuildRequires: boost-devel
BuildRequires: libdb4-cxx-devel
BuildRequires: libdb4-devel
BuildRequires: libevent-devel
BuildRequires: miniupnpc-devel
BuildRequires: openssl-devel
BuildRequires: protobuf-devel
BuildRequires: qrencode-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: zeromq-devel
Requires: boost-chrono
Requires: boost-date-time
Requires: boost-filesystem
Requires: boost-program-options
Requires: boost-system
Requires: boost-thread
Requires: compat-openssl10
Requires: glibc
Requires: keyutils-libs
Requires: krb5-libs
Requires: libcom_err
Requires: libdb4-cxx
Requires: libevent
Requires: libgcc
Requires: libselinux
Requires: libstdc++
Requires: miniupnpc
Requires: openpgm
Requires: openssl-libs
Requires: pcre2
Requires: zeromq
Requires: zlib
# disable autodetection of package dependencies: it causes
# trouble because of our custom OpenSSL-1.0 build
AutoReq: no
Provides: /usr/lib64/libssl.so.1.0.0
Provides: /usr/lib64/libcrypto.so.1.0.0

%description
This package provides the Monetary Unit (MUE) wallet with CLI.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.

%global debug_package %{nil}

# subpackage monetaryunit-wallet-qt5
%package qt5
Group: Applications/System
Summary: QT5 GUI for the Monetary Unit (MUE) wallet
Requires: bzip2-libs
Requires: dbus-libs
Requires: freetype
Requires: glib2
Requires: graphite2
Requires: harfbuzz
Requires: libX11
Requires: libXau
Requires: libXext
Requires: libgcrypt
Requires: libglvnd
Requires: libglvnd-glx
Requires: libgpg-error
Requires: libicu
Requires: libpng
Requires: libxcb
Requires: lz4-libs
Requires: monetaryunit-wallet
Requires: pcre
Requires: pcre2-utf16
Requires: protobuf
Requires: qrencode-libs
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: systemd-libs
Requires: xz-libs
# disable autodetection of package dependencies: it causes
# trouble because of our custom OpenSSL-1.0 build
AutoReq: no

%description qt5
This package provides the QT5 GUI to the Monetary Unit (MUE) wallet.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -

%setup -n MUE-%{version}
%patch0 -p1

%build
./autogen.sh
# The /opt/openssl-1.0 path was created with a custom build of 
# OpenSSL-1.0 because it's impossible to install openssl-devel and
# compat-openssl10-devel at the same time on Fedora 27.
# The custom build is done earlier in the Dockerfile
./configure --prefix=/usr --with-gui=qt5 \
  CFLAGS="-I/opt/openssl-1.0/include/openssl -I/usr/include/libdb4/" \
  CPPFLAGS="-I/opt/openssl-1.0/include/openssl -I/usr/include/libdb4" \
  CXXFLAGS="-I/opt/openssl-1.0/include/openssl -I/usr/include/libdb4" \
  LDFLAGS="-L/opt/openssl-1.0/lib -L/usr/lib64/libdb4" \
  PKG_CONFIG_PATH="/opt/openssl-1.0/lib/pkgconfig"
%make_build

%install
%make_install
# Create symlinks because the MUE binaries are linked to generic
# names of OpenSSL-1.0 .so's, probably due to the sloppy custom build
# of OpenSSL-1.0 mentioned above.
mkdir -p %{buildroot}/usr/lib64
cd %{buildroot}/usr/lib64
ln -sf libcrypto.so.10 libcrypto.so.1.0.0
ln -sf libssl.so.10 libssl.so.1.0.0

%files
/usr/bin/monetaryunit-cli
/usr/bin/monetaryunit-tx
/usr/bin/monetaryunitd
/usr/lib64/libcrypto.so.1.0.0
/usr/lib64/libssl.so.1.0.0

%files qt5
/usr/bin/monetaryunit-qt
