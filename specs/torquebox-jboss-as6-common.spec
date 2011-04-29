%define torquebox_version 1.0.0.Final
%define torquebox_rpm_version 1.0.0.Final

%define jboss_name jboss-as6

Summary:        TorqueBox JBoss AS6 Common
Name:           torquebox-jboss-as6-common
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source:         http://repository-torquebox.forge.cloudbees.com/release/org/torquebox/torquebox-dist/%{torquebox_version}/torquebox-dist-%{torquebox_version}-bin.zip

Requires:       %{jboss_name}
Requires:       torquebox-jruby
Requires:       torquebox-rubygems-dependencies
Requires:       rubyabi(1.8-java) 

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The TorqueBox Common

%define __jar_repack %{nil}

%prep
%setup -n torquebox-%{torquebox_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

# Create common directory to which we copy the TorqueBox subdir
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/common

# Create the common lib directory to which we install our bootstrap jar.
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/common/lib

# Create /etc/sysconfig for our config
install -d -m 755 $RPM_BUILD_ROOT/etc/sysconfig

# Copy the common jars
cp -R torquebox-%{torquebox_version}/jboss/common/torquebox/ $RPM_BUILD_ROOT/opt/%{jboss_name}/common/

# Copy the bootstrap jars
cp torquebox-%{torquebox_version}/jboss/common/lib/torquebox-*.jar $RPM_BUILD_ROOT/opt/%{jboss_name}/common/lib/

# Write our config

echo "TORQUEBOX_VERSION=%{torquebox_version}"           >> $RPM_BUILD_ROOT/etc/sysconfig/torquebox

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,%{jboss_name},%{jboss_name})
/

%changelog
* Fri Apr 29 2011 Lance Ball
- 1.0.0.Final release

* Tue Apr 26 2011 Lance Ball
- 1.0.0.CR2 release

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
