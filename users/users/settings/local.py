from .base import *

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'UserAuthentication',
        'USER': 'root_arturo',
        'PASSWORD': 'arturo_root',
        #'HOST':'0.0.0.0',
        'HOST': '127.0.0.1',
        'PORT': '3306'
        #'PORT': '3306'
    }
}




STATIC_URL = 'static/'
