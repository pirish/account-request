# Account Request

Django application to collect information and create user accounts for various services.

## Getting started

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --username admin

python manage.py runserver

## Using

Rest endpoints available at 

/acct/reqs/
/acct/types/

examples:
http -j -a 'admin:password' http://127.0.0.1:8000/acct/reqs/

or 

curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/acct/reqs/


