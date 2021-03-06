
###
### Sanity-checking and verification
###

task 'sanity'=>[ 'sanity:dirs', 'sanity:versions' ] 

task 'sanity:dirs' do
  dir =  '../rumpler'
  print "Checking #{dir}...."
  ( File.exist?( dir ) ) ? puts( "kk!" ) : fail( "Missing important directory: #{dir}" )
end

desc "Sanity-check versions of stuff"
task 'sanity:versions' do
  # don't use specific build versions for releases
  # BuildVersion.instance
  puts "Skipping sanity:versions. We're working with release builds now."
end

task 'sanity:versions:verify' => [ 'sanity:versions' ] do
  # don't use specific build versions for releases
  # puts "TorqueBox build number...#{BuildVersion.instance.torquebox}"
  # print "Type 'y' if this version is acceptable: "
  # c = STDIN.gets.strip
  # if ( c.downcase != 'y' )
  #   fail "You didn't type 'y'"
  # end
  puts "Skipping sanity:versions:verify. We're working with release builds now."
end



###
### RPM
###
desc "Clean all RPMs"
task 'torquebox:rpm:clean' do
  sh 'rm -Rf ./build/topdir' 
end

desc 'Build all RPMs for torquebox. '
task 'torquebox:rpm' => [ 'rpm:all', 'rpm:repodata:force' ]


###
### Rumpler
###
desc "Resolve dependencies for TorqueBox RPMs and scribble spec files"
task 'torquebox:rumpler' => [ 'sanity:dirs' ] do
  FileUtils.mkdir_p( 'specs/gems' )
  sh "../rumpler/bin/rumpler -f -r gemfiles/root.yml -o ./specs/gems/ -n torquebox-rubygems-dependencies -V #{BuildVersion.instance.torquebox_rpm}"
end

task 'torquebox:rumpler:clean' do
  sh 'rm -Rf specs/gems' 
end



##
# Appliances
##

desc "Build VMware"
task 'appliance:vmware' => 'torquebox:rpm' do
  sh "boxgrinder-build ./appliances/torquebox.appl -p vmware -d local"
end

task 'appliance:vmware:only' do
  sh "boxgrinder-build ./appliances/torquebox.appl -p vmware -d local"
end

desc "Build EBS AMI"
task 'appliance:ebs' => 'torquebox:rpm' do
  sh 'boxgrinder-build ./appliances/torquebox.appl -p ec2 -d ebs'
end

task 'appliance:ebs:only' do
  sh 'boxgrinder-build ./appliances/torquebox.appl -p ec2 -d ebs'
end

desc "Build S3 AMI"
task 'appliance:ami' => 'torquebox:rpm' do
  sh 'boxgrinder-build ./appliances/torquebox.appl -p ec2 -d ami'
end

task 'appliance:ami:only' do
  sh 'boxgrinder-build ./appliances/torquebox.appl -p ec2 -d ami'
end

task 'appliance:clean' => [ 'torquebox:rpm:clean', 'torquebox:rumpler:clean' ] do
  sh "rm -Rf build/topdir"
  sh "rm -Rf build/appliances"
end

