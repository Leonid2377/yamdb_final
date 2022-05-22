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

> остановить проект: `docker-compose down -v`

**проект работает по адресу 84.201.179.254**

**Автор проекта: Старостин Леонид** 