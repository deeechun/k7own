#self-teaching web dev project

##set up python development environment:
1. sudo apt-get update
1. sudo apt-get upgrade
1. pip install virtualenv
1. cd to directory you want to place virtual environment
1. virtualenv venv
1. source venv/bin/activate

##set up git with github and ssh
1. git init
1. touch .gitignore
1. touch readme.md
1. git add .
1. git commit -am "commit message"
1. git remote add origin grabhttpsorsshaddressfromgithubrepo
1. cd ~/.ssh
1. ssh-keygen -t rsa -C "email@email.com"
1. from .ssh/id_rsa.pub copy and paste ssh key to github repo
1. git push -origin master

##install and setup python flask
1. pip install flask OR pip install -r requirements.txt
1. 