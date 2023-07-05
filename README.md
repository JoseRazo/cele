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
- Crear APP **`docker compose run web python manage.py startapp nombre_de_la_app`**
- Crear migraciones `docker compose run web python manage.py makemigrations`
- Ejecutar migraciones `docker compose run web python manage.py migrate`
- Eliminar migraciones solo en pruebas `find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
- Crear superusuario **`docker compose run web python manage.py createsuperuser`**

## Cambios en produccion
- Editar .env
```sh
DEBUG = FALSE
```
- Editar settings.py
> **Descomentar las siguientes lineas:**
```sh
#STATIC_ROOT = BASE_DIR / 'static_prod/'
```
- Editar cele/urls.py
> **Descomentar las siguientes lineas:**
```sh
# from django.urls import re_path
# from django.views.static import serve
#re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
```
> **Comentar las siguientes lineas:**
```sh
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
- Ejecutar `docker compose run web python manage.py collectstatic`

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8000](http://127.0.0.1:8000)
