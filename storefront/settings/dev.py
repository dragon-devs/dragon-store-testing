from .comman import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-obkpqm_zxou#4l0v8)k!ecd0e$2o56vep(rqyw+5qj*#=5#&ju'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'USER': 'root',
        'PASSWORD': 'MyPassword',
        'HOST': 'mysql',    
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@dragondevs.com'

DEBUG_TOOBAR_CONFIG = {
    'SHOW_TOOBAR_CALLBACK': lambda request:True,
}