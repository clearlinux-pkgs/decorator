#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : decorator
Version  : 4.4.1
Release  : 61
URL      : https://files.pythonhosted.org/packages/dc/c3/9d378af09f5737cfd524b844cd2fbb0d2263a35c11d712043daab290144d/decorator-4.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/c3/9d378af09f5737cfd524b844cd2fbb0d2263a35c11d712043daab290144d/decorator-4.4.1.tar.gz
Summary  : Decorators for Humans
Group    : Development/Tools
License  : BSD-2-Clause
Requires: decorator-license = %{version}-%{release}
Requires: decorator-python = %{version}-%{release}
Requires: decorator-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : util-linux

%description
Decorators for Humans
=====================
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
Provides: pypi(decorator)

%description python3
python3 components for the decorator package.


%prep
%setup -q -n decorator-4.4.1
cd %{_builddir}/decorator-4.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582916489
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/decorator
cp %{_builddir}/decorator-4.4.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/decorator/3483701a3a93cfae3581f5a544e3a21fe01933bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/decorator/3483701a3a93cfae3581f5a544e3a21fe01933bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
