Summary:	Resource protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Resource i pomocnicze
Name:		xorg-proto-resourceproto
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/resourceproto-%{version}.tar.bz2
# Source0-md5:	b823b314e37eb19dae1f297951d2e933
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resource protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Resource i pomocnicze.

%package devel
Summary:	Resource protocol and ancillary headers
Summary(pl.UTF-8):   Nagłówki protokołu Resource i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	resourceext

%description devel
Resource protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Resource i pomocnicze.

%prep
%setup -q -n resourceproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/resourceproto.pc
