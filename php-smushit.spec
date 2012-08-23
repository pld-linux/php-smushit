%define		pkgname	smushit
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	A PHP client for the Yahoo! Smush.it web service
Name:		php-%{pkgname}
Version:	1.1
Release:	3
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/davgothic/SmushIt/tarball/master#/%{name}-%{version}.tgz
# Source0-md5:	cc287b37ecd39b0bdc5b54a648061199
URL:		https://github.com/davgothic/SmushIt
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php(core) >= %{php_min_version}
Requires:	php(curl)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(spl)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SmushIt is a PHP client for the popular Yahoo! image compression web
service Smush.it

%prep
%setup -qc
mv *-SmushIt-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p smushit.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%{php_data_dir}/smushit.php
