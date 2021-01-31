from settings.base import *

import dj_database_url
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

def get_cache():
    environment_ready = all(
        os.environ.get(f'MEMCACHIER_{key}', False)
        for key in ['SERVERS', 'USERNAME', 'PASSWORD']
    )
    if not environment_ready:
        cache = {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
    else:
        servers = os.environ['MEMCACHIER_SERVERS']
        username = os.environ['MEMCACHIER_USERNAME']
        password = os.environ['MEMCACHIER_PASSWORD']
        cache = {
            'default': {
                'BACKEND': 'django_bmemcached.memcached.BMemcached',
                'TIMEOUT': None,
                'LOCATION': servers,
                'OPTIONS': {
                    'username': username,
                    'password': password,
                }
            }
        }
    return {'default': cache}


CACHES = get_cache()
