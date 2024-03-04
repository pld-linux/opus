#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	IETF Opus Interactive Audio Codec
Summary(pl.UTF-8):	Opus - interaktywny kodek dźwięku wg projektu IETF
Name:		opus
Version:	1.5
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	1b5270628bc6b1e9dd1a5a29ff697c64
URL:		https://opus-codec.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.527
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

%package apidocs
Summary:	API documentation for OPUS library
Summary(pl.UTF-8):	Dokumentacja API biblioteki OPUS
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for OPUS library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki OPUS.

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
	--disable-silent-rules \
	%{__enable_disable static_libs static}
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
%attr(755,root,root) %{_libdir}/libopus.so
%{_libdir}/libopus.la
%{_includedir}/opus
%{_pkgconfigdir}/opus.pc
%{_aclocaldir}/opus.m4
%{_mandir}/man3/opus_*.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopus.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/html/{search,*.css,*.html,*.js,*.png}
