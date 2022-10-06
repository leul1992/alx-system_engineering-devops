# configure server
exec { 'configure server':
  provider => shell,
  command  => 'apt-get -y update;apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.html;sed -i "/server_name _;/a location /redirect_me {\\n\\treturn 301 https://google.com; \\n\\t}\\n" /etc/nginx/sites-available/default; service nginx restart'
}
