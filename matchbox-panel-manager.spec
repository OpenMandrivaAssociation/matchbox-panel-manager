%define name 	matchbox-panel-manager
%define version 0.1
%define release %mkrel 6

Summary: 	Manager for the Matchbox Desktop panel
Name: 		%name
Version: 	%version
Release: 	%release
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: 	http://matchbox-project.org/sources/%version/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel gtk2-devel
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
