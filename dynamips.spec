Summary:	Cisco 7200 Simulator
Summary(pl.UTF-8):	Symulator Cisco 7200
Name:		dynamips
Version:	0.2.5
Release:	0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.ipflow.utc.fr/dynamips/%{name}-%{version}.tar.gz
# Source0-md5:	b87ef442f7537373ccbe69c3f6dca301
Patch0:		%{name}-Makefile.patch
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
%setup -q
%patch0 -p0

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
	LD="%{__ld}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install dynamips $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
