%define module lockfile

Name:           python-%{module}
Version:        0.12.2
Release:        2
Summary:        Platform-independent file locking module
Group:          Development/Python
License:        MIT
URL:            http://pypi.org/project/lockfile
Source0:        https://files.pythonhosted.org/packages/source/l/lockfile/lockfile-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(nose)
BuildArch:	noarch

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. The lock mechanism relies on the atomic nature of the link
(on Unix) and mkdir (on Windows) system calls.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%doc doc/* LICENSE README* RELEASE-NOTES ACKS
%{python_sitelib}/lockfile-*info
%{python_sitelib}/lockfile
