class base-lamp::solr{
    
    $packageList = [
        "openjdk-7-jdk",
        "solr-tomcat"
    ]

    package { $packageList: }

    exec{'rm -rf  mkdir /usr/java && mkdir /usr/java && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default':

    }

    file{'solr':
            path => '/usr/share/solr/conf',
            ensure => present,
            recurse => true,
            source => "puppet:///modules/base-lamp/solr",
            owner => vagrant,
            group => vagrant;
    }

    

}