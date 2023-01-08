Name:           staticcheck
Version:        2022.1.3
Release:        1%{?dist}
Summary:        Performs static checking against go projects

License:        MIT
URL:            https://github.com/dominikh/go-tools
Source:         https://github.com/dominikh/go-tools/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
In-depth go source code static analyzer and checker

%global debug_package %{nil}
%prep
%autosetup -n go-tools-%{version}

%build
export CGO_CFLAGS="%{optflags} -fpie -fpic -shared" 
export CGO_LDFLAGS="%{build_ldflags} -Wl,-pie"
export CGO_CPPFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
go build -trimpath -buildmode=pie -mod=readonly -modcacherw -buildvcs=false -ldflags=-linkmode=external -o bin/staticcheck ./cmd/staticcheck
strip --strip-all bin/staticcheck

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 bin/staticcheck $RPM_BUILD_ROOT/%{_bindir}/staticcheck

%files
%{_bindir}/staticcheck

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 2022.1.3-1
- Initial revision
