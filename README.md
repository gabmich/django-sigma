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
5. Change directory to reach Django project root dir :
```
cd django_sigma
```
6. Run Django migrations (if you don't modifiy 'settings.py', it will create a sqlite db) :
```
./manage.py migrate
```
7. Created a 'media' directory where you can put your data files (csv, xls, ods) (note : MEDIA_ROOT settings point to this folder)
```
mkdir media
```
8. Run dev web server :
```
./manage.py runserver
```
