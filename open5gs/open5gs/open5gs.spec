# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Open5GS always builds freeDiameter and prometheus-client-c as meson
# subprojects; there is no way to link them from the system.  Both wraps track
# a *branch*, so the sources are vendored here at the branch HEAD the 2.8.0
# tag was released against (the build chroot has no network access).
# subprojects/freeDiameter.wrap        -> branch r1.5.0
%global fd_commit       14725af3ba0edbf9ff61c4e3239ed42464423b2e
# subprojects/prometheus-client-c.wrap -> branch open5gs
%global prom_commit     a58ba25bf87a9b1b7c6be4e6f4c62047d620f402

# Kept on a single line on purpose: a backslash-continued macro body would
# expand with embedded newlines and break the systemd scriptlets.
%global open5gs_units open5gs-amfd.service open5gs-ausfd.service open5gs-bsfd.service open5gs-hssd.service open5gs-mmed.service open5gs-nrfd.service open5gs-nssfd.service open5gs-pcfd.service open5gs-pcrfd.service open5gs-scpd.service open5gs-seppd.service open5gs-sgwcd.service open5gs-sgwud.service open5gs-smfd.service open5gs-udmd.service open5gs-udrd.service open5gs-upfd.service

Name:           open5gs
Version:        2.8.0
Release:        %autorelease
Summary:        5G Core and EPC implementation
# open5gs itself:              AGPL-3.0-or-later
# bundled freeDiameter:        BSD-3-Clause
# bundled prometheus-client-c: Apache-2.0
License:        AGPL-3.0-or-later AND BSD-3-Clause AND Apache-2.0
URL:            https://open5gs.org
VCS:            git:https://github.com/open5gs/open5gs
#!RemoteAsset:  sha256:a04d66f66f6df62a376a2434a05a7268e08e4fc0cc1b9c56221467689a8b56ab
Source0:        https://github.com/open5gs/open5gs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:7933b473661d8fd2f21a5956333643449801e34f930a60a1b36c96572282aa81
Source1:        https://github.com/open5gs/freeDiameter/archive/%{fd_commit}.tar.gz#/freeDiameter-%{fd_commit}.tar.gz
#!RemoteAsset:  sha256:240ccf3616a4b12fcb1f987f75aaab835264fb132360100b9f2b0581718dd349
Source2:        https://github.com/open5gs/prometheus-client-c/archive/%{prom_commit}.tar.gz#/prometheus-client-c-%{prom_commit}.tar.gz
Source3:        open5gs.sysusers
BuildSystem:    meson

BuildRequires:  meson >= 0.51.0
# openRuyi ships the backend as "ninja", not as Fedora's "ninja-build"
BuildRequires:  ninja
BuildRequires:  gcc
BuildRequires:  gcc-c++
# lib/metrics pulls prometheus-client-c in as a CMake subproject
BuildRequires:  cmake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  python3
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.52.1
BuildRequires:  pkgconfig(libmicrohttpd) >= 0.9.40
BuildRequires:  pkgconfig(libnghttp2) >= 1.18.1
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libtins) >= 3.4
BuildRequires:  pkgconfig(mongoc2)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(yaml-0.1)
# looked up with cc.find_library(), so the -devel packages are needed for the
# unversioned .so symlinks rather than for a .pc file
BuildRequires:  libgcrypt-devel
BuildRequires:  libidn-devel
BuildRequires:  lksctp-tools-devel

Provides:       bundled(freediameter) = 1.5.0
Provides:       bundled(prometheus-client-c) = 0.1.3

%{?systemd_requires}

%description
Open5GS is a C-language implementation of the 5G Core and the EPC, i.e. the
core network of an NR/LTE network.

It provides the 5G network functions (AMF, SMF, UPF, AUSF, UDM, UDR, PCF,
NSSF, BSF, NRF, SCP, SEPP) as well as the EPC entities (MME, SGW-C, SGW-U,
HSS, PCRF), each shipped as a separate systemd service that is disabled by
default.

The HSS, UDR and PCRF store subscriber data in MongoDB.  openRuyi cannot ship
a MongoDB server because it is distributed under the SSPL, which is not a free
software license, so the database has to be provided externally; only the
Apache-2.0 licensed C driver is packaged.

The UPF and SGW-U need the "ogstun" TUN device described by the shipped
systemd-networkd .netdev/.network files, and the CAP_NET_ADMIN capability,
which the upstream unit files do not grant.

%prep -a
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
mv freeDiameter-%{fd_commit} subprojects/freeDiameter
mv prometheus-client-c-%{prom_commit} subprojects/prometheus-client-c
# %%license cannot keep two files called LICENSE apart
cp -p subprojects/freeDiameter/LICENSE LICENSE.freeDiameter
cp -p subprojects/prometheus-client-c/LICENSE LICENSE.prometheus-client-c

%install -a
# Everything below /etc and /var is installed by meson.add_install_script()
# hooks which are explicit no-ops when DESTDIR is set, so they have to be
# replayed here by hand.  Note that the files are the *generated* ones from
# the build directory, not the .in templates from the source tree.
install -d -m 0755 %{buildroot}%{_sysconfdir}/open5gs/hnet
install -d -m 0755 %{buildroot}%{_sysconfdir}/open5gs/tls
install -d -m 0755 %{buildroot}%{_sysconfdir}/freeDiameter
install -p -m 0644 %{_vpath_builddir}/configs/open5gs/*.yaml \
    %{buildroot}%{_sysconfdir}/open5gs/
install -p -m 0640 %{_vpath_builddir}/configs/open5gs/hnet/*.key \
    %{buildroot}%{_sysconfdir}/open5gs/hnet/
install -p -m 0644 %{_vpath_builddir}/configs/open5gs/tls/*.crt \
    %{buildroot}%{_sysconfdir}/open5gs/tls/
install -p -m 0640 %{_vpath_builddir}/configs/open5gs/tls/*.key \
    %{buildroot}%{_sysconfdir}/open5gs/tls/
install -p -m 0644 %{_vpath_builddir}/configs/freeDiameter/*.conf \
    %{buildroot}%{_sysconfdir}/freeDiameter/

install -d -m 0755 %{buildroot}%{_unitdir}
install -p -m 0644 %{_vpath_builddir}/configs/systemd/open5gs-*.service \
    %{buildroot}%{_unitdir}/
install -d -m 0755 %{buildroot}%{_prefix}/lib/systemd/network
install -p -m 0644 %{_vpath_builddir}/configs/systemd/99-open5gs.net* \
    %{buildroot}%{_prefix}/lib/systemd/network/
install -D -p -m 0644 %{_vpath_builddir}/configs/logrotate/open5gs \
    %{buildroot}%{_sysconfdir}/logrotate.d/open5gs
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

install -d -m 0755 %{buildroot}%{_localstatedir}/log/open5gs/tls

# libprom comes from a CMake subproject, which picks its install directory
# from GNUInstallDirs instead of from the --libdir meson was configured with.
for so in %{buildroot}%{_prefix}/lib/libprom*.so*; do
    if [ -e "$so" ] && [ "%{_libdir}" != "%{_prefix}/lib" ]; then
        mv "$so" %{buildroot}%{_libdir}/
    fi
done

%check
# The app/epc/5gc suites bring up a full core network: they need a TUN device,
# SCTP sockets and a running MongoDB instance, none of which exist in the
# build chroot.  Upstream Debian restricts the test run the same way.
%meson_test --suite unit

%pre
%sysusers_create_package %{name} %{SOURCE3}

%post
%systemd_post %{open5gs_units}

%preun
%systemd_preun %{open5gs_units}

%postun
%systemd_postun_with_restart %{open5gs_units}

%files
%license LICENSE LICENSE.freeDiameter LICENSE.prometheus-client-c
%doc README.md
%{_bindir}/open5gs-*d
%{_libdir}/libogs*.so*
%{_libdir}/libfdcore.so*
%{_libdir}/libfdproto.so*
%{_libdir}/libprom*.so*
%dir %{_libdir}/freeDiameter
%{_libdir}/freeDiameter/*.fdx
%{_unitdir}/open5gs-*.service
%{_sysusersdir}/%{name}.conf
%{_prefix}/lib/systemd/network/99-open5gs.netdev
%{_prefix}/lib/systemd/network/99-open5gs.network
%dir %{_sysconfdir}/open5gs
%config(noreplace) %{_sysconfdir}/open5gs/*.yaml
%dir %{_sysconfdir}/open5gs/hnet
%config(noreplace) %attr(0640,root,open5gs) %{_sysconfdir}/open5gs/hnet/*.key
%dir %{_sysconfdir}/open5gs/tls
%config(noreplace) %{_sysconfdir}/open5gs/tls/*.crt
%config(noreplace) %attr(0640,root,open5gs) %{_sysconfdir}/open5gs/tls/*.key
%dir %{_sysconfdir}/freeDiameter
%config(noreplace) %{_sysconfdir}/freeDiameter/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/open5gs
%dir %attr(0755,open5gs,open5gs) %{_localstatedir}/log/open5gs
%dir %attr(0755,open5gs,open5gs) %{_localstatedir}/log/open5gs/tls

%changelog
%autochangelog
