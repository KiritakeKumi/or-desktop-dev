# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define qt6_version 6.8.0

%define rname attica
# Full KF6 version (e.g. 6.27.0)
%{!?_kf6_version: %global _kf6_version %{version}}

Name:           kf6-attica
Version:        6.27.0
Release:        %autorelease
Summary:        Open Collaboration Service client library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/frameworks/attica.git
#!RemoteAsset:  sha256:8f3d3d61ec8a7456db8a75caa801a2e5f5e046728bd240a003e71b8813093ae4
Source:         https://download.kde.org/stable/frameworks/6.27/%{rname}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  qt6-qttools
BuildRequires:  qt6-doctools
BuildRequires:  qt6-linguist

%description
Attica is a library to access Open Collaboration Service servers.

%package        devel
Summary:        Open Collaboration Service client library - development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}

%description    devel
Development files for attica, a library to access Open Collaboration Service servers.

%files
%doc README.md
%license LICENSES/*
%{_kf6_debugdir}/attica.categories
%{_kf6_debugdir}/attica.renamecategories
%{_kf6_libdir}/libKF6Attica.so.*

%files devel
%{_kf6_cmakedir}/KF6Attica/
%{_kf6_includedir}/Attica/
%{_kf6_libdir}/libKF6Attica.so
%{_kf6_pkgconfigdir}/KF6Attica.pc

%changelog
%autochangelog
