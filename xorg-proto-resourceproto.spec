# $Rev: 3293 $, $Date: 2005-08-17 20:16:28 $
#
Summary:	Resource protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Resource i pomocnicze
Name:		xorg-proto-resourceproto
Version:	1.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/resourceproto-%{version}.tar.bz2
# Source0-md5:	83faf6d7e354848e8ec1bdd5d89ab7a4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/resourceproto-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Resource protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Resource i pomocnicze.


%package devel
Summary:	Resource protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Rsource i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Obsoletes:	resourceext

%description devel
Resource protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Resource i pomocnicze.


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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/resourceproto.pc
