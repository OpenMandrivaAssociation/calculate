%define name	calculate
%define version	1.00
%define release	%mkrel 10
%define	binname	calc

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Patch0:		calculate-1.00-gcc3-fix.patch.bz2
URL:		http://home.planetinternet.be/~esmee/calc01.html
Summary:	A simple command line calculator for the console

%description
A very simple console command line calculater.

%prep
%setup -q
%patch0 -p1 -b .gcc3

%build
%{__cxx} $RPM_OPT_FLAGS -o %{binname} %{name}.cpp

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -m755 %{binname} -D $RPM_BUILD_ROOT%{_bindir}/%{binname}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_bindir}/%{binname}

