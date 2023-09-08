# Проект Api_final_yatube 
## Описание 
Проект взаимодействия API для программы social_network(yatube) выполненный в DRF  
## Установка
Как запустить проект:  
Клонировать репозиторий и перейти в него в командной строке:  

> git clone https://github.com/yandex-praktikum/api_final_yatube.git  

> cd api_final_yatube/

Cоздать и активировать виртуальное окружение:

> python3 -m venv venv
> 
> source venv/bin/activate
> 
Установить зависимости из файла requirements.txt:

> python3 -m pip install --upgrade pip
> 
> pip install -r requirements.txt

Выполнить миграции:

>python3 manage.py migrate

Запустить проект:

>python3 manage.py runserver
