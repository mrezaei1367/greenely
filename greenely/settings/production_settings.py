from .default_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_data',
        'USER': 'dbuser',
        'PASSWORD': 'dbpass',
        'HOST':
        'prod_db_ip',  # Or an IP Address that your DB is hosted on production
        'PORT': '3306',
    }
}
