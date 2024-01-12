# Django Restful Todo API

This example API is fully docker containerized with a postgresql database and authentication is fully managed using Django session based auth.

Of course this is a very simplified app but it is fully scalable.

Note : the commands following assumes that the user you use is part of the docker group. If not you will need to prefix every docker command with `sudo`.

## To run the App
```bash
docker compose up
```

Once the migrations are applied and everything is up, we need to create a superuser :
```bash
docker exec -it django-restful-api-web-1 /bin/bash

python manage.py createsuperuser
```

Fullfill every prompt the CLI gives you, then `exit` the container's bash session.

TODO :
- django session auth
- VueJS frontend