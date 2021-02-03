# Memcached Django

### Инструкция для локального запуска:

1. Клонировать репозиторий командой:
    ```
    git clone https://github.com/relax-man/SF-ModuleD8.git
    ```

2. Создать файл src/settings/local.py с содержимым:
    ```
    from settings.base import *

    SECRET_KEY = *YOUR_SECRET_KEY*
    DEBUG = True

    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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
    ```

3. Провести все миграции
    ```
    python src/manage.py migrate
    ```

4. Загрузить данные из фикстур для тестирования
    ```
    python src/manage.py loaddata src/fixtures/auth.json
    python src/manage.py loaddata src/fixtures/todolist.json
    ```

5. Запустить проект локально
    ```
    python src/manage.py runserver
    ```

### Дополнительно

Для просмотра To-Do List необходима авторизация через admin-панель. Имя пользователя
и пароль указаны в условии задания.