#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : subunit
Version  : 1.2.0
Release  : 38
URL      : https://launchpad.net/subunit/trunk/1.2/+download/subunit-1.2.0.tar.gz
Source0  : https://launchpad.net/subunit/trunk/1.2/+download/subunit-1.2.0.tar.gz
Source99 : https://launchpad.net/subunit/trunk/1.2/+download/subunit-1.2.0.tar.gz.asc
Summary  : Subunit test protocol library.
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: subunit-bin
Requires: subunit-python
Requires: subunit-lib
BuildRequires : extras
BuildRequires : iso8601
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(cppunit)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : testrepository
BuildRequires : testresources
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : traceback2

%description
#  subunit C++ bindings.
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

%package bin
Summary: bin components for the subunit package.
Group: Binaries

%description bin
bin components for the subunit package.


%package dev
Summary: dev components for the subunit package.
Group: Development
Requires: subunit-lib
Requires: subunit-bin
Provides: subunit-devel

%description dev
dev components for the subunit package.


%package lib
Summary: lib components for the subunit package.
Group: Libraries

%description lib
lib components for the subunit package.


%package python
Summary: python components for the subunit package.
Group: Default

%description python
python components for the subunit package.


%prep
%setup -q -n subunit-1.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500744289
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1500744289
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/Subunit.pm
/usr/lib/perl5/site_perl/5.26.0/Subunit/Diff.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/Subunit/.packlist

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/subunit-1to2
%exclude /usr/bin/subunit-2to1
%exclude /usr/bin/subunit-filter
%exclude /usr/bin/subunit-ls
%exclude /usr/bin/subunit-notify
%exclude /usr/bin/subunit-output
%exclude /usr/bin/subunit-stats
%exclude /usr/bin/subunit-tags
%exclude /usr/bin/subunit2csv
%exclude /usr/bin/subunit2gtk
%exclude /usr/bin/subunit2junitxml
%exclude /usr/bin/subunit2pyunit
%exclude /usr/bin/tap2subunit
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

%files python
%defattr(-,root,root,-)
%exclude /usr/lib/python2.7/site-packages/subunit/__init__.py
%exclude /usr/lib/python2.7/site-packages/subunit/__init__.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/_output.py
%exclude /usr/lib/python2.7/site-packages/subunit/_output.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/_to_disk.py
%exclude /usr/lib/python2.7/site-packages/subunit/_to_disk.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/chunked.py
%exclude /usr/lib/python2.7/site-packages/subunit/chunked.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/details.py
%exclude /usr/lib/python2.7/site-packages/subunit/details.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/filters.py
%exclude /usr/lib/python2.7/site-packages/subunit/filters.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/iso8601.py
%exclude /usr/lib/python2.7/site-packages/subunit/iso8601.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/progress_model.py
%exclude /usr/lib/python2.7/site-packages/subunit/progress_model.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/run.py
%exclude /usr/lib/python2.7/site-packages/subunit/run.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/test_results.py
%exclude /usr/lib/python2.7/site-packages/subunit/test_results.pyc
%exclude /usr/lib/python2.7/site-packages/subunit/v2.py
%exclude /usr/lib/python2.7/site-packages/subunit/v2.pyc
