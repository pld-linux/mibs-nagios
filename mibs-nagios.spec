Summary:	MIBs for Nagios
Name:		net-snmp-mibs-nagios
Version:	1.0.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/nagiosplug/nagiosmib-%{version}.tar.gz
# Source0-md5:	c8ecd90e1bc0ddbce4aaa0b35ee89c24
URL:		http://sourceforge.net/projects/nagiosplug/
Requires:	net-snmp-mibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mibdir	%{_datadir}/snmp/mibs

%description
Objects for Nagios(tm) events. There are 2 primary tables reflecting
the division in Nagios for Host events and Service events.

The event tables are extended by the HostNotifyTable and the
ServiceNotifyTable to keep track of the notifications based on events.

The tables entries themselves are not accessible but are used for OID
entries for TRAP/INFORM notifications.

These objects are based on the macros defined in Nagios v2.0

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
