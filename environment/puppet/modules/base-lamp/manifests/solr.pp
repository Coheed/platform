class base-lamp::solr{
    
    $packageList = [
        "openjdk-7-jdk",
        "solr-tomcat"
    ]

    package { $packageList: }

    exec{'mkdir /usr/java && ln -s /usr/lib/jvm/java-7-openjdk-amd64 /usr/java/default':

    }
    
    

}