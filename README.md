# TorqueBox Appliance

We use [BoxGrinder](http://boxgrinder.org) to build TorqueBox virtual machines
so you can start using TorqueBox today!  BoxGrinder is a set of projects from
[JBoss](http://jboss.org) that makes it easy to grind out appliances for
multiple virtualization and cloud providers.  TorqueBox currently provides a
64-bit appliance for [Amazon AWS](http://aws.amazon.com).  With the imminent
release of TorqueBox 1.0.0.Final we intend to also provide a 32-bit AWS
appliance, and a VMWare virtual machine.


## Running a TorqueBox Appliance

The TorqueBox 1.0.0.CR2 appliance is a 64-bit virtual machine: `ami-a8ca36c1`.
Use your favorite AWS tools to launch an instance. Once launched TorqueBox
should be running on port 8080.  To install
[stompbox](http://github.com/torquebox/stompbox) and/or
[backstage](http://github.com/torquebox/backstage) do the following:

    $ sudo su
    $ jruby -S backstage deploy --secure=user:pass
    $ jruby -S stompbox deploy --setup-db --auto-migrate --secure=user:pass

You are not required to set a username and password for these applications,
however it is strongly encouraged.  If you want to leave them wide open, omit
the `--secure` flag.  For stompbox, unless your database is already setup and
configured for stompbox, you'll need to include the `--setup-db` and
`--auto-migrate` flags.

## Building a TorqueBox Appliance

1. Get a [BoxGrinder Meta](http://boxgrinder.org/download/boxgrinder-build-meta-appliance/) appliance and fire it up

2. Login to the meta appliance: `ssh -i yourkey.pem ec2-user@public.dns.ami`

3. Configure /root/.boxgrinder/config as specified in the [BoxGrinder
   documentation](http://boxgrinder.org/tutorials/boxgrinder-build-plugins/#Plugin_configuration)

4. Become root `$ sudo su`

5. Clone torquebox-appliances in /mnt: `$ cd /mnt && git clone
   git://github.com/torquebox/torquebox-appliances.git`

6. Clone rumpler: `$ git clone git://github.com/torquebox/rumpler.git`

7. Rumple: `$ cd torquebox-appliances && rake torquebox:rumple`

8. Build RPMs: `$ rake torquebox:rpm`

9. Build an appliance `$ rake appliance:ebs`


