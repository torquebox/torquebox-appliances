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
Requires:       torquebox-%{jboss-name}-common
Requires:       torquebox-%{jboss-name}-deployers
Requires:       torquebox-rubygems-dependencies

%description
The TorqueBox Common


%changelog
* Sun Feb 20 2011 Bob McWhirter
- Initial release
