# STOREFRONT APP API
this is A full online shopping store API designed from scratch 
that contains a well-structured database, restful API, and a great 
future.


Tech stacks of this project:
* Django / Djago Rest Framework
* Docker
* MYSQL  
* Redis
* Celery 
* JWT
* Pytest as a test tool


### 1.  Download the project:

* `git clone "https://github.com/arefyazdi4/storefront`


### 2.  Build The Project:

* `docker-compose build`

### 3.  Running the project:

* `docker-compose up ` \ `docker-compose up -d`
      

### 4.  Setting up the project:
* `docker exec -it storefrontApp sh`
* `python manage.py migrate `  
* `python manage.py seed_db   `
* `python manage.py createsuperuser   `


## 5.  Now you can see Browsable Api
* Api to Homepage -> `127.0.0.1:8000/`
* Admin Panel -> `127.0.0.1:8000/admin/`
* Api to JWT authentication -> `127.0.0.1:8000/auth/jwt/create/`

LICENCE: The Ultimate Django _ CodewithMosh.com