# KeruKaffe

## Como instalar

0. `python3 -m venv venv`
1. `venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python manage.py migrate`

## Como rodar

1. `venv/bin/activate`
2. `python manage.py runserver`

## Caso faça alguma alteração em algum `models.py`

1. `python manage.py makemigrations`
2. `python manage.py migrate`
