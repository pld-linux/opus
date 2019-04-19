Summary:	IETF Opus Interactive Audio Codec
Summary(pl.UTF-8):	Opus - interaktywny kodek dźwięku wg projektu IETF
Name:		opus
Version:	1.3.1
Release:	1
License:	BSD
Group:		Libraries
# releases <= 1.2 also on
#Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
Source0:	https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz
# Source0-md5:	d7c07db796d21c9cf1861e0c2b0c0617
URL:		http://opus-codec.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Opus codec is designed for interactive speech and audio
transmission over the Internet. It is designed by the IETF Codec
Working Group and incorporates technology from Skype's SILK codec and
Xiph.Org's CELT codec.

%description -l pl.UTF-8
Kodek Opus został zaprojektowany do interaktywnej transmisji mowy i
dźwięku przez Internet. Zaprojektowała go IETC Codec Working Group,
łącząc technologię z kodeka SILK Skype'a i kodeka CELT Xiph.Org.

%package devel
Summary:	Header files for OPUS libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OPUS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OPUS libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OPUS.

%package static
Summary:	Static OPUS libraries
Summary(pl.UTF-8):	Statyczne biblioteki OPUS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OPUS libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OPUS.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-custom-modes \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/opus/html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libopus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopus.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/html/*
%attr(755,root,root) %{_libdir}/libopus.so
%{_libdir}/libopus.la
%{_includedir}/opus
%{_pkgconfigdir}/opus.pc
%{_aclocaldir}/opus.m4
%{_mandir}/man3/opus_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libopus.a
