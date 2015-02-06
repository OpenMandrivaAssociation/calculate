%define name	calculate
%define version	1.00
%define release	15
%define	binname	calc

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source0:	%{name}-%{version}.tar.bz2
Patch0:		calculate-1.00-gcc3-fix.patch.bz2
URL:		http://home.planetinternet.be/~esmee/calc01.html
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.00-14mdv2011.0
+ Revision: 616910
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.00-13mdv2010.0
+ Revision: 424740
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.00-12mdv2009.0
+ Revision: 243422
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.00-10mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import calculate


* Wed Aug 02 2006 Lenny Cartier <lenny@mandriva.com> 1.00-10mdv2007.0
- rebuild

* Tue Dec 07 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-9mdk
- arg, screwed up P0 in last release, redo it

* Tue Dec 07 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-8mdk
- rebuild

* Fri Jun 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.00-7mdk
- rebuild

* Sat Jan 10 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.00-6mdk
- rebuild

* Thu Feb 27 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.00-5mdk
- Back in contribs!:)
- Updated for gcc 3 (Patch0)
- Cleanups
- Added my own little README(mainly to satisfy rpmlint)

* Thu Jan 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.00-4mdk
- rebuild

* Fri Jan 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.00-3mdk
- rebuilt

* Mon Jul 31 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.00-2mdk
- use new macros
- handle mdk optimization

* Tue Jun 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 1.00-1mdk
- Packaged for Mandrake
- Created Spec file
