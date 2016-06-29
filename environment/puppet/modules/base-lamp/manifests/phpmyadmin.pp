class base-lamp::phpmyadmin{
    file{'phpmyadmin':
            path => '/home/vagrant/phpmyadmin',
            ensure => present,
            recurse => true,
            source => "puppet:///modules/base-lamp/phpmyadmin";

    }

}