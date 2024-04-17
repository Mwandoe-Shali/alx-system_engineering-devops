# Enables the user holberton to login and open files
#         without error by changing OS configuration.

# Increase hard file limit for user holberton
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/55555/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/44444/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
