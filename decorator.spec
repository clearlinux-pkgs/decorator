#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : decorator
Version  : 4.4.0
Release  : 54
URL      : https://files.pythonhosted.org/packages/ba/19/1119fe7b1e49b9c8a9f154c930060f37074ea2e8f9f6558efc2eeaa417a2/decorator-4.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ba/19/1119fe7b1e49b9c8a9f154c930060f37074ea2e8f9f6558efc2eeaa417a2/decorator-4.4.0.tar.gz
Summary  : Better living through Python with decorators
Group    : Development/Tools
License  : BSD-2-Clause
Requires: decorator-license = %{version}-%{release}
Requires: decorator-python = %{version}-%{release}
Requires: decorator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
Decorator module
=================
The goal of the decorator module is to make it easy to define
signature-preserving function decorators and decorator factories.
It also includes an implementation of multiple dispatch and other niceties
(please check the docs). It is released under a two-clauses
BSD license, i.e. basically you can do whatever you want with it but I am not
responsible.

%package license
Summary: license components for the decorator package.
Group: Default

%description license
license components for the decorator package.


%package python
Summary: python components for the decorator package.
Group: Default
Requires: decorator-python3 = %{version}-%{release}

%description python
python components for the decorator package.


%package python3
Summary: python3 components for the decorator package.
Group: Default
Requires: python3-core

%description python3
python3 components for the decorator package.


%prep
%setup -q -n decorator-4.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552790801
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/decorator
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/decorator/LICENSE.txt
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/decorator/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
