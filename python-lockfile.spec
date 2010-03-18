%define module lockfile

Name:           python-%{module}
Version:        0.8
Release:        %mkrel 1
Summary:        Platform-independent file locking module
Group:          Development/Python
License:        MIT
URL:            http://smontanaro.dyndns.org/python/
Source0:        http://smontanaro.dyndns.org/python/%{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
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
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}
 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/* LICENSE MANIFEST README RELEASE-NOTES ACKS
%{python_sitelib}/*
