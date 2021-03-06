import os
import sys
from pathlib import Path

from decouple import config, Csv
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG_PROPAGATE_EXCEPTIONS = config(
    'DEBUG_PROPAGATE_EXCEPTIONS',
    False,
    cast=bool,
)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'sorl.thumbnail',
    'thuawood.base',
    'thuawood.busts',
    'thuawood.guestbook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Important that this is last
    'thuawood.base.middleware.FSCacheMiddleware',
]

ROOT_URLCONF = 'thuawood.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'thuawood.busts.context_processors.busts',
            ],
        },
    },
]

WSGI_APPLICATION = 'thuawood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='postgresql://localhost/thuawood',
        cast=dj_database_url.parse
    ),
    'legacy': config(
        'LEGACY_DATABASE_URL',
        default='postgresql://localhost/thuawood_old',
        cast=dj_database_url.parse
    ),
}

CACHES = {
    'default': {
        'BACKEND': config(
            'CACHE_BACKEND',
            'django_redis.cache.RedisCache',
        ),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
        'LOCATION': config('CACHE_LOCATION', 'redis://127.0.0.1:6379/1'),
        'TIMEOUT': config('CACHE_TIMEOUT', 500),
        'KEY_PREFIX': config('CACHE_KEY_PREFIX', 'thuawood'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')
STATIC_ROOT = config(
    'STATIC_ROOT',
    default=os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))
)

PROJECT_TITLE = 'Thuas Trägubbar'

MEDIA_URL = config('MEDIA_URL', default='/media/')

LEGACY_MEDIA_ROOT = config('LEGACY_MEDIA_ROOT', './legacy-media-root')

MEDIA_ROOT = config(
    'MEDIA_ROOT',
    default=os.path.abspath(os.path.join(BASE_DIR, '..', 'media'))
)

FSCACHE_SECURE_SITE = config(
    'FSCACHE_SECURE_SITE',
    default=True,
    cast=bool,
)

FSCACHE_ROOT = config(
    'FSCACHE_ROOT',
    default=os.path.abspath(os.path.join(BASE_DIR, '..', '_FSCACHE'))
)
assert not FSCACHE_ROOT.endswith('/')

THUMBNAIL_DEBUG = config('THUMBNAIL_DEBUG', default=False, cast=bool)


import logging
from sorl.thumbnail.log import ThumbnailLogHandler

handler = ThumbnailLogHandler()
handler.setLevel(logging.ERROR)
logging.getLogger('sorl.thumbnail').addHandler(handler)


#HACK
logging.basicConfig(filename='/tmp/thuawood.log',
                   level=logging.DEBUG)

EMAIL_HOST = config('EMAIL_HOST', None)
EMAIL_PORT = config('EMAIL_PORT', None)
EMAIL_SUBJET_PREFIX = config('EMAIL_SUBJECT_PREFIX', '[Thuawood] ')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', None)

SERVER_EMAIL = config('SERVER_EMAIL', None) or EMAIL_HOST_USER
