#flasky 
chp8,page 103
11/23 Thurs

#Registered
user: halvong@yahoo.com
passwd: 123

user: halvong5@gmail.com
passwd: 123

Database Use in View Functions

#run
	1. starts postgresql
		sudo systemctl status, start postgresql	

	2. postgresql commands
		su - tom
		psql -d flasky
		\d - show tables
		\l - show databases
		\c <database> - connects
		\q - quit

	3. gunicorn -b 0.0.0.0:3000 --access-logfile - "flasky.app:create_app()" 
	
	4. su - tom
	   psql -d flasky

#-----------------------------------
#new project
1. change FROM python:3.6-alpine in Dockerfile 
2. check requirements.txt

#----
#creates <project>.egg-info
1. In the root folder, 
 	a. copy appropriate setup.py		
 	b. ensure setup.py name correlates to project name 
	c. ~/venv3/bin/activate 
	d. pip install --editable .  

#-----------------------------------
#path to source
cd /home/hal/Documents/softwares/python_eclipse/workspace/flask; source ~/venv3/bin/activate
cd /home/hal/Documents/softwares/python_eclipse/workspace/flask

#code path
cd /home/hal/Documents/codes/flask/flasky

#-----------------------------------
#starts app

#create image of app, build once when code changes
docker-compose up --build

	1. go to localhost:3000	

#starts app
docker-compose up

#stops app
docker-compose stop

#starts with Click
docker-compose up --build
docker-compose exec website flasky
docker-compose exec website flasky flake8

#-----------------------------------
#make changes

#Port
	1. docker-compose.yml 
	2. Dockerfile 
	3. config/settings: servername

#-----------------------------------
#docker commmands

#docker initialized
docker-compose exec website snakeeyes db init
docker-compose exec website snakeeyes db seed

#show all images
docker images

#show all containers
docker-compose ps

#show container pertains to this project
docker ps

#removes containers of this project 
docker-compose rm -f

#removes dangling images
docker rmi -f $(docker images -qf dangling=true)

#installation of dependencies
#install docker-compose
https://docs.docker.com/compose/install/#install-compose

#-----------------------------------------------------------
Flask==0.10.1

# Application server for both development and production.
gunicorn==19.4.5

#
flask-bootstrap

# Testing and static analysis.
pytest==2.9.1
pytest-cov==2.2.1
flake8==2.5.4

# CLI.
Click==6.4

# Data and workers.
redis==2.10.5
celery==3.1.23

# Forms.
Flask-WTF==0.9.5
WTForms-Components==0.9.7

# Extensions.
flask-debugtoolbar==0.10.0
Flask-Mail==0.9.1
flask-moment