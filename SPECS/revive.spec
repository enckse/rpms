Name:           revive
Version:        1.2.5
Release:        1%{?dist}
Summary:        An improved go lint runner

License:        MIT
URL:            https://github.com/mgechev/revive
Source0:        https://github.com/mgechev/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
Fast, configurable, extensible, flexible, and beautiful linter for Go.
Drop-in replacement of golint. Revive provides a framework for 
development of custom rules, and lets you define a strict preset 
for enhancing your development & code review processes.

%global debug_package %{nil}
%prep
%autosetup

%build
go build %{_goflags} -o revive
strip --strip-all revive

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 revive $RPM_BUILD_ROOT/%{_bindir}/revive

%files
%{_bindir}/revive

%changelog
* Mon Feb 06 2023 Sean Enck <enckse@voidedtech.com> - 1.2.5-1
- Initial revision
