%define version 0.1.2

Summary: CERNDB SAPI Client Libraries
Name: cerndb-sw-sapi-client
Version: %{version}
Release: 0%{?dist} 
License: GPL
Group: Applications
ExclusiveArch: x86_64
Source: sapi-%{version}.tar.gz
URL: https://cern.ch/DBOnDemand/
Distribution: DBOD
Vendor: CERN
Packager: Ignacio Coterillo Coz <icoteril@cern.ch>

BuildRequires: python
BuildRequires: python-setuptools

Requires: python-cffi
Requires: python-pycparser
Requires: python-requests
Requires: python-requests-kerberos
Requires: python-cryptography
Requires: python-lxml
Requires: python-kerberos
Requires: python-six
Requires: python-configparser
Requires: python-dateutil

Requires: libxml2-python


%global debug_package %{nil}

%description
CERN SAPI Client Libraries

%prep
%setup -n sapi-%{version}
exit 0

%build
exit 0

%install
python setup.py install --root ${RPM_BUILD_ROOT}
PYTHONPATH=${RPM_BUILD_ROOT}/usr/lib/python2.7 && cd vendor && for folder in *; do cd $folder; python setup.py install --no-compile --root ${RPM_BUILD_ROOT}; cd ..; done
rm -fr ${RPM_BUILD_ROOT}/usr/lib/python2.7/site-packages/test
exit 0

%clean
rm -rf $RPM_BUILD_ROOT
exit 0

%post
exit 0

%files
/usr/bin/sapi
/usr/bin/cern-get-sso-cookie.py
/usr/lib/python2.7/site-packages/sapi_client
/usr/lib/python2.7/site-packages/fire
/usr/lib/python2.7/site-packages/certifi
/usr/lib/python2.7/site-packages/cern_sso.py
/usr/lib/python2.7/site-packages/sapi-0.1.2-py2.7.egg-info
/usr/lib/python2.7/site-packages/fire-0.1.2-py2.7.egg-info
/usr/lib/python2.7/site-packages/certifi-2017.11.05-py2.7.egg-info
/usr/lib/python2.7/site-packages/python_cern_sso_krb-1.3.3-py2.7.egg-info

%changelog
* Mon Dec 18 2017 Ignacio Coterillo <icoteril@cern.ch> 0.1.2
- First packaging
