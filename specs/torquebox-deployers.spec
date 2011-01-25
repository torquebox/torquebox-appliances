%define torquebox_build_number 1357
%define torquebox_version 1.0.0.RC1-SNAPSHOT
%define torquebox_rpm_version 1.0.0.RC1.SNAPSHOT

%define jboss_name jboss-as6

Summary:        TorqueBox Deployers
Name:           torquebox-deployers
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
# Source:         http://repository.torquebox.org/maven2/releases/org/torquebox/torquebox-dist/1.0.0.Beta22/torquebox-dist-%{torquebox_version}-bin.zip
Source:         http://ci.stormgrind.org/repository/download/bt7/%{torquebox_build_number}:id/torquebox-dist-bin.zip?guest=1%{torquebox_build_number}

Requires:       %{jboss_name}
Requires:       torquebox-jruby
Requires:       torquebox-rubygems
Requires:       torquebox-rubygems-dependencies
Requires:       rubyabi(1.8-java) 

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The TorqueBox Deployers

%define __jar_repack %{nil}

%prep
%setup -n torquebox-%{torquebox_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/all/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/osgi/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/standard/deployers
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/jbossweb-standalone/deployers

# copy profiles
cp -R torquebox-%{torquebox_version}/jboss/server/all/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/all/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/default/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/osgi/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/osgi/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/standard/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/standard/deployers/
cp -R torquebox-%{torquebox_version}/jboss/server/jbossweb-standalone/deployers/torquebox.deployer/ $RPM_BUILD_ROOT/opt/%{jboss_name}/server/jbossweb-standalone/deployers/

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Tue Dec 14 2010 Ben Browning
- Upgrade to 1.0.0.RC1-SNAPSHOT

* Sat Oct 16 2010 Ben Browning
- Upgrade to 1.0.0.Beta23-SNAPSHOT

* Mon Oct 04 2010 Bob McWhirter 
- Initial release
