Ticket Management REST API
=============

Files for my helpdesk/ticket managment server written in Python-Flask. Here are the articles:
Following are the key points related to project:
1. This is just small scale ticket managment system using Flask-Restful.
2. At the backend it uses MySQL database.
3. MySQL and Flask application in dockerized and can be lunched using docker-compose.
4. Token based authentication is used in this project.
5. There is seperate database initialization script to insert initial data into the database.
6. Application is deployed using uwsgi server.
7. To run development server execute `dbmigrate.sh`. This script will perform database
table migration from flask ORM models and run application using uwsgi server.
(We can comment out line `python manage.py runserver` to run application on python server.)


Setup
-----

- Install Python 3 and git.
- Export enviroment i.e. development, testing, production, etc.
```bash
export env=production
```
- Run `docker-compose up` to build and run MySQL-flask application container.
- To Get Token:

```
$ curl -X POST -H "Content-Type:application/json" -d '{"username":"admin","password":"admin123"}' http://localhost:9090/api/login
{
    "message": "Hii!",
    "token": "WyIxIiwiOThiZmVlMjFlZjljYTU0NzZkYzNmMTUyODUzNDM2MzgiXQ.CgpV7Q.ypduIJefgJAdHAbB_WIrLzfsXYc"
}
```



