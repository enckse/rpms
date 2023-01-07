Name:           isync
Version:        1.4.4
Release:        1%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes

License:        GPLv2+
URL:            https://isync.sourceforge.io/
Source:         https://prdownloads.sourceforge.net/isync/%{name}-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  libdb-devel
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  make

Requires:       cyrus-sasl

%description
mbsync is a command line application which synchronizes mailboxes. Currently
Maildir and IMAP4 mailboxes are supported. New messages, message deletions
and flag changes can be propagated both ways. mbsync is suitable for use in
IMAP-disconnected mode.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install docdir=%{_docdir}/%{name}
rm -r %{buildroot}%{_defaultdocdir}

%files
%{_bindir}/mdconvert
%{_bindir}/mbsync-get-cert
%{_bindir}/mbsync
%{_mandir}/man1/*

%changelog
* Sat Jan 07 2023 Sean Enck <enckse@voidedtech.com> - 1.4.4-1
- Initial revision
