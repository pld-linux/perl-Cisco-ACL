# ToDo:
# - pl description
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cisco
%define	pnam	ACL
Summary:	Generate Access Control Lists for Cisco IOS
Summary(pl):	Generowanie List Kontroli Dostêpu (ACL) dla Cisco IOS
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic	
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	646effed75f2893847d31435fe71d999
URL:		http://search.cpan.org/dist/Cisco-ACL/
BuildRequires:	perl-Class-MethodMaker
BuildRequires:	perl-Module-Build >= 0.02
BuildRequires:	perl-Params-Validate >= 0.65
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cisco::ACL is a module to create cisco-style access lists. IOS uses a
wildcard syntax that is almost but not entirely unlike netmasks, but
backwards (at least that's how it has always seemed to me).

This module makes it easy to think in CIDR but emit IOS-compatible access lists.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3},%{perl_vendorlib}/%{pdir}}

install blib/script/aclmaker.pl $RPM_BUILD_ROOT%{_bindir}
install blib/bindoc/aclmaker.pl.1p $RPM_BUILD_ROOT%{_mandir}/man1
install blib/lib/Cisco/ACL.pm $RPM_BUILD_ROOT%{perl_vendorlib}/%{pdir}
install blib/libdoc/*.3pm $RPM_BUILD_ROOT%{_mandir}/man3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Cisco
%{_mandir}/man?/*
