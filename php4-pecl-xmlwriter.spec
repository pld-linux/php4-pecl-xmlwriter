%define		_modname	xmlwriter
%define		_status		stable
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

Summary:	%{_modname} - provides fast, non-cached, forward-only means to write XML data
Summary(pl):	%{_modname} - szybka, nie cachowana metoda zapisu danych w formacie XML
Name:		php4-pecl-%{_modname}
Version:	2.0.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	ee90a55b753975faac607f4230ece2b4
URL:		http://pecl.php.net/package/xmlwriter/
BuildRequires:	libxml2-devel
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	rpmbuild(macros) >= 1.238
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension wraps the libxml xmlWriter API. Represents a writer
that provides a non-cached, forward-only means of generating streams
or files containing XML data.

In PECL status of this extension is: %{_status}.

%description -l pl
To rozszerzenie obudowuje API xmlWriter z libxml. Reprezentuje obs³ugê
zapisu dostarczaj±c± nie cachowanych metod generowania strumieni lub
plików zawieraj±cych dane XML.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
