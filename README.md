# Account Request

Django application to collect information and create user accounts for various services.

## Getting started
Install dependencies
```
pip install -r requirements.txt
```

Prepare database
```
python manage.py makemigrations
python manage.py migrate
```

Create priveleged user
```
python manage.py createsuperuser --username admin
```

Run development server
```
python manage.py runserver
```

## Using

Rest endpoints available at 
```
/acct/reqs/
/acct/types/
```
examples:
```
http -j -a 'admin:password' http://127.0.0.1:8000/acct/reqs/
```
or 

```
curl -H 'Accept: application/json; indent=4' -u admin:password http://127.0.0.1:8000/acct/reqs/
```
![Python package](https://github.com/pirish/account-request/workflows/Python%20package/badge.svg)
