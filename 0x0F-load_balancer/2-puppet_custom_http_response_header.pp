# File: nginx_setup.pp

# Install Nginx package

exec { 'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure => 'installed',
}

$file_contents = file('/etc/nginx/sites-enabled/default').content

if !($file_contents =~ /^(\s+)add_header X-Served-By/) {
  file_line { 'custom_header':
    ensure  => present,
    path    => '/etc/nginx/sites-enabled/default',
    line    => "    add_header X-Served-By '${::hostname}';",
    after   => '    root /var/www/html;'
  }
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['custom_header'],
}
