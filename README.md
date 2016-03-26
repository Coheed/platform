#Vagrant for Platform.sh + Drupal

#Vagrant Setup

##Pre-requisites
* Vagrant https://www.vagrantup.com/downloads.html
* Virtual Box https://www.virtualbox.org/wiki/Downloads
* A platform.sh project set up

##Steps
* git clone git@github.com:nicklz/platform.git
* cd platform/vagrant
* copy your own id_rsa file (ssh private key) into vagrant/environment/puppet/modules/base-lamp/files/ssh . Also make sure your Platform.sh account has your public key associated with it
* vagrant plugin install vagrant-hostsupdater
* vagrant up
* vagrant reload --provision (do this step if you see red errors.. need to fix this)
* vagrant ssh
* fab local.setup (say yes to everything + login)
* source .bashrc
* fab local.setup2 (say yes to everything)
* Visit in your browser: http://local.berkshireinnovationcenter.com (this is just the example project)
* Thats it!