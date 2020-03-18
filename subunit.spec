#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : subunit
Version  : 1.3.0
Release  : 63
URL      : https://github.com/testing-cabal/subunit/archive/1.3.0.tar.gz
Source0  : https://github.com/testing-cabal/subunit/archive/1.3.0.tar.gz
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
%setup -q -n subunit-1.3.0
cd %{_builddir}/subunit-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1584563725
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}  INSTALLDIRS=vendor

%install
export SOURCE_DATE_EPOCH=1584563725
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/subunit
cp %{_builddir}/subunit-1.3.0/Apache-2.0 %{buildroot}/usr/share/package-licenses/subunit/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/subunit-1.3.0/python/iso8601/LICENSE %{buildroot}/usr/share/package-licenses/subunit/e7da7157e8398cab6dffd7f689d3f1dc7676f871
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
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/details.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/progress_model.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/_output.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/_to_disk.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/chunked.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/progress_model.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/run.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/run.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/chunked.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/test_results.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/_to_disk.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/test_results.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/_output.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/details.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/filters.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/filters.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/iso8601.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/iso8601.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/v2.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/__init__.cpython-38.pyc
rm -f %{buildroot}/usr/lib/python3.8/site-packages/subunit/__pycache__/v2.cpython-38.pyc

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
/usr/lib/perl5/vendor_perl/5.30.2/Subunit.pm
/usr/lib/perl5/vendor_perl/5.30.2/Subunit/Diff.pm
/usr/lib/perl5/vendor_perl/5.30.2/x86_64-linux-thread-multi/auto/Subunit/.packlist
