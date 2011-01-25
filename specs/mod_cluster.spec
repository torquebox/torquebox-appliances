Summary:    Mod_cluster module for the Apache HTTP server
Name:       mod_cluster
Version:    1.1.0.Final
Release:    1%{dist}
License:    LGPLv2
URL:        http://jboss.org/mod_cluster
Group:      System Environment/Daemons
Source:     http://downloads.jboss.org/%{name}/%{version}/%{name}-%{version}-src-ssl.tar.gz
Source1:    mod_cluster.conf
Source2:    README.fedora
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:      httpd >= 2.2.8
BuildRequires: httpd-devel >= 2.2.8
BuildRequires: autoconf

%description
Mod_cluster is an httpd-based load balancer. Like mod_jk and mod_proxy,
mod_cluster uses a communication channel to forward requests from httpd to one
of a set of application server nodes. Unlike mod_jk and mod_proxy, mod_cluster
leverages an additional connection between the application server nodes and
httpd. The application server nodes use this connection to transmit server-side
load balance factors and lifecycle events back to httpd via a custom set of
HTTP methods, affectionately called the Mod-Cluster Management Protocol (MCMP).
This additional feedback channel allows mod_cluster to offer a level of
intelligence and granularity not found in other load balancing solutions.

%prep
%setup -q -n %{name}-%{version}-src-ssl

%build
module_dirs=( advertise mod_manager mod_proxy_cluster mod_slotmem )

for dir in ${module_dirs[@]} ; do
    pushd srclib/%{name}/native/${dir}
        sh buildconf
        ./configure --libdir=%{_libdir} --with-apxs=/usr/sbin/apxs
        make
    popd
done

%install
rm -rf $RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/httpd/modules

module_dirs=( advertise mod_manager mod_proxy_cluster mod_slotmem )

for dir in ${module_dirs[@]} ; do
    pushd srclib/%{name}/native/${dir}
        cp ./*.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules
    popd
done

install -d -m 755 $RPM_BUILD_ROOT/etc/httpd/conf.d
cp %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/conf.d/

install -m 0644 %{SOURCE2} README

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_libdir}/httpd/modules/mod_advertise.so
%{_libdir}/httpd/modules/mod_manager.so
%{_libdir}/httpd/modules/mod_proxy_cluster.so
%{_libdir}/httpd/modules/mod_slotmem.so
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf

%changelog
* Fri Nov 12 2010  <mgoldman@redhat.com> - 1.1.0.Final-1
- Initial release
