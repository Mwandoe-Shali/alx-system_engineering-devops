#!/usr/bin/env ruby
# A regular expression that matches t{2,5} times
puts ARGV[0].scan(/hbt{2,5}n/).join