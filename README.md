# openweathermap-django
This project uses openweathermap API for fetching the current weather details and compares them with our expected results.

## Used in project
* Python
* Django
* PostgreSQL

## Running the application
Note: You need to create database named 'openweathermap' in PostgreSQL. 
* Install the requirements using the following command
```
pip install requirements.txt
```
* Run the migrations to update all db changes
```
python manage.py migrate
```
* Now you need to run following command for running the server
```
python manage.py runserver --noreload
```
Note: --noreload parameter is used because the application is using APScheduler and there is a job scheduled so --noreload prevents the job to be executed twice at the same time.
* You can now test the API endpoints using Postman
## Running tests
You can run unittests by using following command:
```
python manage.py test
```
