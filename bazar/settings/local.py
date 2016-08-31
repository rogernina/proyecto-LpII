from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('db.sqlite3'),
        #os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



STATIC_URL = '/static/'