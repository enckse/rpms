Name:           revive
Version:        1.2.4
Release:        1%{?dist}
Summary:        An improved go lint runner

License:        MIT
URL:            https://github.com/mgechev/revive
Source:         https://github.com/mgechev/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
An improved golint and general go analyzer system

%global debug_package %{nil}
%prep
%autosetup

%build
export CGO_CFLAGS="%{optflags} -fpie -fpic -shared" 
export CGO_LDFLAGS="%{build_ldflags} -Wl,-pie"
export CGO_CPPFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
go build -trimpath -buildmode=pie -mod=readonly -modcacherw -buildvcs=false -ldflags=-linkmode=external
strip --strip-all revive

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 revive $RPM_BUILD_ROOT/%{_bindir}/revive

%files
%{_bindir}/revive

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 1.2.4-1
- Initial revision
