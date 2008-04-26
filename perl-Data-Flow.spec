%define name perl-Data-Flow
%define module Data-Flow
%define version 1.01
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple-minded recipe-controlled build of data
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
Perl extension for simple-minded recipe-controlled build of data.

%prep

%setup -q -n %{module}-%{version} 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Data
%{perl_vendorlib}/auto/Data
%{_mandir}/*/*

