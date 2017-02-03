# self-teaching web dev project

### set up python development environment:
1. sudo apt-get update
1. sudo apt-get upgrade
1. install virtualenv
 * ```pip install virtualenv```
1. cd to directory you want to place virtual environment
1. create virtual environment called "venv"
 * ```virtualenv venv```
1. activate "venv"
 * ```source venv/bin/activate```

### set up git with github and ssh
1. initialize git
 * ```git init```
1. create .gitignore and readme.md files
 * ```touch .gitignore readme.md```
1. add all new/updated files in to "staging"
 * ```git add .```
1. "commits" changes to local git repo
 * ```git commit -am "commit message"```
1. creates new remote(github in this case) called "origin" for the URL specified
 * ```git remote add origin grabhttpsorsshaddressfromgithubrepo```
1. cd to default ssh directory
 * ```cd ~/.ssh```
1. create public/private RSA key pair
 * ```ssh-keygen -t rsa -C "email@email.com"```
1. from ~/.ssh, open id_rsa.pub, copy and paste ssh key to github repo
1. "push" or record changes to remote repo called "origin" from default local branch "master"
 * ```git push origin master```

### install and setup python flask
1. make sure virtual env is activated
1. install flask and other necessary flask extensions
 * ```pip install flask```
1. OR just install from requirements file
 * ```pip install -r requirements.txt```
1.  