# Приложение бронирования комнат в отеле на Django с использованием базы данных Postgresql

## Активация вертуального окружения
```sh
python -m venv venv
```
```sh
source venv/Scripts/activate
```
## Для работы приложения нужно установить:

requests 2.26.0
Django 4.1.1
django-filter 22.1
django-templated-mail 1.1.1
djangorestframework 3.14.0
psycopg2 2.9.3
``` sh
pip install -r requirements.txt
```

## Настройка БД 


- Установить Postgresql
- Создать новую БД 
- В файле settings.py описать все связи с БД
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database',
        'USER': 'databaseuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

## Запуск проекта
Используйте команду python manage.py runserver для запуска сервера.
```sh 
python manage.py runserver
```