Name:           goyq
Version:        4.30.6
Release:        1%{?dist}
Summary:        A yq implementation in Go

License:        MIT
URL:            https://github.com/mikefarah/yq
Source:         https://github.com/mikefarah/yq/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
Another implementation of yq but this time in Go

%global debug_package %{nil}
%prep
%autosetup -n yq-%{version}

%build
export CGO_CFLAGS="%{optflags} -fpie -fpic -shared" 
export CGO_LDFLAGS="%{build_ldflags} -Wl,-pie"
export CGO_CPPFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
go build -trimpath -buildmode=pie -mod=readonly -modcacherw -buildvcs=false -ldflags=-linkmode=external -o yq
strip --strip-all yq

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 yq $RPM_BUILD_ROOT/%{_bindir}/yq

%files
%{_bindir}/yq

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 4.30.6-1
- Initial revision
