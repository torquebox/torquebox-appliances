%define torquebox_build_number   1761
%define torquebox_version        1.0.0.CR1-SNAPSHOT
%define torquebox_rpm_version    1.0.0.CR1.SNAPSHOT
%define torquebox_gems_version   1.0.0.CR1
%define jruby_version            1.5.6

%global ruby_sitelib /opt/jruby/lib/ruby/site_ruby/1.8
%global gem_dir      /opt/jruby/lib/ruby/gems/1.8
%global bin_dir      /opt/jruby/bin
%global lib_dir      /opt/jruby/lib
%global ruby_abi     1.8-java

%global gem_install  gem install --pre --source http://rubygems.torquebox.org --bindir %{buildroot}%{bin_dir} --install-dir %{buildroot}%{gem_dir} --force --ignore-dependencies -v %{torquebox_gems_version}

%global _binaries_in_noarch_packages_terminate_build 0

Summary:        TorqueBox Rubygems
Name:           torquebox-rubygems
Version:        %{torquebox_rpm_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://ci.stormgrind.org/repository/download/bt7/%{torquebox_build_number}:id/torquebox-dist-bin.zip?guest=1

Requires: ruby(abi)       = %{ruby_abi}
Requires: torquebox-jruby = %{jruby_version}

Provides: torquebox-rubygem(org.torquebox.rake-support)               = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-container)        = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-messaging)        = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-messaging)        = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-naming-client)    = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.torquebox-naming-container) = %{torquebox_rpm_version}
Provides: torquebox-rubygem(org.torquebox.vfs)                        = %{torquebox_rpm_version}

%description
  The TorqueBox Rubygems 

%prep
%setup -n torquebox-%{torquebox_version}

%install

rm -rf %{buildroot}
install -m 755 -d %{buildroot}%{bin_dir}
install -m 755 -d %{buildroot}%{lib_dir}

install -m 755 -d %{buildroot}%{gem_dir}

%{gem_install} --platform ruby org.torquebox.capistrano-support 
%{gem_install} --platform ruby org.torquebox.rake-support 
%{gem_install} --platform java org.torquebox.torquebox-container-foundation 
%{gem_install} --platform java org.torquebox.torquebox-messaging-client 
%{gem_install} --platform java org.torquebox.torquebox-messaging-container 
%{gem_install} --platform java org.torquebox.torquebox-naming-client 
%{gem_install} --platform java org.torquebox.torquebox-naming-container 
%{gem_install} --platform ruby org.torquebox.vfs 

cp ./jruby/lib/jboss-*.jar %{buildroot}%{lib_dir}


%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
/

%changelog
* Thu Jan 27 2011 Lance Ball
- Update gem dependencies for CR1

* Tue Dec 14 2010 Ben Browning
- Upgrade to 1.0.0.RC1-SNAPSHOT and JRuby 1.5.6

* Mon Oct 04 2010 Bob McWhirter 
- Initial release
