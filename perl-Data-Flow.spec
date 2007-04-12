%define name perl-Data-Flow
%define realname Data-Flow
%define version 0.09
%define release %mkrel 3

Summary:	Data-Flow module for perl 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source:		%{realname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildPreReq:	perl
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot

%description
Data-Flow module for perl

%prep

%setup -q -n %{realname}-%{version} 

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Data/Flow.pm
%{perl_vendorlib}/auto/Data/Flow/autosplit.ix
%{_mandir}/*/*

