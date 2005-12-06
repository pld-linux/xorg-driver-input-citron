Summary:	X.org input driver for Citron Infrared Touch (CiTouch) devices
Summary(pl):	Sterownik wej¶ciowy X.org dla ekranów dotykowych Citron Infrared Touch (CiTouch)
Name:		xorg-driver-input-citron
Version:	2.1.1.3
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/driver/xf86-input-citron-%{version}.tar.bz2
# Source0-md5:	fad378f536423e9812db6e6c13f6d987
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Citron Infrared Touch (CiTouch).

%description -l pl
Sterownik wej¶ciowy X.org dla ekranów dotykowych Citron Infrared Touch
(CiTouch).

%prep
%setup -q -n xf86-input-citron-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/citron_drv.so
%{_mandir}/man4/citron.4*
