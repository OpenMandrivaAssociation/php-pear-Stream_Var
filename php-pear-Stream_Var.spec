%define		_class		Stream
%define		_subclass	Var
%define		upstream_name	%{_class}_%{_subclass}

Summary:	Allows stream based access to any variable
Name:		php-pear-%{upstream_name}
Version:	1.1.0
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Stream_Var/
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
%{upstream_name} can be registered as a stream with stream_register_wrapper 
and allows stream based access to any variable in any scope. Arrays are
treated as directories, so it`s possible to replace temporary
directories and files in your applications with variables.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/doc
rm -rf %{buildroot}%{_datadir}/pear/test

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
