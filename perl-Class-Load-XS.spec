#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Class-Load-XS
Version  : 0.10
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-XS-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-XS-0.10.tar.gz
Summary  : 'XS implementation of parts of Class::Load'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Class-Load-XS-license = %{version}-%{release}
Requires: perl-Class-Load-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Load)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Class-Load-XS,
version 0.10:
XS implementation of parts of Class::Load

%package dev
Summary: dev components for the perl-Class-Load-XS package.
Group: Development
Provides: perl-Class-Load-XS-devel = %{version}-%{release}
Requires: perl-Class-Load-XS = %{version}-%{release}

%description dev
dev components for the perl-Class-Load-XS package.


%package license
Summary: license components for the perl-Class-Load-XS package.
Group: Default

%description license
license components for the perl-Class-Load-XS package.


%package perl
Summary: perl components for the perl-Class-Load-XS package.
Group: Default
Requires: perl-Class-Load-XS = %{version}-%{release}

%description perl
perl components for the perl-Class-Load-XS package.


%prep
%setup -q -n Class-Load-XS-0.10
cd %{_builddir}/Class-Load-XS-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Load-XS
cp %{_builddir}/Class-Load-XS-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Load-XS/c715d20265d2931c7564fc64abfdc4f8ff33e297 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Load::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Load-XS/c715d20265d2931c7564fc64abfdc4f8ff33e297

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
