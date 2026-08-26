# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: kiritakekumi <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libidn
Version:        1.44
Release:        %autorelease
Summary:        Internationalized string processing library (IDNA2003)
# The shared library is dual licensed LGPLv2.1+ or LGPLv3+, the idn command
# line tool is GPLv3+.
License:        (LGPL-2.1-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/libidn/
#!RemoteAsset:  sha256:499608bab3a65650a0ea52888c13a8deebe3f71408e319acd9ec52e02eb13959
Source:         https://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-csharp
BuildOption(conf):  --disable-java
BuildOption(conf):  --disable-gtk-doc
BuildOption(conf):  --disable-rpath
BuildOption(conf):  --with-lispdir=%{_datadir}/emacs/site-lisp

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  texinfo

%description
GNU Libidn is an implementation of the Stringprep, Punycode and IDNA 2003
specifications, used to encode and decode internationalized domain names.

It is a hard dependency of freeDiameter (and therefore of Open5GS), which
uses idna_to_ascii_8z() to normalize Diameter identities.  Note that libidn2
implements the newer IDNA2008 specification with an incompatible API and is
not a drop-in replacement.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, the pkg-config file and the API
manual pages needed to develop applications that use GNU Libidn.

%install -a
%find_lang %{name}
find %{buildroot} -name '*.la' -delete

%files -f %{name}.lang
%license COPYING COPYINGv2 COPYING.LESSERv2 COPYING.LESSERv3
%doc AUTHORS NEWS README THANKS
%{_bindir}/idn
%{_libdir}/libidn.so.*
%{_datadir}/emacs/site-lisp/idna.el
%{_datadir}/emacs/site-lisp/punycode.el
%{_infodir}/libidn.info*
%{_infodir}/libidn-components.png
%{_mandir}/man1/idn.1*

%files devel
%{_includedir}/idn-free.h
%{_includedir}/idn-int.h
%{_includedir}/idna.h
%{_includedir}/pr29.h
%{_includedir}/punycode.h
%{_includedir}/stringprep.h
%{_includedir}/tld.h
%{_libdir}/libidn.so
%{_libdir}/pkgconfig/libidn.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
