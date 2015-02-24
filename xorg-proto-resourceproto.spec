Summary:	Resource extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Resource
Name:		xorg-proto-resourceproto
Version:	1.2.0
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/resourceproto-%{version}.tar.bz2
# Source0-md5:	cfdb57dae221b71b2703f8e2980eaaf4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Resource extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Resource.

%package devel
Summary:	Resource extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Resource
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	resourceext

%description devel
Resource extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Resource.

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README resproto.txt
%{_includedir}/X11/extensions/XResproto.h
%{_pkgconfigdir}/resourceproto.pc
