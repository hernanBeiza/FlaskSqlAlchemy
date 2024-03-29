# FlaskSqlAlchemy

 Repositorio de ejemplo de uso Flask y SQLAlchemy

## Requerimiento

### Ambiente

- Python 3.8
- pip 3

### Dependencias

- Click==8.1.3
- Flask==2.3.0
- Flask-DotEnv==0.1.2
- flask-marshmallow==0.10.1
- Flask-SQLAlchemy==2.5.1
- itsdangerous==2.1.2
- Jinja2==3.1.2
- MarkupSafe==2.1.1
- marshmallow==3.0.0
- marshmallow-sqlalchemy==0.21.0
- mysql-connector-python==8.0.30
- six==1.14.0
- SQLAlchemy==1.3.13
- termcolor==1.1.0
- virtualenv==20.16.5
- Werkzeug==2.3.0

## Infraestructura de prueba

### Requerimientos

- Linux Ubuntu
- docker
- mysql 8.0.30

### Instalación

#### mysql

- Bajar imagen

```bash
docker pull mysql:8.0.30
```

- Crear contenedor

```bash
docker run --name tareas-mysql -e MYSQL_ROOT_PASSWORD=mypass123 -d -p 3306:3306  mysql:8.0.30
```

- Conectar usando 3306

- Si el contenedor ya está creado, levantar ejecutando

```bash
docker start tareas-mysql
```

#### phpmyadmin

- Bajar imagen

```bash
docker pull phpmyadmin/phpmyadmin:latest
```

- Crear contenedor

```bash
docker run --name tareas-phpmyadmin -d --link tareas-mysql:db -p 8081:80 phpmyadmin/phpmyadmin
```

- Si el contenedor ya está creado, levantar ejecutando

```bash
docker start denuncias-phpmyadmin
```

- Entrar a [phpMyAdmin](http://localhost:8081)
- Usuario: root
- Contraseña: mypass123

### Comandos útiles Docker

- Listar contenedores

```bash
docker ps -a
```

- Entrar via SSH

```bash
docker exec -it <id contenedor> /bin/bash
```

## Desarrollo

### Configuración de ambiente de desarrollo

- Instalar virtualenv usando pip3

```bash
pip3 install virtualenv
```

- Activar módulo de env en Python

```bash
python3 -m virtualenv venv
```

### Activar ambiente

```bash
. venv/bin/activate
```

### Instalación de dependencias

```bash
pip3 install -r requirements.txt
```

## Configuracióñ de servidor de prueba

- Setear variables de entorno en la CLI, teniendo en cuenta la uybicación del archivo app.py

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
```

### Opción 1

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

### Opción 2

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run --host localhost --port 3000
```

- Todo en una línea

```bash
FLASK_APP=src/run.py FLASK_ENV=development flask run --host localhost --port 3000 --debug
```

## Comandos útiles PIP

- Instalar y guardar

```bash
pip install package && pip freeze > requirements.txt
```

- Guardar package usados

```bash
pip freeze > requirements.txt
```

- Instalar packages guardados en requirements.txt

```bash
pip install -r requirements.txt
```

## Modelo de datos

### Esquema ER

![ER](docs\ER.png)