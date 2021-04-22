# Bloggy

Blog application developed in Django3.
Application was developed with the support of a book [Django 3 By Example - Third Edition](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952).


### **Installation**
> 1) create .env and .env.db file (see [env section](#env-files) for more details)
> 2) cd blog_project
> 3) python manage.py collectstatic
> 4) cd ..
> 5) docker-compose build
> 6) docker-compose up

Notice that docker and docker-compose are required for running this application.

If everything is fine, the application should be available at address http://0.0.0.0:1337.

### **Access to app container**
> docker exec -it bloggy_app sh

### **How to add blog admin**
> 1) docker exec -it bloggy_app sh
> 2) python manage.py createsuperuser
> 3) provide username, e-mail and password
> 4) confirm user was created by logging on http://0.0.0.0:1337/admin.

### **env files**
.env file structure:
```
DEBUG=0
SECRET_KEY=SECURE_KEY_FOR_HASHING
DB_NAME=bloggy
DB_USER=POSTGRES_USERNAME
DB_PASS=POSTGRES_PASSWORD
DATABASE=postgres
EMAIL_HOST=SENDING_SERVER_ADDRESS
EMAIL_HOST_USER=EMAIL_ADDRESS
EMAIL_HOST_PASSWORD=EMAIL_PASSWORD
EMAIL_PORT=E_MAIL_PORT
EMAIL_USE_TLS=ENABLE TSL (0 for disabling, 1 for enabling)
```

.env.db file structure:
```
POSTGRES_DB=bloggy
POSTGRES_USER=POSTGRES USERNAME
POSTGRES_PASSWORD=POSTGRES PASSWORD
```
