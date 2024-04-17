#!/usr/bin/env bash
# Puppet automation using SSH Client Configuration

file {'/etc/ssh/ssh_config':
   ensure => present,
  content => "
        # SSH Client Configuration
        Host *
              PasswordAuthentication no
              IdentityFile ~/.ssh/school
        ",
}

