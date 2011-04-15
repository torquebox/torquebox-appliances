
def determine_value(file_path, key)
  File.open( file_path ) do |f|
    f.each_line do |line|
      if ( line =~ %r(^\s*%define\s*#{key}\s*([^\s]+)) )
        return $1
      end
    end
  end
  nil
end

def scribble_config(plugin, options = {})
  copy( boxgrinder_config_file(plugin), boxgrinder_config_file_bak(plugin) )
  config = YAML.load_file( boxgrinder_config_file(plugin) )
  config.merge!(options)
  File.open( boxgrinder_config_file(plugin), 'w' ) do |out|
    YAML.dump( config, out )
  end
end

def restore_config(plugin)
  move( boxgrinder_config_file_bak(plugin), boxgrinder_config_file(plugin) )
end

def scribble_s3
  copy( boxgrinder_config_file('s3'), boxgrinder_config_file_bak('s3') )
  config = YAML.load_file( boxgrinder_config_file('s3') )
  config['bucket'] = config['bucket'] + "-" + rand(10000).to_s
  File.open( boxgrinder_config_file('s3'), 'w' ) do |out|
    YAML.dump( config, out )
  end
end

def restore_s3
  move( boxgrinder_config_file_bak('s3'), boxgrinder_config_file('s3') )
end

def boxgrinder_config_file(plugin)
  "#{ENV['HOME']}/.boxgrinder/plugins/#{plugin}"
end

def boxgrinder_config_file_bak(plugin)
  boxgrinder_config_file(plugin) + ".bak"
end

class BuildVersion
  include Singleton

  attr_accessor :torquebox, :torquebox_rpm

  def initialize()
    @torquebox         = nil
    @torquebox_rpm     = '1.0.0.CR1'

#    torquebox_versions = {}
#    Dir[ './specs/*.spec' ].each do |spec|
#      version = determine_value( spec, 'torquebox_build_number' )
#      ( torquebox_versions[spec] = version ) unless version.nil?
#    end
#    if ( torquebox_versions.values.uniq.size == 1 )
#      @torquebox = torquebox_versions.values.uniq.first
#    else
#      puts "TorqueBox build number mismatch!"
#      torquebox_versions.each do |spec, ver|
#        puts "  #{ver} - #{spec}"
#      end
#      raise( "TorqueBox build number mismatch" )
#    end
  end

end

