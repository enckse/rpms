Name:           helix
Version:        22.12
Release:        1%{?dist}
Summary:        A post-modern modal text editor

License:        MPL-2.0
URL:            https://helix-editor.com
Source0:        https://github.com/helix-editor/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:			helix-runtimedir.patch
BuildRequires:  cargo
BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
A Kakoune / Neovim inspired editor, written in Rust.

%global debug_package %{nil}
%prep
%autosetup -N
%patch0 -p1
cargo fetch --locked

%build
cargo build --frozen --release
strip --strip-all target/release/hx
strip --strip-all runtime/grammars/*.so

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/%{name}/runtime/grammars
install -Dm755 target/release/hx $RPM_BUILD_ROOT/%{_bindir}/hx
cp -r runtime/queries $RPM_BUILD_ROOT/%{_libdir}/%{name}/runtime
cp -r runtime/themes $RPM_BUILD_ROOT/%{_libdir}/%{name}/runtime
cp -r runtime/grammars/*.so $RPM_BUILD_ROOT/%{_libdir}/%{name}/runtime/grammars/
chmod 644 $RPM_BUILD_ROOT/%{_libdir}/%{name}/runtime/grammars/*.so

%files
%{_bindir}/hx
%{_libdir}/%{name}/*

%changelog
* Wed Jan 11 2023 Sean Enck <enckse@voidedtech.com> - 22.12-1
- Initial revision
