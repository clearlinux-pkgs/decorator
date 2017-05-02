#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : decorator
Version  : 4.0.11
Release  : 30
URL      : http://pypi.debian.net/decorator/decorator-4.0.11.tar.gz
Source0  : http://pypi.debian.net/decorator/decorator-4.0.11.tar.gz
Summary  : Better living through Python with decorators
Group    : Development/Tools
License  : BSD-2-Clause
Requires: decorator-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Decorator module
=================
:Author: Michele Simionato
:E-mail: michele.simionato@gmail.com
:Requires: Python 2.6+
:Download page: http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

%package python
Summary: python components for the decorator package.
Group: Default

%description python
python components for the decorator package.


%prep
%setup -q -n decorator-4.0.11

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486132476
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
export SOURCE_DATE_EPOCH=1486132476
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
