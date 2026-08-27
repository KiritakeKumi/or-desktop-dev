# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           mongo-c-driver
Version:        2.5.0
Release:        %autorelease
Summary:        Client library written in C for MongoDB
License:        Apache-2.0
URL:            https://www.mongodb.com/docs/drivers/c/
VCS:            git:https://github.com/mongodb/mongo-c-driver
#!RemoteAsset:  sha256:3ecf5ffe9c442cd05a79e0e9e7797a2bacd2977733a3d53555ba6fa54936f7b3
Source:         https://codeload.github.com/mongodb/mongo-c-driver/tar.gz/refs/tags/%{version}#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DENABLE_MONGOC:BOOL=ON
BuildOption(conf):  -DENABLE_SHARED:BOOL=ON
BuildOption(conf):  -DENABLE_STATIC:STRING=OFF
BuildOption(conf):  -DENABLE_SSL:STRING=OPENSSL
BuildOption(conf):  -DENABLE_SASL:STRING=CYRUS
BuildOption(conf):  -DENABLE_ZLIB:STRING=SYSTEM
BuildOption(conf):  -DENABLE_SNAPPY:STRING=ON
BuildOption(conf):  -DENABLE_ZSTD:STRING=ON
BuildOption(conf):  -DENABLE_SRV:BOOL=ON
BuildOption(conf):  -DENABLE_MONGODB_AWS_AUTH:STRING=ON
# ships mongoc2-stat; on by default on Linux, pinned so %%files stays stable
BuildOption(conf):  -DENABLE_SHM_COUNTERS:BOOL=ON
# needs libmongocrypt, which openRuyi does not package (yet)
BuildOption(conf):  -DENABLE_CLIENT_SIDE_ENCRYPTION:STRING=OFF
BuildOption(conf):  -DENABLE_TESTS:BOOL=OFF
BuildOption(conf):  -DENABLE_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DENABLE_UNINSTALL:BOOL=OFF
BuildOption(conf):  -DENABLE_MAN_PAGES:BOOL=OFF
BuildOption(conf):  -DENABLE_HTML_DOCS:BOOL=OFF
BuildOption(conf):  -DBUILD_TESTING:BOOL=OFF

BuildRequires:  cmake >= 3.15
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cyrus-sasl-devel
BuildRequires:  snappy-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

# utf8proc is required for SCRAM-SHA-256 with non-ASCII passwords and
# kms-message/uthash have no upstream releases to package separately
Provides:       bundled(utf8proc) = 2.11.3
Provides:       bundled(kms-message)
Provides:       bundled(uthash)

%description
mongo-c-driver is the officially supported MongoDB client library for C.  It
ships libmongoc, the driver itself, and libbson, a library for building,
parsing and iterating BSON documents.

The client library is Apache-2.0 licensed and unaffected by the SSPL
relicensing of the MongoDB server.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)

%description    devel
This package contains the header files, the pkg-config files and the CMake
package configuration needed to develop applications that use libmongoc and
libbson.

%install -a
# shipped as %%license/%%doc instead
rm -rf %{buildroot}%{_datadir}/mongo-c-driver

%files
%license COPYING THIRD_PARTY_NOTICES
%doc NEWS README.rst
%{_bindir}/mongoc2-stat
%{_libdir}/libbson2.so.2*
%{_libdir}/libmongoc2.so.2*

%files devel
%{_includedir}/bson-%{version}/
%{_includedir}/mongoc-%{version}/
%{_libdir}/libbson2.so
%{_libdir}/libmongoc2.so
%{_libdir}/cmake/bson-%{version}/
%{_libdir}/cmake/mongoc-%{version}/
%{_libdir}/pkgconfig/bson2.pc
%{_libdir}/pkgconfig/mongoc2.pc

%changelog
%autochangelog
