#!/usr/bin/pup
# Install flask with pip3 for exact version
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
