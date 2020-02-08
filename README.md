# FlaskSqlAlchemy
 Repositorio de ejemplo de uso Flask y SQLAlchemy

## Necesario

- python3
- python venv
- pip3
- flask
- flask-sqlalchemy
- marshmallow-sqlalchemy
- mysql-connector
- termcolor

## Instalar dependencias

## PIP para Python 3

``
sudo apt install python3-pip
``

## Instalar virtualenv en ubuntu

``
sudo apt-get install python-virtualenv
``

## Configurar Activar módulo de env

``
python -m virtualenv venv
``

## Activar ambiente

``
. venv/bin/activate
``

### Flask

`` 
pip install flask 
``

### DB

``
pip install mysql-connector
``


### Sqlalchemy y Marshmallow

``
pip install flask-sqlalchemy
``

``
pip install -U flask-sqlalchemy marshmallow-sqlalchemy
``

``
pip install flask-marshmallow
``

### Listar dependencias instaladas

`` pip list ``

## Ejecutar

``
python src/app.py
``

## Servidor de prueba

Ejecutar en la CLI

### Setear variables de entorno en la CLI

```
export FLASK_APP=app.py
export FLASK_ENV=development
```

### Opción 1

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Opción 2

```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host localhost --port 3000
```

```
FLASK_APP=app.py FLASK_ENV=development flask run --host localhost --port 3000
```

```
flask run
```


## Utilidades

``
pip install termcolor
``

### PIP

Instalar y guardar
``pip install package && pip freeze > requirements.txt``

Guardar package usados

``pip freeze > requirements.txt``

Instalar packages usados
``pip install -r requirements.txt``

## Esquema ER

![ER](docs\ER.png)