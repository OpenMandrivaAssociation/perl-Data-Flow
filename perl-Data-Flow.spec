%define upstream_name    Data-Flow
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simple-minded recipe-controlled build of data
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl extension for simple-minded recipe-controlled build of data.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Data
%{perl_vendorlib}/auto/Data
%{_mandir}/*/*


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.20.0-2mdv2011.0
+ Revision: 681373
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.20.0-1mdv2011.0
+ Revision: 403042
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.02-2mdv2009.0
+ Revision: 268409
- rebuild early 2009.0 package (before pixel changes)

* Tue May 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2009.0
+ Revision: 206816
- update to new version 1.02
- new version

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.09-3mdv2008.1
+ Revision: 135831
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.09-3mdv2008.0
+ Revision: 67484
- buildrequires obsoletes buildprereq


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.09-3mdv2007.0
- rebuild

* Tue Jul 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.09-2mdk
- rebuild

* Wed Jun 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.09-1mdk
- initial package

