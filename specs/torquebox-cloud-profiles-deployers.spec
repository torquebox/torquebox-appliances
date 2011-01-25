%define torquebox_build_number 1357
%define torquebox_version 1.0.0.RC1-SNAPSHOT
%define torquebox_rpm_version 1.0.0.RC1.SNAPSHOT

%define jboss_name jboss-as6

Summary:        TorqueBox Cloud Profiles Deployers
Name:           torquebox-cloud-profiles-deployers
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
#Source0:        http://repository.torquebox.org/maven2/releases/org/torquebox/torquebox-dist/1.0.0.Beta22/torquebox-dist-%{torquebox_version}-bin.zip
Source:         http://ci.stormgrind.org/repository/download/bt7/%{torquebox_build_number}:id/torquebox-dist-bin.zip?guest=1%{torquebox_build_number}
Requires:       %{jboss_name}-cloud-profiles
Requires:       torquebox-jruby
Requires:       torquebox-rubygems
Requires:       torquebox-rubygems-dependencies
Requires:       rubyabi(1.8-java)

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The TorqueBox Cloud Profiles Deployers

%define __jar_repack %{nil}

%prep
%setup -T -b 0 -n torquebox-%{torquebox_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deployers


# copy profiles
cp -R torquebox-%{torquebox_version}/jboss/server/all/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster-ec2/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/all/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/cluster/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/all/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/group/deployers/

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Tue Dec 14 2010 Ben Browning
- Upgrade to 1.0.0.RC1-SNAPSHOT

* Mon Oct 04 2010 Bob McWhirter 
- Initial release
