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
        local('echo "drop database berkshireinnovationcenter;" | mysql -uroot')
        local('echo "create database berkshireinnovationcenter;" | mysql -uroot')
        #local('mysql -u root -p berkshireinnovationcenter --password="" < /home/vagrant/www/sites/local.berkshireinnovationcenter.com/dump.sql')


        local('curl -sS https://getcomposer.org/installer | php')
        local('sudo mv composer.phar /usr/local/bin/composer')
        local('echo \'export PATH="$PATH:$HOME/.composer/vendor/bin"\' >> ~/.bashrc')
        local('composer global require drush/drush:dev-master')

        local('curl -sS https://platform.sh/cli/installer | php')

        #https://github.com/MasterDoublePrime/BIC-project/wiki/Development-With-Platform.sh



@task
def setup2():
    with settings(warn_only=True):
        local('cd ~ && source .bashrc')
        local('cd ~ && platform')
        local('cd ~ && platform get cld2r5664mncw www/platform')
        local('cd ~/www/platform && platform drush-aliases -g bic')

        local('cd ~/www/platform && git remote remove origin')
        local('cd ~/www/platform && git remote add upstream git@github.com:MasterDoublePrime/BIC-project.git')
        local('cd ~/www/platform && git remote add origin git@github.com:nicklz/BIC-project.git')
        local('cd ~/www/platform && git fetch --all')
        local('cd ~/www/platform && platform build')


        local('cat /home/vagrant/www/settings.local.php > /home/vagrant/www/platform/.platform/local/shared/settings.local.php')
        local('cd ~/www/platform/_www && drush @bic.phase-3 sql-dump | drush @bic._local sqlc')

        local('cd ~/www/platform/ && git config --global user.email "nicholas.kuhn@spi.com"')
        local('cd ~/www/platform/ && git config --global user.name "Nick Kuhn"')
        local('cd ~/www/platform/ && git config --global core.editor "vim"')


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
        local("cd ~/www/platform/_www && drush sql-sync @bic.phase-3 @bic._local --create-db -y --source-dump=/tmp/tmp.sql.gz --target-dump=/tmp/tmp.sql.gz")

        local('sudo chmod 777 -R /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('sudo rm -rf /home/vagrant/www/platform/.platform/local/builds/default/public')
        local('cd ~/www/platform/ && platform build')
        local('cd ~/www/platform/_www && drush @bic._local updb -y && drush @bic._local fra -y')

