Name:           filebrowser
Version:        2.23.0
Release:        1%{?dist}
Summary:        Web-based file browser application

License:        Apache-2.0
URL:            https://filebrowser.org
Source:         https://github.com/filebrowser/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        go.Makefile
BuildRequires:  go
BuildRequires:  npm
BuildRequires:  make

%description
Filebrowser provides a file managing interface within a specified directory and 
it can be used to upload, delete, preview, rename and edit your files. It allows 
the creation of multiple users and each user can have its own directory. 
It can be used as a standalone app.

%global debug_package %{nil}
%prep
%autosetup
cp %{SOURCE1} .

%build
export NODE_OPTIONS="--openssl-legacy-provider"
cd frontend
npm install
npm update
npm run build
cd ..
make -f go.Makefile BINARY=filebrowser

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -Dm755 filebrowser $RPM_BUILD_ROOT/%{_bindir}/filebrowser

%files
%{_bindir}/filebrowser

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 2.23.0-1
- Initial revision
