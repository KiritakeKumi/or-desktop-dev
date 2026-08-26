# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtins
Version:        4.6
Release:        %autorelease
Summary:        C++ library for network packet sniffing and crafting
License:        BSD-2-Clause
URL:            https://libtins.github.io/
VCS:            git:https://github.com/mfontanini/libtins
#!RemoteAsset:  sha256:37a9cc407929c56c2081e717347cac455287ba354016bad5bad6243d1f0a4a7a
Source:         https://github.com/mfontanini/libtins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DLIBTINS_BUILD_SHARED:BOOL=ON
BuildOption(conf):  -DLIBTINS_BUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DLIBTINS_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DLIBTINS_ENABLE_CXX11:BOOL=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# header only (boost.icl / boost.any), needed for the TCP ACK tracker and the
# TCP stream custom data support, which are silently dropped without it
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(openssl)

%description
libtins is a high-level, multiplatform C++ network packet sniffing and
crafting library.  It allows decoding, forging and sending arbitrary packets
of a wide range of protocols.

Open5GS links its UPF against libtins to build gratuitous ARP and IPv6
neighbour discovery packets for the UE address pool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libpcap)

%description    devel
This package contains the header files, the pkg-config file and the CMake
package configuration needed to develop applications that use libtins.

%check
# The test suite pulls in a bundled googletest submodule which is not part of
# the release tarball, so it is disabled at configure time.

%files
%license LICENSE
%doc CHANGES.md README.md THANKS
%{_libdir}/libtins.so.*

%files devel
%{_includedir}/tins/
%{_libdir}/libtins.so
%{_libdir}/cmake/libtins/
%{_libdir}/pkgconfig/libtins.pc

%changelog
%autochangelog
