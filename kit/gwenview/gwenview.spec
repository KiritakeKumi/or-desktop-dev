# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define plasma6_version 5.27.80
%define qt6_version 6.9.0

Name:           gwenview
Version:        26.04.2
Release:        %autorelease
Summary:        Image Viewer by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/gwenview
VCS:            git:https://invent.kde.org/graphics/gwenview.git
#!RemoteAsset:  sha256:150b601741f1fcf3aae5e8fa6dbd28ae83afe3e0914a1e91c84efa55312d9a69
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cfitsio-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libjpeg-turbo
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Baloo) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  cmake(kImageAnnotator-Qt6)
BuildRequires:  cmake(kColorPicker-Qt6)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)

%description
Gwenview is an image viewer by KDE. It features a folder tree window and a file
list window, providing navigation of file hierarchies.

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/gwenview/
%{_kf6_applicationsdir}/org.kde.gwenview.desktop
%{_kf6_applicationsdir}/org.kde.gwenview_importer.desktop
%{_kf6_appstreamdir}/org.kde.gwenview.appdata.xml
%{_kf6_bindir}/gwenview
%{_kf6_bindir}/gwenview_importer
%{_kf6_debugdir}/gwenview.categories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_libdir}/libgwenviewlib.so.*
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/slideshowfileitemaction.so
%{_kf6_plugindir}/kf6/parts/gvpart.so
%{_kf6_sharedir}/gwenview/
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/gwenview_importer.desktop
%{_kf6_sharedir}/solid/actions/gwenview_importer_camera.desktop

%changelog
%autochangelog
