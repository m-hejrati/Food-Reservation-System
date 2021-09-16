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

* To register new user, send a POST request with username, password, password2, email, first_name and last_name to below address: 
(notice that username and email must be unique.)

```
http://localhost:8000/auth/register/
```

* To login send a POST request with username and password:
```
http://localhost:8000/auth/login/
```

* If you forget your password, you can reset it by sending an email to the following address:
```
http://localhost:8000/auth/password_reset/
```
then enter the received token and a new password:
```
http://localhost:8000/auth/password_reset/confirm/
```

After logging, admin can use the following APIs:

* Add a new menu with sending a POST request consist of food_name, date and amount:
```
http://localhost:8000/menus
```

* Remove a menu with sending a DELETE request and id:
```
http://localhost:8000/menus/id
```

* Edit a menu with sending a PUT request and id, and also food_name, date and amount as body:
```
http://localhost:8000/menus/id
```

* Show list of all menus and user that reserved them by sending a GET request:
```
http://localhost:8000/menus
```

* Reserve an order by sending POST request and your user_id, menu_id as body (Admin can order for other users):
```
http://localhost:8000/orders/add/
```

* Remove an order by sending POST request and your user_id, menu_id as body (Admin can order for other users):
```
http://localhost:8000/orders/delete/
```
