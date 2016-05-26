#!/usr/bin/env bash



sudo locale-gen  en_US.UTF-8 
export LC_ALL="en_US.UTF-8" 
export LANG="en_US.UTF-8" 

cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz
