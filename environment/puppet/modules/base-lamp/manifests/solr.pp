class base-lamp::solr{
    
    $packageList = [
        "openjdk-7-jdk",
    ]

    package { $packageList: }

    exec{'rm -rf  mkdir /usr/java && mkdir /usr/java && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default':

    }

    file{'solr':
            path => '/home/vagrant/www/solr',
            ensure => present,
            recurse => true,
            source => "puppet:///modules/base-lamp/solr",
            owner => vagrant,
            group => vagrant;
    }

    

}