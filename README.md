# Boxgrinder appliance definition files for steamcannon. 

For best results, use a BoxGrinder meta-appliance to build these images.  You can
find the meta-appliances here http://www.jboss.org/boxgrinder/downloads/build/meta-appliance.html

At the moment, only the 32-bit meta-appliances can sucessfully produce these images.

Some extra items are necessary to add to a meta-appliance 
to build cirras-rpm:

**Gems necessary to use:**

* rake
    * net-ssh
    * net-sftp

**Packages necessary to install:**

* (rhq-agent)
    * java-1.6.0-openjdk-devel

* (qemu)
    * zlib-devel 
    * SDL-devel

* (cirras-management)
    * libxml2-devel
    * libxslt-devel

# How to Launch the SteamCannon AMI

The easiest way to get an instance of SteamCannon up and running is to launch a SteamCannon appliance.
The current stable SteamCannon appliance ID is ami-a66f9bcf. Launch an instance of this with your choice
of Amazon tools and enjoy SteamCannon immediately.

# How to Build the SteamCannon AMI From Scratch

Building the SteamCannon AMI is done using the SteamCannon meta-appliance. This is a Fedora 13 machine image
that comes pre-rolled with everything you need to create and customize your own SteamCannon AMI to your liking.
The meta-appliance can be launched as an EBS-backed instance on EC2 using the ID ami-ae6296c7.  Or you can [Download](http://github.com/steamcannon/steamcannon-appliances/downloads) the latest VMware image from GitHub.

You may also try the beta version of the 1.4 32-bit image on Amazon using the ID ami-d819eeb1

You may also try the beta version of the 1.4 64-bit image on Amazon using the ID ami-6c30c705

Open up your Amazon AWS tool of choice, provide it with the AMI ID, and launch an instance.  Or, alternatively,
fire up VMware and load the image you downloaded.  SSH to the instance as root using 'boxgrinder' as your password.
It's a good idea to change the password once you login.  

We'll refer to this machine as SC-meta.  You will use it to build the SteamCannon AMI.  

When building the SteamCannon AMI, boxgrinder will attempt to register it with Amazon AWS and provide you with an
AMI ID when it's complete.  In order to do this, you'll need to have some configuration files in place.  Read
more about these options on the [BoxGrinder Plugins](http://community.jboss.org/wiki/BoxGrinderBuildPlugins) page.

Building the SteamCannon appliance involves downloading a number of repositories, and generating RPMs, and machine image files. 
BoxGrinder, Rake and [Rumpler](http://github.com/torquebox/rumpler) together make this possible.  Building the appliance
is just a couple of command lines.

    # cd /mnt/boxgrinder/steamcannon-appliances
    
If you want to build an EC2 EBS-backed image, issue the following command.

    # rake dist:appliance:ec2
    
If you want to build an EC2 AMI stored in S3, issue the following command.

    # rake dist:appliance:ami
    
If you want to build a machine image for VMware, issue the following command.

    # rake dist:appliance:vmware
    
This will build a number of RPMs and create the machine image file. The image will have all required RPMs, gems and other
dependencies. The SteamCannon database will be setup and seeded with in iniitial data, and JBoss will be configured and set 
to start on boot.  If you are creating an AMI for Amazon (whether EBS-backed or not), the image will be uploaded to Amazon
and registered as a new AMI.

The last line of the rake task looks something like this:

    # I, [2010-10-20T14:43:59.519772 #9500]  INFO -- : Image successfully registered under id: ami-561aee3f.

That's your new SteamCannon image.  Fire up your favorite Amazon AWS UI and launch it.  If all goes as planned,
you should have a new Fedora 13 instance running JBoss-AS with Torquebox and SteamCannon.  Enjoy!
