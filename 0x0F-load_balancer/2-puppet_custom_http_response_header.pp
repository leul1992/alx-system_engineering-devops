exec { 'install_nginx':
    command => 'sudo apt-get -y update;sudo apt-get -y install nginx'
}
exec { 'put_header':
    command => 'sed -i "/server_name _;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default;sudo service nginx restart'
}
