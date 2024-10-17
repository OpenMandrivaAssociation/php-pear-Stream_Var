%define		_class		Stream
%define		_subclass	Var
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.1.0
Release:	9
Summary:	Allows stream based access to any variable
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Stream_Var/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
%{upstream_name} can be registered as a stream with stream_register_wrapper 
and allows stream based access to any variable in any scope. Arrays are
treated as directories, so it`s possible to replace temporary
directories and files in your applications with variables.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-7mdv2012.0
+ Revision: 742279
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-6
+ Revision: 679583
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-5mdv2011.0
+ Revision: 613776
- the mass rebuild of 2010.1 packages

* Tue Nov 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-4mdv2010.1
+ Revision: 467088
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-3mdv2010.0
+ Revision: 452034
- fix %%postun

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-2mdv2010.0
+ Revision: 450204
- use pear installer
- use fedora %%post/%%postun

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 446484
- new version
- spec cleanup

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-10mdv2010.0
+ Revision: 441574
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2009.1
+ Revision: 322664
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2009.0
+ Revision: 237069
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.0-7mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2007.0
+ Revision: 82679
- Import php-pear-Stream_Var

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

