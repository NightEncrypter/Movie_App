"""
Django settings for realestate_app project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# #Authentication backends
# AUTHENTICATION_BACKENDS = (
#         'django.contrib.auth.backends.ModelBackend',
#     )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r$de+6xn_2ldxtv568qv2+y20(k3+^udj^mt*_^q@numb5^vl#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False

ALLOWED_HOSTS = ["themoviemaniac.herokuapp.com","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "pages.apps.PagesConfig",
    "reviews.apps.ReviewsConfig",
    "casts.apps.CastsConfig",
    "accounts.apps.AccountsConfig",
    "watchlists.apps.WatchlistsConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'realestate_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'realestate_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


# #! With Postgres 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'moviedb',
        
#         "USER":"postgres",
#         "PASSWORD":"manas123",
#          "HOST":"localhost"
#     }
# }

import urllib 

# ! With MongoDb
DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'movie_app',
            'CLIENT': {
                # 'host':  "mongodb+srv://manas:manas12345@moviemaniac.icnap.mongodb.net/moviemaniac_app?retryWrites=true&w=majority",
                "authMechanism":'SCRAM-SHA-1',
                # "host":'mongodb+srv://Abhishek:'+ urllib.parse.quote('abhi@8223') +'@portfolio-cluster.esifa.mongodb.net/another-db?retryWrites=true&w=majority'
                "host":"mongodb+srv://manas:manas123@cluster0.ylvco.mongodb.net/movie_app?retryWrites=true&w=majority"
                
            }  
        }
}

 
# mongodb+srv://manasrathore2342:<password>@moviemaniac.icnap.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

# ? INITIALLY SETUP
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# For production purpose
# ? wehen you deploy your application you run a command ( python manage.py collectstatic ) collectstatic and it will go all of your application takes all stattic file and put into root static folder
STATIC_ROOT = os.path.join(BASE_DIR, "static")


# LOCATION OF STATIC DIR
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "node_modules/feather-icons"),
    
    os.path.join(BASE_DIR, "realestate_app/static"),
    os.path.join(BASE_DIR, "styles"),
]


# Media folder setting => to store a image 
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

MEDIA_URL="/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# FOR ALERTS MESSAGES
from django.contrib.messages import constants as messages

MESSAGE_TAGS={
    messages.ERROR:'danger',
    messages.SUCCESS:'success'
}



# EMAIL CONFIG
EMAIL_HOST= "smtp.gmail.com"
EMAIL_PORT= 587
EMAIL_HOST_USER= 'manasrathore2342@gmail.com'
EMAIL_HOST_PASSWORD = "manas2342@"
EMAIL_USE_TLS= True