%define torquebox_version 1.0.0
%define torquebox_rpm_version 1.0.0

%define jruby_name jruby

%global _binaries_in_noarch_packages_terminate_build 0

Summary:        TorqueBox JRuby VFS Add-On
Name:           torquebox-jruby-vfs
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source:         http://repository-torquebox.forge.cloudbees.com/release/org/torquebox/torquebox-dist/%{torquebox_version}/torquebox-dist-%{torquebox_version}-bin.zip

Requires:       torquebox-jruby
Requires:       torquebox-rubygem-org.torquebox.vfs-10

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
The TorqueBox JRuby VFS Add-On

%define __jar_repack %{nil}

%prep
%setup -n torquebox-%{torquebox_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

# Create lib directory to which we copy the JRuby subdir
install -d -m 755 $RPM_BUILD_ROOT/opt/%{jruby_name}/lib/

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
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
