%define torquebox_version 1.0.0.CR1
%define torquebox_rpm_version 1.0.0.CR1

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
mkdir $RPM_BUILD_ROOT/torquebox
mkdir $RPM_BUILD_ROOT/torquebox/apps

%files
%defattr(-,root,root)
/

%changelog
* Fri Apr 15 2011 Lance Ball
- 1.0.0.CR1 release

* Thu Apr 7 2011 Lance Ball
- Update torquebox build number

* Sun Feb 20 2011 Bob McWhirter
- Initial release
