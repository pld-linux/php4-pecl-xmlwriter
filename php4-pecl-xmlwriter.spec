%define		_modname	xmlwriter
%define		_status		stable

Summary:	%{_modname} - provides fast, non-cached, forward-only means to write XML data
Summary(pl):	%{_modname} - szybka, nie cachowana metoda zapisu danych w formacie XML
Name:		php4-pecl-%{_modname}
Version:	2.0.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	ee90a55b753975faac607f4230ece2b4
URL:		http://pecl.php.net/package/xmlwriter/
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	php4-devel >= 3:4.3.0
Requires:	php4-common >= 3:4.3.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

%description
This extension wraps the libxml xmlWriter API. Represents a writer
that provides a non-cached, forward-only means of generating streams
or files containing XML data.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie obudowuje API xmlWriter z libxml. Reprezentuje 
obs³ugê zapisu dostarczaj±c± nie cachowanych metod generowania
strumieni lub plików zawieraj±cych dane XML.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php4-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php4-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
