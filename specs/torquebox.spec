%define torquebox_build_number 1864
%define torquebox_version 1.0.0.CR1-SNAPSHOT
%define torquebox_rpm_version 1.0.0.CR1.SNAPSHOT

%define jboss_name jboss-as6

Summary:        TorqueBox Ruby Application Server
Name:           torquebox
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System

Requires:       %{jboss_name}
Requires:       torquebox-jruby
Requires:       torquebox-%{jboss_name}-common
Requires:       torquebox-%{jboss_name}-deployers
Requires:       torquebox-rubygems-dependencies

%description
The TorqueBox Common

%install
rm -Rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/

%changelog
* Sun Feb 20 2011 Bob McWhirter
- Initial release
