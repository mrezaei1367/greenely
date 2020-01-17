from .default_settings import *

from .default_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'test_data.db'),
    }
}

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test_data',
#         'USER': 'dbuser',
#         'PASSWORD': 'dbpass',
#         'HOST':
#         'prod_db_ip',  # Or an IP Address that your DB is hosted on production
#         'PORT': '3306',
#     }
# }
