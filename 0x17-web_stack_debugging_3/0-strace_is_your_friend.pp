# fixes apache returning 500 error by fixing wordpress config file
exec { 'configure wordpress':
  provider => shell,
  command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
}
