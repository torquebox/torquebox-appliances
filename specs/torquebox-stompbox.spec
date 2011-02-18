%define torquebox_version 1.0.0.CR1-SNAPSHOT
%define torquebox_rpm_version 1.0.0.CR1.SNAPSHOT

%define jboss_name jboss-as6

Summary:        TorqueBox StompBox
Name:           torquebox-stompbox
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        %{name}-installer.init
Source1:        %{name}-knob.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       jboss-as6
Requires:       git
Requires(post): /sbin/chkconfig

%description
TorqueBox StompBox

%prep

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{_initrddir}/%{name}-installer

install -d -m 755 $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deploy
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT/opt/%{jboss_name}/server/default/deploy/torquebox-stompbox-knob.yml

install -d -m 755 $RPM_BUILD_ROOT/opt/stompbox-deployments

%clean
rm -Rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}-installer

%files
%defattr(-,root,root)
/

%changelog
* Tue Dec 14 2010 Ben Browning
- Upgrade to JRuby 1.5.6

* Sun Oct 17 2010 Bob McWhirter 
- Initial release
