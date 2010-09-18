Summary:	Open-Source JavaScript framework for visual effects and interface behaviours
Summary(pl.UTF-8):	Oparty na otwartych źródłach szkielet JavaScript dla wizualnych efektów i zachowania interfejsu
Name:		scriptaculous
Version:	1.8.3
Release:	0.1
License:	MIT
Group:		Applications/WWW
Source0:	http://script.aculo.us/dist/%{name}-js-%{version}.tar.bz2
# Source0-md5:	47122c84cdd2f5eb9b5b9cb84f5d2242
Source1:	apache.conf
Source2:	lighttpd.conf
URL:		http://script.aculo.us/
BuildRequires:	sed >= 4.0
Requires:	prototype >= 1.6.0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir	%{_datadir}/%{name}

%description
A collection of Web 2.0 style JavaScript libraries that help web
developers to easily add visual and ajax effects to projects.

%description -l pl.UTF-8
Kolekcja styli Web 2.0 dlabibliotek JavaScriptowych, które pomagają
twórcom stron aby łatwiej dodawać wizualne i ajaxowe efekty do
projektów.

%prep
%setup -q -n %{name}-js-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}
cp -a src/*.js $RPM_BUILD_ROOT%{_appdir}

cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc README.rdoc CHANGELOG
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%{_appdir}
