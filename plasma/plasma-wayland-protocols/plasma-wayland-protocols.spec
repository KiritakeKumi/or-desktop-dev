# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           plasma-wayland-protocols
Version:        1.20.0
Release:        %autorelease
Summary:        Wayland protocols used by Plasma
License:        BSD-3-Clause AND LGPL-2.1-only AND LGPL-2.1-or-later AND MIT
URL:            https://www.kde.org
VCS:            https://invent.kde.org/libraries/plasma-wayland-protocols
#!RemoteAsset:  sha256:9818bb1462211ce5982e670abf0d964eb11fe1d0c02a1c26084db30695a79d6a
Source0:        https://download.kde.org/stable/plasma-wayland-protocols/plasma-wayland-protocols-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig(wayland-scanner)

%description
This package contains the non-standard Wayland protocol definitions used by
KDE Plasma.

%files
%license COPYING* LICENSES/*.txt
%{_kf6_sharedir}/plasma-wayland-protocols/
%dir %{_kf6_sharedir}/cmake/
%{_kf6_sharedir}/cmake/PlasmaWaylandProtocols/

%changelog
%autochangelog
