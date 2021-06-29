%define module lockfile
#define debug_package %{nil}

Name:           python-%{module}
Version:        0.12.2
Release:        1
Summary:        Platform-independent file locking module
Group:          Development/Python
License:        MIT
URL:            http://smontanaro.dyndns.org/python/
Source0:        https://files.pythonhosted.org/packages/17/47/72cb04a58a35ec495f96984dddb48232b551aafb95bde614605b754fe6f7/%{module}-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. The lock mechanism relies on the atomic nature of the link
(on Unix) and mkdir (on Windows) system calls.

%prep
%setup -q -n %{module}-%{version}

%build

%install
python setup.py install --root=%{buildroot}

%files
%doc doc/* LICENSE MANIFEST README RELEASE-NOTES ACKS
%{py_puresitedir}/*
