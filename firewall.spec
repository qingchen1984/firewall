Name: firewall
Summary: ClearOS Firewall Engine
Version: 1.4.21
Release: 1%{?dist}
Vendor: ClearFoundation
Source: firewall-%{version}.tar.gz
Group: System Environment/Base
URL: http://www.clearfoundation.com/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
License: GPLv2
BuildRequires: libselinux-devel
BuildRequires: kernel-headers
BuildRequires: lua-devel
BuildRequires: iptables-devel = %{version}
BuildRequires: autoconf >= 2.63
BuildRequires: automake
BuildRequires: libtool
Conflicts: kernel < 2.4.20
Requires: iptables = %{version}

%description
The ClearOS Firewall Engine.  This is a customized version of iptables combined with the LUA interpreter.

%prep
%setup -q
./autogen.sh
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
./configure --bindir=/bin --sbindir=/sbin --sysconfdir=/etc --libdir=/%{_lib} --libexecdir=/%{_lib} --mandir=%{_mandir} --includedir=%{_includedir}

%build
# do not use rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot} 
mv %{buildroot}/sbin/firewall  %{buildroot}/sbin/app-firewall
mv %{buildroot}/sbin/firewall6  %{buildroot}/sbin/app-firewall6

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/sbin/app-firewall
/sbin/app-firewall6

%changelog
