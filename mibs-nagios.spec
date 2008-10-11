Summary:	MIBs for Nagios
Name:		net-snmp-mibs-nagios
Version:	1.0.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/nagiosplug/nagiosmib-%{version}.tar.gz
# Source0-md5:	88a74f2bda5440a70a3f8e29b9c82628
URL:		http://sourceforge.net/projects/nagiosplug/
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/snmp/mibs

%description
MIBs for Nagios.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{mibdir}
cp -a MIB/*-MIB $RPM_BUILD_ROOT%{mibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{mibdir}/*
