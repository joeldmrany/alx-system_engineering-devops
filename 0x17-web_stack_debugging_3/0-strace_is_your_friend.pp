# it converts files with "phpp" into "php"

exec{'fix-code':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path	=> '/usr/local/bin/:/bin/'
}

