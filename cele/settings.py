"""
Django settings for cele project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import site
import environ


# environ settings
env = environ.Env()

# modificar el path para que se puedan crear apps en subdirectorios
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), "apps"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

SECRET_KEY = env.str('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DJANGO_DEBUG = env.bool('DJANGO_DEBUG', default=False)

ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    # "admin_interface",
    # "colorfield",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'usuarios',
    'gestion_escolar',
    'edcon',
    'sistema',
    'smart_selects',
    'import_export',
    'pagos',
    'blog',
]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cele.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cele.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'mssql',
#         'HOST': os.environ.get('DB_HOST_EDCON'),
#         'NAME': os.environ.get('DB_NAME_EDCON'),
#         'USER': os.environ.get('DB_USER_EDCON'),
#         'PASSWORD': os.environ.get('DB_PASS_EDCON'),
#         'PORT': os.environ.get('DB_PORT_EDCON'),
#         'OPTIONS': {
#             'driver': 'FreeTDS',
#             'unicode_results': True,
#             'host_is_server': True,
#             'driver_supports_utf8': True,
#             'extra_params': 'tds_version=7.4',
#         }
#     },
#     'sito': {
#         'ENGINE': 'mssql',
#         'HOST': os.environ.get('DB_HOST_SITO'),
#         'NAME': os.environ.get('DB_NAME_SITO'),
#         'USER': os.environ.get('DB_USER_SITO'),
#         'PASSWORD': os.environ.get('DB_PASS_SITO'),
#         'PORT': os.environ.get('DB_PORT_SITO'),
#         'OPTIONS': {
#             'driver': 'FreeTDS',
#             'unicode_results': True,
#             'host_is_server': True,
#             'driver_supports_utf8': True,
#             'extra_params': 'tds_version=7.4',
#         }
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
# STATIC_ROOT = BASE_DIR / 'static_prod/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'usuarios.Usuario'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

USE_DJANGO_JQUERY = True

JAZZMIN_SETTINGS = {
    "site_title": 'Educación Continua',
    "site_header": 'Educación Continua',
    "site_brand": "Educación Continua",
    "site_logo": "images/logo-uts-10-aniversario.png",
    "welcome_sign": "Bienvenido a Educación Continua",
    "copyright": "Universidad Tecnológica de Salamanca",
    "order_with_respect_to": ["gestion_escolar", 'edcon', "usuarios", "sistema", "auth"],
    "show_ui_builder": True,
}

JAZZMIN_UI_TWEAKS = {
    "body_small_text": True,
    # "sidebar_nav_small_text": True,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

DATABASE_ROUTERS = ['routers.db_routers.AuthRouter',]

#SMTP OFFICE 365
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# SERVER_EMAIL = EMAIL_HOST_USER
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = env('EMAIL_USE_TLS')
# EMAIL_TIMEOUT = os.getenv("APP_EMAIL_TIMEOUT", 60)

#SMTP GMAIL
# EMAIL_BACKEND = env('EMAIL_BACKEND')
# EMAIL_HOST = env('EMAIL_HOST')
# EMAIL_USE_TLS = env('EMAIL_USE_TLS')
# EMAIL_PORT = env('EMAIL_PORT')
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')