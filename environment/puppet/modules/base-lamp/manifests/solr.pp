class base-lamp::solr{
    
    $packageList = [
        "openjdk-7-jdk",
    ]

    package { $packageList: }

    exec{'rm -rf  mkdir /usr/java && mkdir /usr/java && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default':

    }

    exec{'cd /opt && sudo wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz && sudo tar -xvf solr-4.7.2.tgz && sudo cp -R solr-4.7.2/example /opt/solr && cd /opt/solr && sudo java -jar start.jar':

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