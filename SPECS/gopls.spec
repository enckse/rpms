Name:           gopls
Version:        0.11.0
Release:        1%{?dist}
Summary:        Go LSP implementation

License:        BSD
URL:            https://github.com/golang/tools
Source:         https://github.com/golang/tools/archive/gopls/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  go
BuildRequires:  git

%description
An implementation of the Language Server Protocol for Go

%global debug_package %{nil}
%prep
%autosetup -n tools-gopls-v%{version}/gopls

%build
export CGO_CFLAGS="%{optflags} -fpie -fpic -shared" 
export CGO_LDFLAGS="%{build_ldflags} -Wl,-pie"
export CGO_CPPFLAGS="%{optflags}"
export CGO_CXXFLAGS="%{optflags}"
go build -trimpath -buildmode=pie -mod=readonly -modcacherw -buildvcs=false -ldflags=-linkmode=external -o gopls
strip --strip-all gopls

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 gopls $RPM_BUILD_ROOT/%{_bindir}/gopls

%files
%{_bindir}/gopls

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 0.11.0-1
- Initial revision
