#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Load-XS
Version  : 0.10
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-XS-0.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Class-Load-XS-0.10.tar.gz
Summary  : 'XS implementation of parts of Class::Load'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Class-Load-XS-lib
Requires: perl-Class-Load-XS-license
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Load)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Class-Load-XS,
version 0.10:
XS implementation of parts of Class::Load

%package dev
Summary: dev components for the perl-Class-Load-XS package.
Group: Development
Requires: perl-Class-Load-XS-lib
Provides: perl-Class-Load-XS-devel

%description dev
dev components for the perl-Class-Load-XS package.


%package lib
Summary: lib components for the perl-Class-Load-XS package.
Group: Libraries
Requires: perl-Class-Load-XS-license

%description lib
lib components for the perl-Class-Load-XS package.


%package license
Summary: license components for the perl-Class-Load-XS package.
Group: Default

%description license
license components for the perl-Class-Load-XS package.


%prep
%setup -q -n Class-Load-XS-0.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Class-Load-XS
cp LICENSE %{buildroot}/usr/share/doc/perl-Class-Load-XS/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Class/Load/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Load::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Class/Load/XS/XS.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Class-Load-XS/LICENSE
