Summary:	IETF Opus Interactive Audio Codec
Summary(pl.UTF-8):	Opus - interaktywny kodek dźwięku wg projektu IETF
Name:		opus
Version:	0.9.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
# Source0-md5:	934226d4f572d01c5848bd70538248f5
Patch0:		%{name}-link.patch
Patch1:		%{name}-celt-rename.patch
URL:		http://opus-codec.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
# for tools
BuildRequires:	libogg-devel
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
%patch0 -p1
%patch1 -p1

%build
cd celt
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../silk
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for f in Decoder Encoder signalCompare ; do
	mv $RPM_BUILD_ROOT%{_bindir}/$f $RPM_BUILD_ROOT%{_bindir}/opus-$f
done
%{__rm} $RPM_BUILD_ROOT%{_bindir}/celt{dec,enc}
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/celt
%{__rm} $RPM_BUILD_ROOT%{_pkgconfigdir}/celt.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO
%attr(755,root,root) %{_bindir}/opus-Decoder
%attr(755,root,root) %{_bindir}/opus-Encoder
%attr(755,root,root) %{_bindir}/opus-signalCompare
%attr(755,root,root) %{_libdir}/libSKP_SILK_SDK.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSKP_SILK_SDK.so.0
%attr(755,root,root) %{_libdir}/libietfcodec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libietfcodec.so.0
%attr(755,root,root) %{_libdir}/libopuscelt0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopuscelt0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSKP_SILK_SDK.so
%attr(755,root,root) %{_libdir}/libietfcodec.so
%attr(755,root,root) %{_libdir}/libopuscelt0.so
%{_libdir}/libSKP_SILK_SDK.la
%{_libdir}/libietfcodec.la
%{_libdir}/libopuscelt0.la
%{_includedir}/opus
%{_includedir}/silk

%files static
%defattr(644,root,root,755)
%{_libdir}/libSKP_SILK_SDK.a
%{_libdir}/libietfcodec.a
%{_libdir}/libopuscelt0.a
