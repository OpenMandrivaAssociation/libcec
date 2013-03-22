%define major 2
%define libname %mklibname cec %{major}
%define devname %mklibname cec -d

Name:		libcec
Version:	2.1.1
Release:	1
Summary:	Pulse-Eight CEC adapter control library
License:	GPLv2+
Group:		System/Libraries
URL:		http://libcec.pulse-eight.com/
Source0:	%{name}-%{version}.tar.bz2
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

%files -n cec-utils
%{_bindir}/cec-client

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for Pulse-Eight CEC adapter control
Group:		System/Libraries

%description -n %{libname}
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the shared library which allows programs to access your
Pulse-Eight CEC adapter.

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	cec-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the files for developing applications which
will use libcec.

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/*.h


#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -ifv
%configure2_5x --disable-static
%make

%install
%makeinstall_std

