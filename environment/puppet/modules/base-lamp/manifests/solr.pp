class base-lamp::solr{
    
    $packageList = [
        "openjdk-7-jdk",
    ]

    package { $packageList: }

    exec{'rm -rf  mkdir /usr/java && mkdir /usr/java && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default':

    }

    exec{'wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz -O /opt/solr-4.7.2.tgz &&  tar -xvf /opt/solr-4.7.2.tgz && cp -R /opt/solr-4.7.2/example /opt/solr && java -jar /opt/start.jar':

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