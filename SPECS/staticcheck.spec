Name:           staticcheck
Version:        2023.1
Release:        1%{?dist}
Summary:        Performs static checking against go projects

License:        MIT
URL:            https://github.com/dominikh/go-tools
Source:         https://github.com/dominikh/go-tools/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  git
BuildRequires:  make

%description
Staticcheck is a state of the art linter for the Go
programming language. Using static analysis, it finds
bugs and performance issues, offers simplifications, 
and enforces style rules.

%global debug_package %{nil}
%prep
%autosetup -n go-tools-%{version}
cp %{SOURCE1} .

%build
make -f go.Makefile BINARY=bin/staticcheck SRC=./cmd/staticcheck

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 bin/staticcheck $RPM_BUILD_ROOT/%{_bindir}/staticcheck

%files
%{_bindir}/staticcheck

%changelog
* Fri Feb 03 2023 Sean Enck <enckse@voidedtech.com> - 2023.1-1
- New release
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 2022.1.3-1
- Initial revision
