%define torquebox_version 1.0.0.CR1
%define torquebox_rpm_version 1.0.0.CR1

%define jboss_name jboss-as6

Summary:        TorqueBox JBoss AS6 Deployers
Name:           torquebox-jboss-as6-deployers
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source:         http://repository-torquebox.forge.cloudbees.com/release/org/torquebox/torquebox-dist/%{torquebox_version}/torquebox-dist-%{torquebox_version}-bin.zip

Requires:       torquebox-jboss-as6-common

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The TorqueBox JBoss AS6 Deployers

%define __jar_repack %{nil}

%prep
%setup -n torquebox-%{torquebox_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

# Create profile deployer directories to which we copy the TorqueBox subdir
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/all/deployers

# Copy the deployer directories
cp -R torquebox-%{torquebox_version}/jboss/server/default/deployers/torquebox.deployer/  $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/all/deployers/torquebox.deployer/        $RPM_BUILD_ROOT/opt/%{jboss_name}/server/all/deployers/

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Fri Apr 15 2011 Lance Ball
- 1.0.0.CR1 release

* Thu Apr 7 2011 Lance Ball
- Update torquebox build number and dist url

* Tue Dec 14 2010 Ben Browning
- Upgrade to 1.0.0.RC1-SNAPSHOT

* Sat Oct 16 2010 Ben Browning
- Upgrade to 1.0.0.Beta23-SNAPSHOT

* Mon Oct 04 2010 Bob McWhirter 
- Initial release
