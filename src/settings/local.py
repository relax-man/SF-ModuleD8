from settings.base import *

SECRET_KEY = '12lufy*floh0boww30)kl#&l1)obq$9kp+$(7d$s!wcz5_2mc5'
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

LOCAL_APPS = ['livereload']

INSTALLED_APPS = LOCAL_APPS + INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211'
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'special': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(asctime)s] %(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'special'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        }
    }
}
