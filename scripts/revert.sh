#!/usr/bin/env bash

cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz
cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y