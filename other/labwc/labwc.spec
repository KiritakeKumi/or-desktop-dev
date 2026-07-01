# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           labwc
Version:        0.20.1
Release:        %autorelease
Summary:        A Wayland window-stacking compositor
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc
#!RemoteAsset:  sha256:b9a9efb9f22a0584f91ebd8de4e94132824927992ec5ecc68c2e18d2f0625a21
Source0:        https://github.com/KiritakeKumi/labwc/archive/refs/heads/master.zip
BuildSystem:    meson

BuildOption(conf):  -Dxwayland=disabled

BuildRequires:  meson >= 0.59.0
BuildRequires:  gcc
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libinput) >= 1.14
BuildRequires:  pkgconfig(libsfdo-basedir)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server) >= 0.19.0
BuildRequires:  pkgconfig(wlroots-0.20)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  unzip

Requires:       xdg-desktop-portal-wlr
Requires:       xkeyboard-config

%description
Labwc is a wlroots-based window-stacking compositor for wayland, inspired by
openbox. It is light-weight and independent with a focus on simply stacking
windows well and rendering some window decorations.

%install -a
# TODO: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files -f %{name}.lang
%doc NEWS.md README autostart environment menu.xml rc.xml rc.xml.all shutdown themerc
%license LICENSE
%{_bindir}/labwc
%{_bindir}/lab-sensible-terminal
%{_bindir}/labnag
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_datadir}/xdg-desktop-portal/labwc-portals.conf
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/icons/hicolor/*/*/labwc*.svg
%{_userunitdir}/labwc-session.target

%changelog
%autochangelog
