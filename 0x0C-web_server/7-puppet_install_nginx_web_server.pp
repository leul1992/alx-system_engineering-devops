# install nginx
exec { 'install nginx':
   command  => 'apt-get -y update;apt-get -y install nginx',
}

# quering nginx
exec { 'quering':
   command => 'echo "Hello World!" > /var/www/html/index.html',
}

#redirecting page
exec { 'redirect':
   command => 'sed -i "37i\rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
}

# restart nginx
exec { 'restart':
   command => 'service nginx restart',
}
