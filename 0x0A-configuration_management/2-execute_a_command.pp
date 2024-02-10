# Using Puppet, create a manifest that kills a process named killmenow.
#
#	Requirements:
#
#	Must use the exec Puppet resource
#	Must use pkill

exec {'kill_a_process':
  command => 'pkill killmenow',
  path    => ['/usr/bin' , '/usr/sbin'],
}
