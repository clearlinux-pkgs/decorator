#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : decorator
Version  : 4.3.0
Release  : 48
URL      : https://files.pythonhosted.org/packages/6f/24/15a229626c775aae5806312f6bf1e2a73785be3402c0acdec5dbddd8c11e/decorator-4.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6f/24/15a229626c775aae5806312f6bf1e2a73785be3402c0acdec5dbddd8c11e/decorator-4.3.0.tar.gz
Summary  : Better living through Python with decorators
Group    : Development/Tools
License  : BSD-2-Clause
Requires: decorator-python3
Requires: decorator-license
Requires: decorator-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=================

%package license
Summary: license components for the decorator package.
Group: Default

%description license
license components for the decorator package.


%package python
Summary: python components for the decorator package.
Group: Default
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
%setup -q -n decorator-4.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530326628
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/decorator
cp LICENSE.txt %{buildroot}/usr/share/doc/decorator/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/decorator/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
