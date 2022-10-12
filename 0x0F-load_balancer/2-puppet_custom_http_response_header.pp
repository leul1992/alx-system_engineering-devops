# creating a custom HTTP header response
service { 'nginx':
    ensure => running,
    require => Package['nginx'],
}
exec { 'customHTTP':
    provider => shell,
    command  => 'sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default;sudo service nginx restart'
}
