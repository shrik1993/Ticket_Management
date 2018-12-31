Ticket Management REST API
=============

Files for my helpdesk/ticket managment server written in Python-Flask. Here are the articles:
Following are the key points related to project:
1. This is just small scale ticket managment system using Flask-Restful.
2. At the backend it uses MySQL database.
3. MySQL and Flask application in dockerized and can be lunched using docker-compose.
4. Token based authentication and Role based access filter is implemented in this project.
5. There is seperate database initialization script to insert initial data into the database.
6. Application is deployed using uwsgi server.
7. To script `dbmigrate.sh` will perform database table migration from Flask ORM models 
and run application using uwsgi server.
8. Token is valid only for 1 hour.


Setup
-----

- Install Python 3 and git.
- Export enviroment i.e. development, testing, production, etc.
```bash
export env=production
```
- Run `docker-compose up` to build and run MySQL-flask application container.
- As this API implements token based authentication you need to get the token from `/api/login` 
- Execute following commands to get token and perfoem CRUD operation on tickets using REST APIs. 

NOTE: To get token you require username and password. Bydefault this application creates guest and admin user.

1. To get the access token:
```
$ curl -X POST -H "Content-Type:application/json" -d '{"username":"admin","password":"admin123"}' http://localhost:9090/api/login
{
    "message": "Hii!",
    "token": "WyIxIiwiOThiZmVlMjFlZjljYTU0NzZkYzNmMTUyODUzNDM2MzgiXQ.CgpV7Q.ypduIJefgJAdHAbB_WIrLzfsXYc"
}
```

2. To add ticket:
```
$ curl -X POST -H "Content-Type:application/" -H "Authorization:WyIyIiwiJDUkcm91bmRzPTUzNTAwMCRxSEZOLjdBY211QmlVaHhLJENOTmZ5SmRvZnFWUHRDVXRpQUx1TTgvRjJNOEVuanRBY1ZjLlZXdzB3cjAiXQ.XCmHGg.XSdOnMKbCRS8DCZ8QTaFiIvlIoA" -d '{"title":"ticket1","description":"Urgent requirement.", "done": "False", "assigned_to":"foo"}' http://localhost:9090/api/tickets
{
    "results": "Ticket created successfully!"
}
```

3. Use token and access `/api/tickets` using `GET` method to get all tickets.
```
curl -X GET -H "Content-Type:application/json" http://localhost:9090/api/tickets
{
    "results": [
        {
            "id": "1",
            "title": "ticket1",
            "done": "false",
            "description": "Urgent requirement",
            "assigned_to": "foo"
        },
    ],
    "count": 1
}
```

4. Modify particular ticket using ticket ID:
```
curl -X PUT -H "Content-Type:application/json" -H "Authorization:WyIyIiwiJDUkcm91bmRzPTUzNTAwMCRrR2NYRUxNMG5SWEo1emJVJEt0TUZKQ2FKMi9LTFVHUGFLZzJTbXZMdzd0by5UYWFBNTlLRElHN1VPQjYiXQ.XCmPrg.1XsgMVETYg7CkHPxIijxWgXphZ4" -d '{"title":"ticket1","description":"Urgent requirement.", "done": "Done", "assigned_to":"foo1"}' http://localhost:5000/api/ticket/1
{
    "results": [
        "Updated Ticket ID: 2"
    ]
}
``` 

5. Delete particular ticket using ticket ID:
```
curl -X DELETE -H "Content-Type:application/json" -H "Authorization:WyIyIiwiJDUkcm91bmRzPTUzNTAwMCQ4ajlnN0FEZ0RTWS5Da25YJE9LelN1MmVBY2lqcnlOdC5hbzRkaGpCSE02aC5rTlpKaFdhZWpnZDJKMzAiXQ.XCmTUQ.sQl7EAiSlgBxJld4z5hvI6j-xI8"  http://localhost:5000/api/ticket/2
{
    "results": "Successfully deleted ticket ID: 2"
}
```


Note: This is just small scale project for demo purpose.
