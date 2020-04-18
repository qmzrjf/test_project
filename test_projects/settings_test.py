from test_projects.settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

CELERY_ALWAYS_EAGER = CELERY_TASK_ALWAYS_EAGER = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
