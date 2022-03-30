# maps.312
***
### ENG information.
The project has two functions:
1. Puts a marker on the map and writes the coordinates to 
the database (PostgreSQL). Address: http://127.0.0.1:8000/maps/

2. Displays a general list with all coordinates from the database. 
Address: http://127.0.0.1:8000/maps/views/

A pre-installed PostgreSQL database is required.

In the settings.py file, you need to change the data for connecting to the database.

> 'NAME': 'NAME_DATABASE',
* The name of your PostgreSQL database. For example 'New_DB'.
> 'USER': 'USER_BASE',
* Account in the database. For example 'admin'.
> 'PASSWORD': 'PASSWORD_USER',
* Account password. For example, 'qwerty'.
> 'HOST': 'HOST_BASE',
* Database server. For example, 'localhost' or '127.0.0.1'.
> 'PORT': 'PORT',
* Available or configured connection port. For example '5432'.

***
### RUS information.

У проекта две функции:
1. Ставит маркер на карту и записывает координаты 
в базу данных (PostgreSQL). Адрес: http://127.0.0.1:8000/maps/

2. Отображает общий список со всеми координатами из базы данных.
Адрес: http://127.0.0.1:8000/maps/views/

Необходима предустановленная база PostgreSQL.

В файле settings.py необходимо изменить данные для подключения к базе данных
> 'NAME': 'NAME_DATABASE',
* Наименование вашей базы PostgreSQL. Например 'NewDB'
> 'USER': 'USER_BASE',
* Учетная запись в базе данных. Например 'admin'
> 'PASSWORD': 'PASSWORD_USER',
* Пароль от учетной записи. Например 'qwerty'
> 'HOST': 'HOST_BASE',
* Используемый сервер. Напиример 'localhost' или '127.0.0.1'
> 'PORT': 'PORT',
* Доступный или используемый порт подключения. Например '5432'
