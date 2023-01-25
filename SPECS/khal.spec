Name:       khal
Version:    0.10.5
Release:    1%{?dist}
Summary:    CLI calendar application

License:    MIT
URL:        https://github.com/pimutils/khal
Source0:    https://files.pythonhosted.org/packages/source/k/%{name}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: make
BuildRequires:  python3-devel
BuildRequires:  python3-configobj
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-sphinx

Requires:       python3-click >= 3.2
Requires:       python3-configobj
Requires:       python3-dateutil
Requires:       python3-icalendar
Requires:       python3-urwid
Requires:       python3-tzlocal
Requires:       python3-pytz
Requires:       python3-pyxdg

%description
Khal is a standards based CLI (console) calendar program. CalDAV compatibility
is achieved by using vdir/vdirsyncer as a back-end, allowing syncing of
calendars with a variety of other programs on a host of different platforms.

%prep
%setup -q

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%{python3_sitelib}/*
%{_bindir}/ikhal
%{_bindir}/khal

%changelog
* Wed Jan 25 2023 Sean Enck <enckse@voidedtech.com> - 0.10.5-1
- Initial revision
