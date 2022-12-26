from .comman import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-obkpqm_zxou#4l0v8)k!ecd0e$2o56vep(rqyw+5qj*#=5#&ju'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefrontwsl3',
        'USER': 'root',
        'PASSWORD': 'Brucelee28',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    
    }
}