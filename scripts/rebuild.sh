#!/usr/bin/env bash



sudo locale-gen  en_US.UTF-8 
export LC_ALL="en_US.UTF-8" 
export LANG="en_US.UTF-8" 

cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz

sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public
sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public
cd ~/www/platform/ && platform build
cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y
