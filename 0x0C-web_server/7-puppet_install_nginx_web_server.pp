# This manifest installs nginx and adds redirect page

package {'nginx':
  ensure => present,
  name   => 'nginx',
}

file {'/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://youtu.be/myZ29u1gpWQ?t=83 permanent;',
}

service { 'nginx':
  ensure     => running,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['redirect_me'],
}
