# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 2bf2ca7f1623db7ad7840a4dd626444d11830815

Name:           vkmark
Version:        2025.01
Release:        %autorelease
Summary:        Extensible Vulkan benchmarking suite
License:        LGPL-2.1-or-later
URL:            https://github.com/vkmark/vkmark
VCS:            git:https://github.com/vkmark/vkmark.git
#!RemoteAsset:  sha256:71a83b8c23aa0b6d7ad749c9184537f6182e7a66a57ddb44dd74c605dbefba92
Source:         https://github.com/vkmark/vkmark/archive/%{commit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  vulkan-loader-devel
BuildRequires:  glm-devel
BuildRequires:  assimp-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgbm-devel

%description
vkmark is an extensible Vulkan benchmarking suite with targeted, configurable
scenes. It is the Vulkan successor to glmark2 and supports xcb, Wayland and KMS
window systems.

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING-LGPL2.1
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
