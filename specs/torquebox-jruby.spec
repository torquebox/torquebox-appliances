%define jruby_version 1.5.6

%global _binaries_in_noarch_packages_terminate_build 0

Summary:        TorqueBox JRuby
Name:           torquebox-jruby
Version:        %{jruby_version}
Release:        1
License:        LGPL
BuildArch:      noarch
Group:          Applications/System
Source0:        http://jruby.org.s3.amazonaws.com/downloads/%{jruby_version}/jruby-bin-%{jruby_version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides: rubyabi(1.8-java)
Provides: torquebox-rubygem(columnize)       = 0.3.1
Provides: torquebox-rubygem(rake)            = 0.8.7
Provides: torquebox-rubygem(rspec)           = 1.3.0
Provides: torquebox-rubygem(ruby-debug)      = 0.10.3
Provides: torquebox-rubygem(ruby-debug-base) = 0.10.3.2
Provides: torquebox-rubygem(source)          = 0.0.1

%description
The TorqueBox JRuby Distribution

%define __jar_repack %{nil}

%prep
%setup -n jruby-%{jruby_version}

%install
rm -Rf $RPM_BUILD_ROOT

cd %{_topdir}/BUILD

install -d -m 755 $RPM_BUILD_ROOT/opt/

# copy jruby
cp -R jruby-%{jruby_version} $RPM_BUILD_ROOT/opt/jruby

%clean
rm -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/

%changelog
* Tue Dec 14 2010 Ben Browning
- Upgrade to JRuby 1.5.6

* Sun Oct 17 2010 Bob McWhirter 
- Initial release
