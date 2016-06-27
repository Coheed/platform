#!/usr/bin/env bash

cd ~/www/platform/_www && drush sql-sync @bic.master @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz