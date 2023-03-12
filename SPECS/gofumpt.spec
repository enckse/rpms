Name:           gofumpt
Version:        0.4.0
Release:        1%{?dist}
Summary:        Stricter gofmt

License:        BSD-3-Clause
URL:            https://github.com/mvdan/gofumpt
Source:         https://github.com/mvdan/gofumpt/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
Like gofmt but stricter/added formatting rules

%global debug_package %{nil}
%prep
%autosetup

%build
go build %{_goflags} -o gofumpt
strip --strip-all gofumpt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 gofumpt $RPM_BUILD_ROOT/%{_bindir}/gofumpt

%files
%{_bindir}/gofumpt

%changelog
* Sat Jan 28 2023 Sean Enck <enckse@voidedtech.com> - 0.4.0-1
- Initial revision
