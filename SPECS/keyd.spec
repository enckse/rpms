%global libinput_overrides %{_sysconfdir}/libinput/local-overrides.quirks
Name:           keyd
Version:        2.4.2
Release:        2%{?dist}
Summary:        A key remapping daemon for linux
License:        MIT
URL:            https://github.com/rvaiya/keyd
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        keyd.default.conf
BuildRequires:  gcc
BuildRequires: systemd-rpm-macros
Requires:       python3-xlib
Requires(postun): sed
Requires(postun): shadow
Requires(pre):  shadow

%description
Linux lacks a good key remapping solution.
In order to achieve satisfactory results a medley of tools need to be employed
(e.g xcape, xmodmap) with the end result often being tethered to a specified
environment (X11).
keyd attempts to solve this problem by providing a flexible system wide daemon
which remaps keys using kernel level input primitives (evdev, uinput).

%prep
%setup -q

%build
%make_build

%install
install -m755 -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/layouts %{buildroot}%{_mandir}/man1 %{buildroot}%{_unitdir} %{buildroot}%{_sysconfdir}/%{name}
install -m755 bin/* %{buildroot}%{_bindir}
install -m644 data/keyd.compose keyd.quirks %{buildroot}%{_datadir}/%{name}
install -m644 layouts/* %{buildroot}%{_datadir}/%{name}/layouts
install -m644 data/*.1.gz %{buildroot}%{_mandir}/man1/
install -m644 %{name}.service %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/defaults.conf

%files
%license LICENSE
%doc README.md docs/*.md
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_unitdir}/%{name}.service
%{_sysconfdir}/%{name}/*

%pre
getent group keyd >/dev/null 2>&1 || groupadd keyd

%post
%systemd_post %{name}.service
if [ $1 -eq 1 -a -d %{_datadir}/libinput* ]; then
    # performed only on install
    mkdir -p %{_sysconfdir}/libinput
    echo "# added by %{name} package: START" >> %{libinput_overrides}
    cat %{_datadir}/%{name}/keyd.quirks >> %{libinput_overrides}
    echo "# added by %{name} package: END" >> %{libinput_overrides}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
if [ $1 -eq 0 ]; then
    # performed only on uninstall
    getent group keyd >/dev/null 2>&1 && groupdel keyd
    sed -i -e '/# added by %{name} package: START/,/# added by %{name} package: END/d' %{libinput_overrides} 2> /dev/null || :
    # remove file if it exists and is empty and remove libinput dir if empty
    if [ -f %{libinput_overrides} -a ! -s %{libinput_overrides} ]; then
	rm %{libinput_overrides}
	rm -d %{_sysconfdir}/libinput 2> /dev/null || :
    fi
fi

%changelog
* Fri Mar 10 2023 Sean Enck <enckse@voidedtech.com> - 2.4.2-2
- Include config
* Fri Mar 10 2023 Sean Enck <enckse@voidedtech.com> - 2.4.2-1
- Init release
