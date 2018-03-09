Name: barrier
Version: 1.9.0
#Version: 1.9.0-snapshot ###FIXME can't have a dash - in the version string
Summary: Keyboard and mouse sharing solution
Group: Applications/Productivity
URL: https://github.com/debauchee/barrier/
Source: https://github.com/debauchee/barrier/archive/v1.9.0-snapshot.tar.gz
# workaround the git versionning and set to Release instead of the default Debug
#Source1: build_env.sh
Vendor: Debauchee ### FIXME ###
Packager: Tru Huynh <tru@pasteur.fr>
License: GPLv2
Release: 1%{?dist}

# at least for CentOS-7 and CentOS-6
BuildRequires: git cmake3 make gcc gcc-c++ curl-devel  openssl-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: avahi-compat-libdns_sd-devel
BuildREquires: libXtst-devel libXinerama-devel libICE-devel libXrandr-devel

# possible issue here for cmake: on CentOS-7, cmake is cmake 2.x and barrier needs cmake 3.x
# which is available from EPEL as cmake3, that might not be the case for other RPMS based distro

# CXX14
%if 0%{?rhel} == 6
BuildRequires: centos-release-scl-rh devtoolset-3-gcc-c++.x86_64
%endif

%description
Barrier allows you to share one mouse and keyboard between multiple computers.
Work seamlessly across Windows, macOS and Linux.

%prep
%setup -n %{name}-1.9.0-snapshot

%build
cp dist/rpm/build_env.sh .

%if 0%{?rhel} == 6
scl enable devtoolset-3 ./clean_build.sh 
%endif

%if 0%{?rhel} == 7
./clean_build.sh 
%endif
# maybe need a default if/else for non rhel target :P

%install
# no make install, so manual install
%{__mkdir} -p %{buildroot}%{_bindir} %{buildroot}%{_datarootdir}/applications %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps
%{__install} -t %{buildroot}%{_datarootdir}/applications res/barrier.desktop
%{__install} -t %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps res/barrier.svg
%{__install} -t %{buildroot}%{_bindir} build/bin/{barrier,barrierc,barriers,barrierd,syntool}

%files
%defattr(755,root,root,-)
%{_bindir}/barrier
%{_bindir}/barrierc
%{_bindir}/barriers
%{_bindir}/barrierd
%{_bindir}/syntool
%attr(644,-,-) %{_datarootdir}/applications/barrier.desktop
%attr(644,-,-) %{_datarootdir}/icons/hicolor/scalable/apps/barrier.svg

%changelog
* Fri Mar  9 2018 Tru Huynh <tru@pasteur.fr> - barrier 2.0.0-1
- Initial rpm package for barrier
