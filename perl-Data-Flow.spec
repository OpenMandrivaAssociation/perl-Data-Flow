%define modname	Data-Flow
%define modver	1.02

Summary:	Simple-minded recipe-controlled build of data
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Data/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Perl extension for simple-minded recipe-controlled build of data.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Data
%{perl_vendorlib}/auto/Data
%{_mandir}/man3/*

