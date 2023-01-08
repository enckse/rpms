Name:           revive
Version:        1.2.4
Release:        1%{?dist}
Summary:        An improved go lint runner

License:        MIT
URL:            https://github.com/mgechev/revive
Source0:        https://github.com/mgechev/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  git
BuildRequires:  make

%description
An improved golint and general go analyzer system

%global debug_package %{nil}
%prep
%autosetup
cp %{SOURCE1} .

%build
make -f go.Makefile BINARY=revive MORE_FLAGS="-ldflags=-linkmode=external"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 revive $RPM_BUILD_ROOT/%{_bindir}/revive

%files
%{_bindir}/revive

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 1.2.4-1
- Initial revision
