%{?!bash_completions_dir:%global bash_completions_dir %{_datadir}/bash-completion/completions}

Name:           lockbox
Version:        23.01.02
Release:        2%{?dist}
Summary:        Password manager/storage

License:        GPLv3
URL:            https://github.com/enckse/lockbox
Source0:        https://github.com/enckse/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  git
BuildRequires:  make
BuildRequires:  help2man
BuildRequires:  pkgconfig(bash-completion)

%description
Fast, configurable, extensible, flexible, and beautiful linter for Go.
Drop-in replacement of golint. Revive provides a framework for 
development of custom rules, and lets you define a strict preset 
for enhancing your development & code review processes.

%global debug_package %{nil}
%prep
%autosetup
cp %{SOURCE1} .

%build
make -f go.Makefile BINARY=lb SRC=cmd/main.go MORE_FLAGS="-ldflags=-linkmode=external"
make BUILD=./ lb.man
./lb bash > lb.bash

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir} $RPM_BUILD_ROOT/%{_mandir}/man1
install -Dm755 lb $RPM_BUILD_ROOT/%{_bindir}/lb
install -Dm644 lb.bash $RPM_BUILD_ROOT/%{bash_completions_dir}/lb
install -Dm644 lb.man $RPM_BUILD_ROOT/%{_mandir}/man1/lb

%files
%{_bindir}/lb
%{bash_completions_dir}/lb
%{_mandir}/man1/lb*

%changelog
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
