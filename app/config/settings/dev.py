from .base import *

WSGI_APPLICATION = 'config.wsgi.dev.application'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': secrets['DEV_DB_NAME'],
        'USER': secrets['DEV_DB_USER'],
        'PASSWORD': secrets['DEV_DB_PASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
