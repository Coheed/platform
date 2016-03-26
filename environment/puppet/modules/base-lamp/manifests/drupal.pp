class base-lamp::drupal {

    file{'settings.local.php':
            path => '/home/vagrant/www/settings.local.php',
            ensure => present,
            source => "puppet:///modules/base-lamp/drupal/settings.local.php",
            owner => vagrant,
            group => vagrant,
            mode => 0644;
    }

}