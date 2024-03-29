# Yatube API

## Автор
[Ермолов Иван](https://ErmolovIvan/YaTube_API)

## Описание
Yatube API позволяет через простые запросы обращаться к Yatube для получения и отправления информации.

## Технологии
- Python 3.7
- Django 3.2.16
- Django REST Framework 3.12.4
- Djoser 2.1.0

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/ErmolovIvan/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
