# Django Restful Todo API

This example of a Django REST Framework API is fully docker containerized with a postgresql database and authenticated using Django session based auth.

Of course this is a very simplified app but it is fully scalable.

## To run the App
>**_NOTE:_** The following commands assume that the user is part of the docker group. If he is not you will need to prefix every docker command with `sudo`.
```bash
docker compose up
```

Once the migrations are applied and both containers are up, we need to create a superuser:
```bash
docker exec -it django-restful-api-web-1 /bin/bash

python manage.py createsuperuser
```

Fullfill every prompt the CLI gives you, then `exit` the container's bash session.

## How does it work
The base URL is `localhost:8000/api/todos`. This URL accepts: 
- GET requests from unauthenticated users and will return every elements in the table in a read-only manner.
- POST requests from authenticated users only and will create an element owned by the user.

The URL `localhost:8000/api/todos/{id}` will accepts: 
- GET requests from unauthenticated users and will return the element with corresponding id.
- PUT requests from owner only that will update the element in the database.
- DELETE requests from owner only that will delete the element in the database.

Coming soon :
- Django session auth
- VueJS frontend