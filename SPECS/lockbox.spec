%{?!bash_completions_dir:%global bash_completions_dir %{_datadir}/bash-completion/completions}

Name:           lockbox
Version:        1.0.0
Release:        1%{?dist}
Summary:        Password manager/storage

License:        GPLv3
URL:            https://github.com/enckse/lockbox
Source0:        https://github.com/enckse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git
BuildRequires:  pkgconfig(bash-completion)

%description
Fast, configurable, extensible, flexible, and beautiful linter for Go.
Drop-in replacement of golint. Revive provides a framework for 
development of custom rules, and lets you define a strict preset 
for enhancing your development & code review processes.

%global debug_package %{nil}
%prep
%autosetup

%build
go build %{_goflags} -o lb cmd/main.go
strip --strip-all lb
./lb bash > lb.bash

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 lb $RPM_BUILD_ROOT/%{_bindir}/lb
install -Dm644 lb.bash $RPM_BUILD_ROOT/%{bash_completions_dir}/lb

%files
%{_bindir}/lb
%{bash_completions_dir}/lb

%changelog
* Fri Mar 10 2023 Sean Enck <enckse@voidedtech.com> - 1.0.0-1
- New release
* Sat Jan 21 2023 Sean Enck <enckse@voidedtech.com> - 23.01.02-3
- Fixing manpages
* Sat Jan 21 2023 Sean Enck <enckse@voidedtech.com> - 23.01.02-2
- Including manpages
* Sat Jan 21 2023 Sean Enck <enckse@voidedtech.com> - 23.01.02-1
- Updated version
* Sat Jan 21 2023 Sean Enck <enckse@voidedtech.com> - 23.01.01-1
- Updated version
* Tue Jan 17 2023 Sean Enck <enckse@voidedtech.com> - 23.01.00-1
- Updated version
* Wed Jan 11 2023 Sean Enck <enckse@voidedtech.com> - 22.12.05-1
- Initial revision
