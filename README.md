# cele

Sistema de Gestón de Cursos de Educación Continua de Universidad TEcnológica de Salamanca.

## Pre-requisitos

- Instalar [Docker.](https://www.docker.com/get-started)
- Instalar [Docker Compose.](https://docs.docker.com/compose/install/)

## Instalación

- Clonar repositorio `git clone https://github.com/JoseRazo/cele.git`
- Abrir proyecto con editor de codigo y configurar archivo **`.env`**
- Abrir terminal y entrar a la carpeta del proyecto `~/dev/django/cele$`
- Generar imagen docker y contenedores con **`docker-compose build`** y **`docker-compose up -d`**
- Crear migraciones `docker compose run web python manage.py makemigrations`
- Ejecutar migraciones `docker compose run web python manage.py migrate`
- Crear superusuario **`docker compose run web python manage.py createsuperuser`**

## Cambios en produccion
- Editar .env DEBUG = FALSE
- Editar settings.py y agregar STATIC_ROOT = BASE_DIR / 'static_prod/'
- Ejecutar `docker compose run web python manage.py collectstatic`

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8888](http://127.0.0.1:8080)
