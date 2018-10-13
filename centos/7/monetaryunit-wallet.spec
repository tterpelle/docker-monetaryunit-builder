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
BuildRequires: libdb4-devel
BuildRequires: libdb4-cxx-devel
BuildRequires: libevent-devel
BuildRequires: miniupnpc-devel
BuildRequires: openssl-devel
BuildRequires: protobuf-devel
BuildRequires: qrencode-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: which
BuildRequires: zeromq-devel

%description
This package provides the Monetary Unit (MUE) wallet with CLI.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.

%global debug_package %{nil}

# subpackage monetaryunit-wallet-qt5
%package qt5
Group: Applications/System
Summary: QT5 GUI for the Monetary Unit (MUE) wallet
%description qt5
This package provides the QT5 GUI to the Monetary Unit (MUE) wallet.
MUE is a decentralised, self-sustainable and self-governed cryptocurrency
project with long term goals.

# verify checksum of downloaded source
%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -

%setup -n MUE-%{version}
%patch0 -p1

%build
./autogen.sh
./configure --prefix=/usr --with-gui=qt5 BDB_FLAGS="-I /usr/include/libdb4" CFLAGS="-I /usr/include/libdb4" CPPFLAGS="-I /usr/include/libdb4" CXXFLAGS="-I /usr/include/libdb4"
make

%install
%make_install

%files
/usr/bin/monetaryunit-cli
/usr/bin/monetaryunit-tx
/usr/bin/monetaryunitd

%files qt5
/usr/bin/monetaryunit-qt
