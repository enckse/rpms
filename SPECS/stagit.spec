Name:           stagit
Version:        1.2
Release:        1%{?dist}
Summary:        Static site generator for git version control

License:        MIT
URL:            https://codemadness.org/stagit.html
Source0:        https://codemadness.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:			stagit-owner.patch
Patch1:			stagit-time.patch

BuildRequires:  libgit2-devel
BuildRequires:  gcc
BuildRequires:  make
Requires:       git

%description
Static site generator for git version control

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fpie -fpic -shared" 
export LDFLAGS="%{build_ldflags} -Wl,-pie"
%make_build

%install
%make_install DESTDIR="$RPM_BUILD_ROOT" MANPREFIX="%{_mandir}" PREFIX="%{_prefix}"

%files
%{_mandir}/man1/stagit*
%{_docdir}/*
%{_bindir}/stagit*

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 1.2-1
- Initial revision
