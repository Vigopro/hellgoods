from .common import *


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIR, 'db.sqlite3'),
    }
}


INSTALLED_APPS += ()


try:
    from .local import *
except ImportError:
    pass
