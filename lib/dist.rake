
###
### Sanity-checking and verification
###

task 'sanity'=>[ 'sanity:dirs', 'sanity:versions' ] 

task 'sanity:dirs' do
  [ 
    '../rumpler',
    '../torquebox-rpm'
  ].each do |dir|
    print "Checking #{dir}...."
    if ( File.exist?( dir ) )
      puts "kk!"
    else
      fail( "Missing important directory: #{dir}" )
    end
  end
end

task 'sanity:versions' do
  BuildVersion.instance
end

task 'sanity:versions:verify' => [ 'sanity:versions' ] do
  puts "TorqueBox build number...#{BuildVersion.instance.torquebox}"
  print "Type 'y' if this version is acceptable: "
  c = STDIN.gets.strip
  if ( c.downcase != 'y' )
    fail "You didn't type 'y'"
  end
end



###
### RPM
###

desc 'Build all RPMs for torquebox. Requires git://github.com/torquebox/torquebox-rpm.git in the parent directory.'
task 'torquebox:rpm' => 'rpm:core' do
  Dir.chdir( '../torquebox-rpm' ) do
    sh 'rake rpm:all'
    sh 'rake rpm:repodata:force'
  end
end

desc "Clean all RPMs"
task 'torquebox:rpm:clean' do
  sh 'rm -Rf ../torquebox-rpm/build/topdir' 
  sh 'rm -Rf ./build/topdir' 
end

task 'rpm:core' => [
  'rpm:jboss-as6',
  'rpm:torquebox-deployers',
  'rpm:repodata:force'
]



###
### Rumpler
###
desc "Resolve dependencies for TorqueBox RPMs and scribble spec files"
task 'torquebox:rumpler' => [ 'sanity:versions:verify' ] do
  puts "rumpling torquebox-rpm"
  Dir.chdir( "../torquebox-rpm" ) do
    FileUtils.mkdir_p( 'specs/gems' )
    if ( Dir[ 'specs/gems/*.spec' ].empty? )
      sh "../rumpler/bin/rumpler -r gemfiles/root.yml -o ./specs/gems/ -n torquebox-rubygems-dependencies -V #{BuildVersion.instance.torquebox_rpm}"
    else
      puts "INFO: specs present, not rumpling"
    end
  end
end

task 'torquebox:rumpler:clean' do
  sh 'rm -Rf ../torquebox-rpm/specs/gems' 
end



##
# Appliances
##

task 'appliance:vmware' => 'torquebox:rpm' do
  sh "boxgrinder-build -W ./appliances/torquebox.appl -p vmware"
end

task 'appliance:vmware:only' do
  sh "boxgrinder-build -W ./appliances/torquebox.appl -p vmware"
end

task 'appliance:ebs' => 'torquebox:rpm' do
  sh 'boxgrinder-build -W ./appliances/torquebox.appl -p ec2 -d ebs'
end

task 'appliance:ebs:only' do
  sh 'boxgrinder-build -W ./appliances/torquebox.appl -p ec2 -d ebs'
end

task 'appliance:ami' => 'torquebox:rpm' do
  begin
    interrupt_handler = proc{ restore_s3 }
    trap "SIGINT", interrupt_handler
    scribble_s3
    sh 'boxgrinder-build -W ./appliances/torquebox.appl -p ec2 -d ami'
  ensure
    restore_s3
  end
end

task 'appliance:ami:only' do
  begin
    interrupt_handler = proc{ restore_s3 }
    trap "SIGINT", interrupt_handler
    scribble_s3
    sh 'boxgrinder-build -W ./appliances/torquebox.appl -p ec2 -d ami'
  ensure
    restore_s3
  end
end

task 'appliance:clean' => [ 'torquebox:rpm:clean', 'torquebox:rumpler:clean' ] do
  sh "rm -Rf build/topdir"
  sh "rm -Rf build/appliances"
end

