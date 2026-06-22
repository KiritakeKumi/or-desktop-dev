# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define soversion 6

Name:           assimp
Version:        6.0.5
Release:        %autorelease
Summary:        Library to import various 3D model formats into applications
License:        BSD-3-Clause AND MIT AND BSL-1.0 AND Apache-2.0 AND Unlicense AND Zlib
URL:            https://github.com/assimp/assimp
VCS:            git:https://github.com/assimp/assimp.git
#!RemoteAsset:  sha256:edf3749559c2b7d1f758ffb66fc5bec62186221e623b7f2e8969f17ee46ecb6f
Source:         https://github.com/assimp/assimp/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DASSIMP_WARNINGS_AS_ERRORS=OFF
BuildOption(conf):  -DASSIMP_BUILD_ASSIMP_TOOLS=OFF
BuildOption(conf):  -DASSIMP_BUILD_TESTS=OFF
BuildOption(conf):  -DASSIMP_IGNORE_GIT_HASH=ON
BuildOption(conf):  -DASSIMP_BUILD_ZLIB=ON
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Assimp (Open Asset Import Library) is a library to import various well-known 3D
model formats into a shared in-memory data structure. It is built here with its
bundled third-party contrib libraries (draco, pugixml, poly2tri, rapidjson,
utf8cpp, stb, zip, zlib) for a self-contained build.

%package        devel
Summary:        Development files for assimp
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Header files, the shared library symlink and pkg-config file for developing
applications that use assimp.

%install -a
# Drop the internal static zlib (built via ASSIMP_BUILD_ZLIB=ON, linked into libassimp).
rm -f %{buildroot}%{_libdir}/libzlibstatic.a

%files
%license LICENSE
%doc Readme.md CREDITS
%{_libdir}/libassimp.so.%{soversion}
%{_libdir}/libassimp.so.%{soversion}.%{version}

%files devel
%{_includedir}/assimp
%{_libdir}/libassimp.so
%{_libdir}/pkgconfig/assimp.pc
%{_libdir}/cmake/assimp-*/

%changelog
%autochangelog
