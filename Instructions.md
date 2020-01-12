# Running Time Environmnet and Installation Instructions

## Operating System and Hardware

### Operating System

    Project has been tested on the Windows 10. It should be easy to setup on Linux as well.

## Python and Django

### Python version 3.7+ is required 

    Python --version

### Pipenv or other virtual environment tool must be installed,
    pip install pipenv

## Make sure your install git or the other same tools, clone the repository from

    git clone  https://github.com/sethfengli/hivery-backend-challenge.git
    cd {Path}/hivery-backend=challenge/

## Setup virtual environment, depended package and 
    
### Change the current folder to your download  repository folder   
    cd {Path}/hivery-backend=challenge/

### If your current python version is lower than 3.7 and you can't change it, you can install python 3.7 in the virtual environment.
    
    pipenv shell
    pipenv --python 3.7

### You can copy the following instructions to a bacth file or paster directly to CLI or CMD 

    pipenv shell
    pipenv install -r requirements.txt

    django-admin.py startproject paranuara .
    python manage.py startapp colony

    python manage.py makemigrations colony
    python manage.py migrate

    python manage.py runscript import_data
   
## Create admin user
    python manage.py createsuperuser

## Start the server 
   
    python manage.py runserver

##  Test APIs

### Swagger UI
    
    Recommend to use Swagger UI 

    http://127.0.0.1:8000/openapi/#/

### API URLs

- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

    ​URL Pattern:   /employees/{company_id}/  
    example:        http://127.0.0.1:8000/employees/3/

- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.

    ​URL Pattern:   /commonfriends/{person1_index}/{person2_index}/{eyeColor}/{has_died}/  
    example:        http://127.0.0.1:8000/commonfriends/3/2/brown/0/

- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": 

    ​URL Pattern:   /favouritefood​/{person_index}​/  
    example:        http://127.0.0.1:8000/favouritefood​/1/

### Django Admin http://127.0.0.1:8000/Admin

    Provided the data create, update, delete and import functions

#### Remove the database and import different raw data files from resources folder

    cd {Path}/hivery-backend=challenge/
    pipenv shell   
    del db.sqlite3
    cd colony
    del migrations /S /Q
    cd ..
    python manage.py makemigrations colony
    python manage.py migrate
    python manage.py runscript import_data
    python manage.py runserver

## Visual Studio Code 

    Visual Stadio Code is not mandatory, but it provides a lot of tools for our development.  

    The latest version has integraded Jupyter Notebook which is common tool to Data Scientists and developers. 

#### [data_study_ipynb](https://github.com/sethfengli/hivery-backend-challenge/blob/master/data_study.ipynb) is an example how it could help us study the raw data here.  




