#!/usr/bin/env bash

#this was causing ssh errors
sudo locale-gen  en_US.UTF-8 
export LC_ALL="en_US.UTF-8" 
export LANG="en_US.UTF-8" 

#so we dont have to type yes

ssh-keyscan -H github.com >> ~/.ssh/known_hosts

ssh-keyscan -H keys.gnupg.net >> ~/.ssh/known_hosts

ssh-keyscan -H raw.githubusercontent.com >> ~/.ssh/known_hosts

ssh-keyscan -H platform.sh >> ~/.ssh/known_hosts

yes | sudo apt-get install tofrodos  

echo "drop database berkshireinnovationcenter;" | mysql -uroot
echo "create database berkshireinnovationcenter;" | mysql -uroot
#mysql -u root -p berkshireinnovationcenter --password="" < /home/vagrant/www/sites/local.berkshireinnovationcenter.com/dump.sql


curl -sS https://getcomposer.org/installer | php
sudo mv composer.phar /usr/local/bin/composer
echo 'export PATH="$PATH:$HOME/.composer/vendor/bin"' >> ~/.bashrc
composer global config minimum-stability dev
composer global require drush/drush:dev-master

curl -sS https://platform.sh/cli/installer | php

