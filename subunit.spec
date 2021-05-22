#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : subunit
Version  : 1.4.0
Release  : 72
URL      : https://github.com/testing-cabal/subunit/archive/1.4.0/subunit-1.4.0.tar.gz
Source0  : https://github.com/testing-cabal/subunit/archive/1.4.0/subunit-1.4.0.tar.gz
Summary  : Subunit test protocol library.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: subunit-bin = %{version}-%{release}
Requires: subunit-lib = %{version}-%{release}
Requires: subunit-license = %{version}-%{release}
Requires: subunit-perl = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : iso8601
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(cppunit)
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2

%description
#  subunit shell bindings.
#  Licensed under either the Apache License, Version 2.0 or the BSD 3-clause
#  license at the users choice. A copy of both licenses are available in the
#  project source as Apache-2.0 and BSD. You may not use this file except in
#  compliance with one of these two licences.
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under these licenses is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
#  license you chose for the specific language governing permissions and
#  limitations under that license.

%package bin
Summary: bin components for the subunit package.
Group: Binaries
Requires: subunit-license = %{version}-%{release}

%description bin
bin components for the subunit package.


%package dev
Summary: dev components for the subunit package.
Group: Development
Requires: subunit-lib = %{version}-%{release}
Requires: subunit-bin = %{version}-%{release}
Provides: subunit-devel = %{version}-%{release}
Requires: subunit = %{version}-%{release}

%description dev
dev components for the subunit package.


%package lib
Summary: lib components for the subunit package.
Group: Libraries
Requires: subunit-license = %{version}-%{release}

%description lib
lib components for the subunit package.


%package license
Summary: license components for the subunit package.
Group: Default

%description license
license components for the subunit package.


%package perl
Summary: perl components for the subunit package.
Group: Default
Requires: subunit = %{version}-%{release}

%description perl
perl components for the subunit package.


%prep
%setup -q -n subunit-1.4.0
cd %{_builddir}/subunit-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616002797
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}  INSTALLDIRS=vendor

%install
export SOURCE_DATE_EPOCH=1616002797
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/subunit
cp %{_builddir}/subunit-1.4.0/Apache-2.0 %{buildroot}/usr/share/package-licenses/subunit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/subunit-1.4.0/python/iso8601/LICENSE %{buildroot}/usr/share/package-licenses/subunit/e7da7157e8398cab6dffd7f689d3f1dc7676f871
%make_install
## Remove excluded files
rm -f %{buildroot}/usr/lib/perl5/5.20.0/x86_64-linux/perllocal.pod
rm -f %{buildroot}/usr/bin/subunit-1to2
rm -f %{buildroot}/usr/bin/subunit2csv
rm -f %{buildroot}/usr/bin/subunit2gtk
rm -f %{buildroot}/usr/bin/subunit2junitxml
rm -f %{buildroot}/usr/bin/subunit2pyunit
rm -f %{buildroot}/usr/bin/subunit-2to1
rm -f %{buildroot}/usr/bin/subunit-filter
rm -f %{buildroot}/usr/bin/subunit-ls
rm -f %{buildroot}/usr/bin/subunit-notify
rm -f %{buildroot}/usr/bin/subunit-output
rm -f %{buildroot}/usr/bin/subunit-stats
rm -f %{buildroot}/usr/bin/subunit-tags
rm -f %{buildroot}/usr/bin/tap2subunit
## install_append content
rm -rfv %{buildroot}/usr/lib/python3*/site-packages/subunit
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/subunit-diff
/usr/bin/subunit2disk

%files dev
%defattr(-,root,root,-)
/usr/include/subunit/SubunitTestProgressListener.h
/usr/include/subunit/child.h
/usr/lib64/libcppunit_subunit.so
/usr/lib64/libsubunit.so
/usr/lib64/pkgconfig/libcppunit_subunit.pc
/usr/lib64/pkgconfig/libsubunit.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcppunit_subunit.so.0
/usr/lib64/libcppunit_subunit.so.0.0.0
/usr/lib64/libsubunit.so.0
/usr/lib64/libsubunit.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/subunit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/subunit/e7da7157e8398cab6dffd7f689d3f1dc7676f871

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Subunit.pm
/usr/lib/perl5/vendor_perl/5.34.0/Subunit/Diff.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Subunit/.packlist
