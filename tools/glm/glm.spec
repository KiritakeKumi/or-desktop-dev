# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global debug_package %{nil}

Name:           glm
Version:        1.0.3
Release:        %autorelease
Summary:        C++ mathematics library for graphics programming
License:        MIT
URL:            http://glm.g-truc.net
VCS:            git:https://github.com/g-truc/glm.git
#!RemoteAsset:  sha256:6775e47231a446fd086d660ecc18bcd076531cfedd912fbd66e576b118607001
Source:         https://github.com/g-truc/glm/archive/%{version}.tar.gz
BuildSystem:    cmake
BuildArch:      noarch

BuildOption(conf):  -DGLM_BUILD_LIBRARY=OFF
BuildOption(conf):  -DGLM_BUILD_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++

Provides:       glm-devel = %{version}-%{release}
Provides:       glm-static = %{version}-%{release}

%description
GLM is a header-only C++ mathematics library for graphics programming based on
the GLSL specification. Its interface resembles the built-in matrix and vector
types of the OpenGL Shading Language.

%files
%license copying.txt
%doc readme.md
%{_includedir}/glm
%{_datadir}/glm

%changelog
%autochangelog
