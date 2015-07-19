%define major	2
%define libname	%mklibname cec %{major}
%define devname	%mklibname cec -d

Summary:	Pulse-Eight CEC adapter control library
Name:		libcec
Version:	2.2.0
Release:	3
License:	GPLv2+
Group:		System/Libraries
Url:		http://libcec.pulse-eight.com/
Source0:	%{name}-%{version}.tar.xz
Patch0:		libcec-2.2.0-imx6-support.patch
BuildRequires:	lockdev-devel
BuildRequires:	pkgconfig(libudev)

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
This package contains the shared library which allows programs to access your
Pulse-Eight CEC adapter.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
With libcec you can access your Pulse-Eight CEC adapter.

This package contains the files for developing applications which
will use libcec.

%prep
%setup -q
%patch0 -p1 -b .imx6~
./bootstrap

%build
%configure \
%ifarch %{arm}
		--enable-imx6
%endif

%make

%install
%makeinstall_std

%files -n cec-utils
%{_bindir}/cec-client

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/*.h
