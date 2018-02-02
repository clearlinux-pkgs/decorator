#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : decorator
Version  : 4.1.2
Release  : 38
URL      : https://pypi.python.org/packages/bb/e0/f6e41e9091e130bf16d4437dabbac3993908e4d6485ecbc985ef1352db94/decorator-4.1.2.tar.gz
Source0  : https://pypi.python.org/packages/bb/e0/f6e41e9091e130bf16d4437dabbac3993908e4d6485ecbc985ef1352db94/decorator-4.1.2.tar.gz
Summary  : Better living through Python with decorators
Group    : Development/Tools
License  : BSD-2-Clause
Requires: decorator-legacypython
Requires: decorator-python3
Requires: decorator-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=================

%package legacypython
Summary: legacypython components for the decorator package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the decorator package.


%package python
Summary: python components for the decorator package.
Group: Default
Requires: decorator-legacypython
Requires: decorator-python3

%description python
python components for the decorator package.


%package python3
Summary: python3 components for the decorator package.
Group: Default
Requires: python3-core

%description python3
python3 components for the decorator package.


%prep
%setup -q -n decorator-4.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1508429522
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1508429522
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
