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
Requires:       libgit2
Requires:       git

%description
Static site generator for git version control

%global debug_package %{nil}
%prep
%autosetup


%build
%make_build


%install
%make_install DESTDIR="$RPM_BUILD_ROOT" MANPREFIX="%{_mandir}" PREFIX="%{_prefix}"
/usr/lib/rpm/brp-compress
/usr/lib/rpm/brp-strip
/usr/lib/rpm/brp-strip-comment-note

%files
%{_mandir}/man1/stagit*
%{_docdir}/*
%{_bindir}/stagit*

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com>
- Initial revision 1.2 build 
