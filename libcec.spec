%define snap 20120917

%define major 1
%define libname %mklibname cec %{major}
%define devname %mklibname cec -d

Name:		libcec
Version:	1.9.0
Release:	%mkrel -c git%{snap} 1
Summary:	Pulse-Eight CEC adapter control library
License:	GPLv2+
Group:		System/Libraries
URL:		http://libcec.pulse-eight.com/
# rm -rf libcec && git clone git://github.com/Pulse-Eight/libcec.git && cd libcec/
# git archive --prefix=libcec-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../libcec-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{snap}.tar.xz
BuildRequires:	pkgconfig(libudev)
BuildRequires:	lockdev-devel

%description
With libcec you can access your Pulse-Eight CEC adapter.

%package -n cec-utils
Summary:	Utilities for Pulse-Eight CEC adapter control
Group:		System/Configuration/Hardware
# the binaries require the library, but automatic dependency generation doesn't
# catch that
Requires:	%{libname} = %{EVRD}

%description -n cec-utils
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the command-line tools to configure and test your
Pulse-Eight CEC adapter.

%package -n %{libname}
Summary:	Shared library for Pulse-Eight CEC adapter control
Group:		System/Libraries

%description -n %{libname}
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the shared library which allows programs to access your
Pulse-Eight CEC adapter.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	cec-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %devname
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the files for developing applications which
will use libcec.

%prep
%setup -q -n %{name}-%{snap}

%build
autoreconf -ifv
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n cec-utils
%{_bindir}/cec-client
%{_bindir}/cec-config

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/*.h
