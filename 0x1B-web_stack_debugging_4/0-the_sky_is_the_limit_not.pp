# Incresing the trafic of the server

#execute the file
exec { 'fix--for-nginx':
  # Modifying
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  # Specifying
  path    => '/usr/local/bin/:/bin/',
}

# Restart
exec { 'nginx-restart':
  # Restarting
  command => '/etc/init.d/nginx restart',
  # Specifiying
  path    => '/etc/init.d/',
}
