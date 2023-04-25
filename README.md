# Hall Of Memorial

----

## Цели проекта

Сохранение и предоставление информации о политических репрессиях при СССР


## Quickstart

__Установите Docker и docker-compose!__

+ Запустите проект

`docker-compose up`

+ Создайте супер-пользователя

`docker-compose exec web python manage.py createsuperuser`

По дефолту ваше приложение будет работать на 8000 порту

## Запуск без Docker

Установите poetry

Установите зависимости: 

`poetry install`

Запустите django приложение

`poetry run python manage.py runserver`







