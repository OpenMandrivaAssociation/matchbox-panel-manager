%define name 	matchbox-panel-manager
%define version 0.1
%define release 1mdk

Summary: 	Manager for the Matchbox Desktop panel
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox.handhelds.org/
License: 	GPL
Group: 		Graphical desktop/Other
Source: 	ftp://ftp.handhelds.org/matchbox/sources/matchbox-panel-manager/%version/%{name}-%{version}.tar.bz2

Buildroot: 	%_tmppath/%name-%version-buildroot
BuildRequires:	matchbox-devel gtk2-devel
Requires:	matchbox-panel

%description
A GTK2 based manager for the Matchbox Dektop panel

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%_bindir/%name
%_datadir/applications/*
%_datadir/pixmaps/*

