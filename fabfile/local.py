# import os
# from fabric.api import cd
from fabric.api import lcd
# from fabric.api import sudo
# from fabric.api import run
# from fabric.api import show
from fabric.api import get
# from fabric.api import put
from fabric.colors import green
#from fabric.colors import cyan
from fabric.colors import red
from fabric.api import local
from fabric.api import task
from fabric.api import roles
from fabric.api import execute
from fabric.api import settings
# import css as _css

      
      
@task
def setup():
    with settings(warn_only=True):
        # Install local database from dev server
        
        
        
        
        local('sudo locale-gen  en_US.UTF-8')
        local('export LC_ALL="en_US.UTF-8"')
        local('export LANG="en_US.UTF-8"')

        #so we dont have to type yes

        local('ssh-keyscan -H github.com >> ~/.ssh/known_hosts')

        local('ssh-keyscan -H keys.gnupg.net >> ~/.ssh/known_hosts')

        local('ssh-keyscan -H raw.githubusercontent.com >> ~/.ssh/known_hosts')

        local('ssh-keyscan -H platform.sh >> ~/.ssh/known_hosts')

        local('ssh-keyscan -H git.us.platform.sh >> ~/.ssh/known_hosts')
        
        
        local('ssh-keyscan -H ssh.us.platform.sh >> ~/.ssh/known_hosts')
        
        
                

        
        local('echo "drop database berkshireinnovationcenter;" | mysql -uroot')
        local('echo "create database berkshireinnovationcenter;" | mysql -uroot')
        #local('mysql -u root -p berkshireinnovationcenter --password="" < /home/vagrant/www/sites/local.berkshireinnovationcenter.com/dump.sql')


        local('curl -sS https://getcomposer.org/installer | php')
        local('sudo mv composer.phar /usr/local/bin/composer')
        

        #local('composer global config minimum-stability dev')
        local('composer require drush/drush')
        local('composer global require drupal/coder')
        local('export PATH="$PATH:$HOME/vendor/bin"')
        local('export PATH="$PATH:$HOME/.config/composer/vendor/bin"')
        
        
        
        
        

        local('curl -sS https://platform.sh/cli/installer | php')
        
        local('echo \'export PATH="$PATH:$HOME/vendor/bin:$HOME/.config/composer/vendor/bin"\' >> ~/.bashrc')

        #https://github.com/MasterDoublePrime/BIC-project/wiki/Development-With-Platform.sh



@task
def setup2():
    with settings(warn_only=True):
        local('cd ~ && source .bashrc')
        local('ln -s ~/.config/composer ~/.composer')
        
        local('phpcs --config-set installed_paths ~/.config/composer/vendor/drupal/coder/coder_sniffer')
        local('cd ~ && platform')
        local('cd ~ && platform get cld2r5664mncw www/platform')
        local('cd ~/www/platform && platform drush-aliases -g bic')

        local('cd ~/www/platform && git remote remove origin')
        local('cd ~/www/platform && git remote add upstream git@github.com:MasterDoublePrime/BIC-project.git')
        local('cd ~/www/platform && git remote add origin git@github.com:nicklz/BIC-project.git')
        local('cd ~/www/platform && git fetch --all')
        local('cd ~/www/platform && platform build')


        local('cat /home/vagrant/www/settings.local.php > /home/vagrant/www/platform/.platform/local/shared/settings.local.php')


        local('cd ~/www/platform/ && git config --global user.email "nicholas.kuhn@spi.com"')
        local('cd ~/www/platform/ && git config --global user.name "Nick Kuhn"')
        local('cd ~/www/platform/ && git config --global core.editor "vim"')


        local('cd ~/www/platform/ && git config --global core.editor "vim"')
        local('cd ~ && wget http://archive.apache.org/dist/lucene/solr/4.7.2/solr-4.7.2.tgz && sudo tar -xvf solr-4.7.2.tgz && sudo cp -R solr-4.7.2/example /opt/solr && sudo cp /home/vagrant/solr/conf/* /opt/solr/solr/collection1/conf/ -rf && cd /opt/solr &&  sudo java -jar start.jar &')



        local("cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz")
        #https://github.com/MasterDoublePrime/BIC-project/wiki/Development-With-Platform.sh




@task
def sync():
    with settings(warn_only=True):
        # Install local database from dev server
        local("cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz")



@task
def update():
    with settings(warn_only=True):
        # Install local database from dev server

        local('sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('cd ~/www/platform/ && platform build')
        local('cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y')



@task
def rebuild():
    with settings(warn_only=True):
        # Install local database from dev server
        local('sudo service apache2 stop')
        local('sudo service mysql stop')
        local('sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('cd ~/www/platform/ && platform build')
        local('sudo service apache2 start')
        local('sudo service mysql start')
        local("cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz")
        local('cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y')
        local('cd ~/www/platform/_www && phpcbf')
         




@task
def revert():
    with settings(warn_only=True):
        # Install local database from dev server
        local("cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz")
        local('cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y')
        



@task
def fix():
    with settings(warn_only=True):
        # Install local database from dev server
        local('cd ~/www/platform/_www && phpcbf')
        
        
@task
def check():
    with settings(warn_only=True):
        # Install local database from dev server
        local('cd ~/www/platform/_www && phpcs')
        
        