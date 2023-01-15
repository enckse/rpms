Name:           goyq
Version:        4.30.8
Release:        1%{?dist}
Summary:        A yq implementation in Go

License:        MIT
URL:            https://github.com/mikefarah/yq
Source:         https://github.com/mikefarah/yq/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  git
BuildRequires:  make

%description
Another implementation of yq but this time in Go

%global debug_package %{nil}
%prep
%autosetup -n yq-%{version}
cp %{SOURCE1} .

%build
make -f go.Makefile BINARY=yq

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 yq $RPM_BUILD_ROOT/%{_bindir}/yq

%files
%{_bindir}/yq

%changelog
* Sun Jan 15 2023 Sean Enck <enckse@voidedtech.com> - 4.30.8-1
- Upstream update
* Sat Jan 14 2023 Sean Enck <enckse@voidedtech.com> - 4.30.7-1
- Upstream update
* Wed Jan 11 2023 Sean Enck <enckse@voidedtech.com> - 4.30.6-1
- Initial revision
