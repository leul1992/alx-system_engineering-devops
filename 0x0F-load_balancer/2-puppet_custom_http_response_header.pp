# creating a custom HTTP header response
exec { 'customHTTP':
    provider => shell,
    command  => 'sudo apt-get -y update;sudo apt-get -y install nginx;sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default;sudo service nginx restart'
}
