#!/usr/bin/env bash

sudo service apache2 stop
sudo service mysql stop
sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public
sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public
cd ~/www/platform/ && platform build
sudo service apache2 start
sudo service mysql start
cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz
cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local cc all && drush @bic._local fra -y && drush @bic._local cc all
cd ~/www/platform/_www && phpcbf