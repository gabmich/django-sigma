### DJANGO-SIGMA

## DESCRIPTION

Django-Sigma is a pre-configured Django project with Sigma JS 1.2.0 installed.

## GETTING STARTED
1. Download zip archive and unzip it.
2. Create a virtualenv in the django-sigma-master folder as follow :
```
cd django-sigma
python3 -m venv env
```
3. Activate virtualenv :
```
source env/bin/activate
```
4. Install dependencies :
```
pip install -r requirements.txt
```
5. Change directory to reach Django root dir :
```
cd django_sigma
```
6. Run Django migrations :
```
./manage.py migrate
```
7. Run dev web server :
```
./manage.py runserver
```
