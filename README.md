# Food Reservation System

a simple food reservation system with python language using django rest framework.

## Setup To Run

first install requirements;

```bash
pip install -r requirements.txt
```

then run the program in you desired port for example 8000

```bash
python manage.py runserver 8000
```

### Test APIs

* To register new user, send a post request with username, password, password2, email, first_name and last_name to below address: 
(notice that username and email must be unique.)

```
http://localhost:8000/auth/register/
```

* To login send a post request with username and password:
```
http://localhost:8000/auth/login/
```

* also its possible to see list of menus and orders by sending your token:
```
http://localhost:8000/auth/menus/
http://localhost:8000/auth/orders/
```
