%define jboss_name jboss-as6
%define jboss_version 6.0.0.CR1
%define jboss_version_full 6.0.0.20101110-CR1

Summary:        The JBoss AS 6 Developer Add-ons for Cloud Profiles
Name:           jboss-as6-cloud-profiles-developer
Version:        %{jboss_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
#Source0:        http://internap.dl.sourceforge.net/sourceforge/jboss/jboss-as-distribution-%{jboss_version_full}.zip
Source0:        http://cdnetworks-us-1.dl.sourceforge.net/project/jboss/JBoss/JBoss-%{jboss_version}/jboss-as-distribution-%{jboss_version_full}.zip
Requires:       jboss-as6-developer

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The JBoss AS 6 Developer Add-ons

%define __jar_repack %{nil}

%prep
%setup -T -b 0 -n jboss-%{jboss_version_full}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

# create directories
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deploy
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deploy
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deploy

# re-install 'httpha-invoker.sar' 
cp -R jboss-%{jboss_version_full}/server/all/deploy/httpha-invoker.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/httpha-invoker.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/httpha-invoker.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deploy/

# re-install 'juddi-service.sar' 
cp -R jboss-%{jboss_version_full}/server/all/deploy/juddi-service.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/juddi-service.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/juddi-service.sar $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deploy/

# re-install 'jbossws-console-activator-jboss-beans.xml' to { all, default, standard }
cp -R jboss-%{jboss_version_full}/server/all/deploy/jbossws-console-activator-jboss-beans.xml $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/jbossws-console-activator-jboss-beans.xml $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deploy/
cp -R jboss-%{jboss_version_full}/server/all/deploy/jbossws-console-activator-jboss-beans.xml $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deploy/


%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Tue Oct 26 2010 Bob McWhirter 
- Initial revision
