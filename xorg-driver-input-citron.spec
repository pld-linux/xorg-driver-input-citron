Summary:	X.org input driver for Citron Infrared Touch (CiTouch) devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla ekranów dotykowych Citron Infrared Touch (CiTouch)
Name:		xorg-driver-input-citron
Version:	2.2.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-citron-%{version}.tar.bz2
# Source0-md5:	4e254fcefb3bea55772e63c12570f6d9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel >= 1.4.1
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.4
BuildRequires:	rpmbuild(macros) >= 1.389
%requires_xorg_xserver_xinput
Requires:	xorg-xserver-server >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Citron Infrared Touch (CiTouch). This driver
supports the following devices: IRT6I5-V2.x, IRT10I4-V4.x,
IRT12I1-V2.x, IRT15I1-V1.x, IRT65-V3.x, IRT84-V2.x, IRT104-V5.x,
IRT104-V6.x, IRT121-V3.x, IRT15I1-V1.x, IRT170-V1.x, IRT181-V1.x,
IRT190-V1.x.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla ekranów dotykowych Citron Infrared Touch
(CiTouch). Obsługuje następujące urządzenia: IRT6I5-V2.x,
IRT10I4-V4.x, IRT12I1-V2.x, IRT15I1-V1.x, IRT65-V3.x, IRT84-V2.x,
IRT104-V5.x, IRT104-V6.x, IRT121-V3.x, IRT15I1-V1.x, IRT170-V1.x,
IRT181-V1.x, IRT190-V1.x.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/citron_drv.so
%{_mandir}/man4/citron.4*
