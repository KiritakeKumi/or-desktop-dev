# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vkpeak
Version:        20260527
Release:        %autorelease
Summary:        Synthetic Vulkan device peak performance benchmark
License:        MIT AND BSD-3-Clause
URL:            https://github.com/nihui/vkpeak
VCS:            git:https://github.com/nihui/vkpeak.git
#!RemoteAsset:  sha256:ccdd270e3a565a4f8cac0296fd8f05aa0dd3f04c107f89e66529755c91b24b10
Source:         https://github.com/nihui/vkpeak/archive/refs/tags/%{version}.tar.gz
#!RemoteAsset:  sha256:999e904d1631f46381728c68c3255af67d2cf4dbfbab8e3a7f2343e7a6dffc3d
Source1:        https://github.com/Tencent/ncnn/archive/e54f7b1f88434e1d844ea0551b880a1cfb079ce1.tar.gz
#!RemoteAsset:  sha256:dc78c7f2c479779db66c60582bf8c4173b75b89f689b7edaff3a97d8820dbecd
Source2:        https://github.com/nihui/glslang/archive/fe88f421038e1bb0a25cd5c1b2dfe505db82d08f.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  vulkan-headers

Requires:       vulkan-loader

%description
vkpeak is a synthetic benchmarking tool to measure the peak capabilities of
Vulkan devices. It measures the peak metrics that can be achieved using vector
and matrix operations (fp32/fp16/fp64, int8/int16/int32/int64, bf16, fp8) and
does not represent a real-world use case.

%prep -a
tar -xf %{SOURCE1} --strip-components=1 -C ncnn
tar -xf %{SOURCE2} --strip-components=1 -C ncnn/glslang
echo 'install(TARGETS vkpeak RUNTIME DESTINATION bin)' >> CMakeLists.txt

%files
%doc README.md
%license LICENSE
%license ncnn/LICENSE.txt
%license ncnn/glslang/LICENSE.txt
%{_bindir}/vkpeak

%changelog
%autochangelog
