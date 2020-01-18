#  Greenely  application

## Setup

At the first you can  clone the repository:
```sh
$ git clone https://gitlab.com/m.rezaei67/greenely.git

```

You can setup with Docker or virtual environment.
 
### setup with **Docker** first

It's very simple, and you should run the below command inthe root directory which exist docker-compose.yml file:

    docker-compose up
    
Now you can browse to http://127.0.0.1:8000 and use the API's.

### setup with  **virtual environment** 
Create a virtual environment (with python 3) to install dependencies in and activate it:

    sudo apt-get install python3-pip

##### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

##### Now create a virtual environment 

    virtualenv greenelyEnv 

### Active your virtual environment:    
    
    source greenelyEnv/bin/activate

Then install the dependencies so you should got to the directory that existed _manage.py_:

```sh
(greenelyEnv)$ cd greenely
(greenelyEnv)$ pip install -r requirement.txt
```
Note the `(greenelyEnv)` in front of the prompt.

Once `pip` has finished downloading the dependencies :
```sh
(greenelyEnv)$ python manage.py makemigrations users
(greenelyEnv)$ python manage.py makemigrations authentication
(greenelyEnv)$ python manage.py makemigrations consumption
(greenelyEnv)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## API list information
There are 4 API's and it's worth mentioning that there is a postman collection in the root directory of project that is named _**greenely.postman_collection.json**_. So you can easily import this file to your postman application and see all of the API's.
However I put some description about the API's.


### 1- signup
 You can easily open below url in your browser and fill the blanks to register a user and then get a JWT token (for the access to the others API's):
 
```sh
http://127.0.0.1:8000/api/v1/auth/signup/
```

### 2- login
If you signed up a user, you can get JWT token with your username and password with the following API. I should say that for the login api you can use your browser :

```sh
http://127.0.0.1:8000/api/v1/auth/login/
```

### 3- data

This Api uses for getting the consumption data of current user based on query parameters:

```sh
curl -X GET \
  'http://127.0.0.1:8000/api/v1/consumption/data/'
```
Also there is an example with query parameters and token of user:

```sh
curl -X GET \
  'http://127.0.0.1:8000/api/v1/consumption/data/?start=2014-09-1&resolution=M&count=3 \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IkFsaSIsImV4cCI6MTU3OTM4MTQxMCwiZW1haWwiOiJzZGZAeWFob28uY29tIiwiaXAiOiIxMjcuMC4wLjEifQ.JgRMQZcRazYnccGteZEttd0sEym8ZFvXN280mOjqNTY'
```

### 4- limit
This Api uses for getting the information of max and min consumption values of current user :

```sh
curl -X GET \
  'http://127.0.0.1:8000/api/v1/consumption/limit/'
```
There is an example for limit api with the token:

```sh
curl -X GET \
  'http://127.0.0.1:8000/api/v1/consumption/limit/ \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IkFsaSIsImV4cCI6MTU3OTM4MTQxMCwiZW1haWwiOiJzZGZAeWFob28uY29tIiwiaXAiOiIxMjcuMC4wLjEifQ.JgRMQZcRazYnccGteZEttd0sEym8ZFvXN280mOjqNTY'
```


## JWT token 
I used [JWT](https://jpadilla.github.io/django-rest-framework-jwt/) for authentication so aftre calling signup API you get a token in response that should be used for the protected APIs. 
The signup and login API are unprotected but the other APIs need to send authorization token in header of HTTP request and it has bareer "JWT" in the first of token. There is an example for calling an API with token:
Also for search greenely API there is a sample:
```sh
curl -X GET \
  'http://127.0.0.1:8000/api/v1/consumption/data/?start=2014-09-1&resolution=M&count=3 \
  -H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IkFsaSIsImV4cCI6MTU3OTM4MTQxMCwiZW1haWwiOiJzZGZAeWFob28uY29tIiwiaXAiOiIxMjcuMC4wLjEifQ.JgRMQZcRazYnccGteZEttd0sEym8ZFvXN280mOjqNTY'
```

## Swagger
Also there are the list of all API with the related input in swagger page. so you see the unprotected APIs at the first time but you can login with your user credential that you created with signup API.
Then click on login button on Swagger page and use your user credential. 
```sh
http://127.0.0.1:8000/api/v1/swagger/
```

## Tests

To run the tests with virtual environment , `cd` into the directory where `manage.py` is:
```sh
(greenelyEnv)$ python manage.py test authentication
(greenelyEnv)$ python manage.py test consumption
```
And also you can run the test with Docker:

```sh
docker exec -it your_docker_container_id python manage.py test authentication
docker exec -it your_docker_container_id python manage.py test consumption
```

