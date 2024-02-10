# Using Puppet, install flask from pip3.
#  Requirements:
#   Install flask
#   Version must be 2.1.0

# ensure python is installed
package {'python3.8':
  ensure => '3.8.10',
}

# ensure pip3 is installed
package {'python3-pip':
  ensure  => present,
  # require => Package['python3.8'],
}

# install flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# install Werkzeug 2.1.1
package {'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
