Name:           mblaze
Version:        1.2
Release:        1%{?dist}
Summary:        Unix utilities to deal with Maildir

License:        Custom:Public Domain
URL:            https://github.com/leahneukirchen/mblaze/
Source0:        https://github.com/leahneukirchen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
Requires:       bash
Requires:       gawk

%description
The mblaze message system is a set of Unix utilities for processing and
interacting with mail messages which are stored in maildir folders

%prep
%autosetup

%build
%set_build_flags
%make_build

%install
%make_install DESTDIR="$RPM_BUILD_ROOT" PREFIX="%{_prefix}"

%files
%{_bindir}/m*
%{_mandir}/man1/m*
%{_mandir}/man5/m*
%{_mandir}/man7/m*

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 1.2-1
- Initial revision
