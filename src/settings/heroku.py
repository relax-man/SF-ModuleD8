from settings.base import *

import dj_database_url
import django_heroku
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

django_heroku.settings(locals())

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'TIMEOUT': None,
        'LOCATION': os.environ['MEMCACHIER_SERVERS'],
        'OPTIONS': {
            'username': os.environ['MEMCACHIER_USERNAME'],
            'password': os.environ['MEMCACHIER_PASSWORD'],
        }
    }
}
