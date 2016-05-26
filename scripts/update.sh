#!/usr/bin/env bash


sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public
sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public
cd ~/www/platform/ && platform build
cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y