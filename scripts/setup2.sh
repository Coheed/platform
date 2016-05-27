
cd ~ && source .bashrc
cd ~ && platform
cd ~ && platform get cld2r5664mncw www/platform
cd ~/www/platform && platform drush-aliases -g bic

cd ~/www/platform && git remote remove origin
cd ~/www/platform && git remote add upstream git@github.com:MasterDoublePrime/BIC-project.git
cd ~/www/platform && git remote add origin git@github.com:nicklz/BIC-project.git
cd ~/www/platform && git fetch --all
cd ~/www/platform && platform build


cat /home/vagrant/www/settings.local.php > /home/vagrant/www/platform/.platform/local/shared/settings.local.php


cd ~/www/platform/ && git config --global user.email "nicholas.kuhn@spi.com"
cd ~/www/platform/ && git config --global user.name "Nick Kuhn"
cd ~/www/platform/ && git config --global core.editor "vim"


cd ~/www/platform/ && git config --global core.editor "vim"
cd ~ && wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz && sudo tar -xvf solr-4.7.2.tgz && sudo cp -R solr-4.7.2/example /opt/solr && sudo cp /home/vagrant/solr/conf/* /opt/solr/solr/collection1/conf/ -rf && cd /opt/solr &&  sudo java -jar start.jar &



cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz