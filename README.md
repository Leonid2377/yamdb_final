![example workflow](https://github.com/Leonid2377/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# yamdb_final
#Описание проекта
Проект позволяет зарегистрироваться пользователям
и оставлять отзывы на различные произведения

**Как пользоватся**:
>Скопировать проект командой: 
>> `git clone`

>Установить и активировать виртуальное окружение
>>`python3 -m venv env`
> 
>>`source env/bin/activate`
> 
>>`python3 -m pip install --upgrade pip`
 
>Установить зависимости:
>> `pip install -r api_yamdb/requirements.txt`


>Запустить из директории infra:
>> `docker-compose up -d --build`
>
>>`docker-compose exec web python manage.py migrate`
> 
>>`docker-compose exec web python manage.py createsuperuser`
>
>>`docker-compose exec web python manage.py collectstatic --no-input`

 
>Создать файл .env из директории infra/ и внестите в него данные:
>
>>`DB_ENGINE=django.db.backends.postgresql`
>
>>`DB_NAME=postgres`
>
>>`POSTGRES_USER=postgres`
>
>>`POSTGRES_PASSWORD= # установите свой пароль`
>
>>`DB_HOST=db`
>
>>`DB_PORT=5432`

> остановить проект: `docker-compose down -v`

*зайти можно по адресу http://130.193.34.248/redoc/ , http://130.193.34.248/admin/**

**Автор проекта: Старостин Леонид** 
