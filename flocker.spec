Summary:	Easily manage Docker containers & their data
Summary(pl.UTF-8):	Łatwe zarządzanie kontenerami Dockera i ich danymi
Name:		flocker
Version:	0.4.0
Release:	0.1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://github.com/ClusterHQ/flocker/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	76aa991d8ea4cbf7ae6b3b81b9073a06
Patch0:		deps.patch
URL:		https://github.com/ClusterHQ/flocker
BuildRequires:	python-PyYAML >= 3.10
#BuildRequires:	python-Twisted >= 15.0.0
#BuildRequires:	python-characteristic >= 14.1.0
BuildRequires:	python-docker >= 0.7.1
#BuildRequires:	python-eliot >= 0.6.0
BuildRequires:	python-ipaddr >= 2.1.11
BuildRequires:	python-jsonschema >= 2.4.0
BuildRequires:	python-klein >= 0.2.3
#BuildRequires:	python-machinist >= 0.2.0
BuildRequires:	python-netifaces >= 0.8
BuildRequires:	python-psutil >= 2.1.2
BuildRequires:	python-pyrsistent >= 0.9.1
BuildRequires:	python-pytz
BuildRequires:	python-setuptools >= 1:7.0
#BuildRequires:	python-treq >= 0.2.1
#BuildRequires:	python-zope.interface >= 4.0.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flocker is a data volume manager and multi-host Docker cluster
management tool. With it you can control your data using the same
tools you use for your stateless applications by harnessing the power
of ZFS on Linux. This means that you can run your databases, queues
and key-value stores in Docker and move them around as easily as the
rest of your app.

%description -l pl.UTF-8
Flocker to zarządca wolumenów danych oraz narzędzie do zarządzania
klastrami Dockera na wielu hostach. Przy jego użyciu można mieć
kontrolę nad danymi przy użyciu takich samych narzędzi, jakich używa
się dla aplikacji bezstanowych wykorzystujących potencjał ZFS-a na
Linuksie. Oznacza to, że można uruchamiać na Dockerze bazy danych,
kolejki czy przechowalnie danych klucz-wartość i przenosić je tak
łatwo, jak resztę aplikacji.

%prep
%setup -q
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/flocker/volume/test

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flocker
%attr(755,root,root) %{_bindir}/flocker-changestate
%attr(755,root,root) %{_bindir}/flocker-control
%attr(755,root,root) %{_bindir}/flocker-dataset-agent
%attr(755,root,root) %{_bindir}/flocker-deploy
%attr(755,root,root) %{_bindir}/flocker-reportstate
%attr(755,root,root) %{_bindir}/flocker-volume
%attr(755,root,root) %{_bindir}/flocker-zfs-agent
%{py_sitescriptdir}/Flocker-%{version}-py*.egg-info
%{py_sitescriptdir}/flocker
