%define jboss_version 6.0.0.CR1
%define jboss_version_full 6.0.0.20101110-CR1

Summary:        JBoss Application Server
Name:           jboss-as6
Version:        %{jboss_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://cdnetworks-us-1.dl.sourceforge.net/project/jboss/JBoss/JBoss-%{jboss_version}/jboss-as-distribution-%{jboss_version_full}.zip
Source1:        %{name}.init
Source2:        jboss-as6-https-connector.patch
Source3:        jboss-as6-jmx-console.patch
Requires:       shadow-utils
Requires:       coreutils
Requires:       java-1.6.0-openjdk
Requires:       initscripts
Requires(post): /sbin/chkconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define runuser %{name}
%define __jar_repack %{nil}

%description
The JBoss Application Server

# Don't complain about arch-specific packages in noarch build (HornetQ libaio natives)
%global _binaries_in_noarch_packages_terminate_build 0

%prep
%setup -n jboss-%{jboss_version_full}

%install
cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT/opt/%{name}
cp -R jboss-%{jboss_version_full}/* $RPM_BUILD_ROOT/opt/%{name}

# it caused adding bad requires for package
rm -rf $RPM_BUILD_ROOT/opt/%{name}/bin/jboss_init_solaris.sh

# Remove ROOT.war files
find $RPM_BUILD_ROOT/opt/%{name}/server/ -name "ROOT.war" | xargs rm -rf

# Remove gratuitous services and consoles
find $RPM_BUILD_ROOT/opt/%{name}/server/ -name "httpha-invoker.sar" | xargs rm -rf
find $RPM_BUILD_ROOT/opt/%{name}/server/ -name "juddi-service.sar" | xargs rm -rf

find $RPM_BUILD_ROOT/opt/%{name}/common/ -name "jbossws-console.war" | xargs rm -rf
find $RPM_BUILD_ROOT/opt/%{name}/server/ -name "jbossws.war" | xargs rm -rf
find $RPM_BUILD_ROOT/opt/%{name}/server/ -name "jbossws-console-activator-jboss-beans.xml" | xargs rm -rf

# Open the HTTPS Connector
cd $RPM_BUILD_ROOT/opt/%{name}/server/all/deploy/jbossweb.sar && patch -i %{SOURCE2}
cd $RPM_BUILD_ROOT/opt/%{name}/server/default/deploy/jbossweb.sar && patch -i %{SOURCE2}
cd $RPM_BUILD_ROOT/opt/%{name}/server/jbossweb-standalone/deploy/jbossweb.sar && patch -i %{SOURCE2}
cd $RPM_BUILD_ROOT/opt/%{name}/server/osgi/deploy/jbossweb.sar && patch -i %{SOURCE2}
cd $RPM_BUILD_ROOT/opt/%{name}/server/standard/deploy/jbossweb.sar && patch -i %{SOURCE2}

# Enable authentication for jmx-console
cd $RPM_BUILD_ROOT/opt/%{name} && patch -p0 -i %{SOURCE3}

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig

echo "JBOSS_VERSION=%{version}"              > $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "JBOSS_HOME=/opt/%{name}"              >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}
echo "JBOSS_IP=0.0.0.0"                     >> $RPM_BUILD_ROOT/etc/sysconfig/%{name}

chmod 600 $RPM_BUILD_ROOT/etc/sysconfig/%{name} 

%clean
rm -Rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r %{name} 2>/dev/null || :
/usr/sbin/useradd -c "JBoss AS" -r -s /bin/bash -d /opt/%{name} -g %{name} %{name} 2>/dev/null || :

%post
/sbin/chkconfig --add %{name}

ln -s /etc/sysconfig/%{name} /etc/sysconfig/jboss-as
ln -s /opt/%{name} /opt/jboss-as
ln -s /etc/init.d/%{name} /etc/init.d/jboss-as
ln -s /etc/init.d/%{name} /etc/init.d/jboss_as

echo "jboss-as6 soft nofile 4096"           >> /etc/security/limits.conf
echo "jboss-as6 hard nofile 4096"           >> /etc/security/limits.conf

%files
%defattr(-,%{name},%{name})
/

%changelog
* Wed Jul 28 2010 Marek Goldmann 6.0.0.M4-1
- Upgrade to upstream 6.0.0.M4 release 

* Fri May 05 2010 Marek Goldmann 6.0.0.M3-1
- Upgrade to upstream 6.0.0.M3 release

* Wed Feb 17 2010 Marek Goldmann 6.0.0.M2-1
- Upgrade to JBoss AS 6.0.0.M2

* Thu Dec 03 2009 Marek Goldmann 6.0.0.M1-1
- Initial release
