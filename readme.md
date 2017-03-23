# self-teaching web dev: flask project

### set up python development environment
1. download package list information on newest versions of packages
1. fetch new versions of packages on machine
1. install virtualenv
1. create virtual environment
1. activate virtual environment "venv"
   ```
   sudo apt-get update
   sudo apt-get upgrade
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   ```

### set up git with github and ssh
1. initialize git
1. create .gitignore and readme.md files
1. add all new/updated files in to "staging"
1. "commits" changes to local git repo
1. create new remote(github in this case) called "origin" for the URL specified
    ```
    git init
    touch .gitignore readme.md
    git add .
    git commit -am "commit message"
    git remote add origin grabhttpsorsshaddressfromgithubrepo
    ```
1. create public/private RSA key pair
    ```
    ssh-keygen -t rsa -C "email@email.com"
    ```
1. open id_rsa.pub, copy and paste ssh key to github repo
1. "push" or record changes to remote repo called "origin" from default local branch "master"
    ```
    git push origin master
    ```

### install and set up python flask project
1. make sure virtual environment is activated
1. install flask and other flask extensions
    ```
    pip install flask
    ```
1. OR just install them all from requirements file
    ```
    pip install -r requirements.txt
    ```
1. run app using simple builtin server
    ```
    export FLASK_APP=run.py
    flask run
     * Running on http://127.0.0.1:5000/
    ```

### install and set up mysql db
