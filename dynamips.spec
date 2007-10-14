#
%define		_rc	RC2
#
Summary:	Cisco 7200 Simulator
Summary(pl.UTF-8):	Symulator Cisco 7200
Name:		dynamips
Version:	0.2.8
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.ipflow.utc.fr/dynamips/%{name}-%{version}-%{_rc}.tar.gz
# Source0-md5:	8d12d28684d164fe3312a3fe43c84d2e
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-debian.patch
URL:		http://www.ipflow.utc.fr/index.php/Cisco_7200_Simulator
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cisco 7200 Simulator.

%description -l pl.UTF-8
Symulator Cisco 7200.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch0 -p1
%patch1 -p1

%build
%ifarch %{x8664}
ARCH=amd64
%else
%ifarch %{ix86}
ARCH=x86
%else
ARCH=nojit
%endif
%endif

%{__make} \
	DYNAMIPS_ARCH=$ARCH \
	CC="%{__cc}" \
	RPM_CFLAGS="%{rpmcflags}" \
	LD="%{__ld}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX="%{_prefix}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.hypervisor ChangeLog TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*
