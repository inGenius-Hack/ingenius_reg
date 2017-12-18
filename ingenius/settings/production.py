import os

from ingenius.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

ALLOWED_HOSTS += [os.environ['DJANGO_HOST_NAME']]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DBNAME'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'],
        'HOST': 'localhost',
        'PORT': ''
    }
}


STATIC_ROOT = os.environ['STATIC_ROOT']
