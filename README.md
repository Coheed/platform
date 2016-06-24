#Vagrant for Platform.sh + Drupal

#Vagrant Setup

##Pre-requisites
* Vagrant https://www.vagrantup.com/downloads.html
* Virtual Box https://www.virtualbox.org/wiki/Downloads
* A platform.sh project set up

##Steps
* git clone git@github.com:nicklz/platform.git
* cd platform/vagrant
* cp ~/.ssh/id_rsa environment/puppet/modules/base-lamp/files/ssh/ (** ensure your ssh key has been added to your platform.sh account **)
* vagrant plugin install vagrant-hostsupdater
* vagrant up
* vagrant reload
* vagrant ssh
* source ./scripts/setup.sh
* Visit in your browser: http://local.berkshireinnovationcenter.com (this is just the example project)
* Thats it!