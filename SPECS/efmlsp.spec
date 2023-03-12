Name:           efmlsp
Version:        0.0.44
Release:        1%{?dist}
Summary:        General purpose language server

License:        MIT
URL:            https://github.com/mattn/efm-langserver
Source:         https://github.com/mattn/efm-langserver/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  git
BuildRequires:  make

%description
General purpose Language Server that can use specified error
message format generated from specified command.
This is useful for editing code with linter.

%global debug_package %{nil}
%prep
%autosetup -n efm-langserver-%{version}
cp %{SOURCE1} .

%build
make -f go.Makefile BINARY=efm-langserver

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 efm-langserver $RPM_BUILD_ROOT/%{_bindir}/efm-langserver

%files
%{_bindir}/efm-langserver

%changelog
* Mon Jan 23 2023 Sean Enck <enckse@voidedtech.com> - 0.0.44-1
- Initial revision
