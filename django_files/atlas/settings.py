# -*- coding: utf-8 -*-

import os

BASE_DIR = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ifrs9',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'painel-ifrs9-database',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'django_files/locale'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'html'),
)

STATIC_IMAGE_PATH = ''
STATIC_IMAGE = ''
YEAR_MIN_HS4 = 1995
YEAR_MAX_HS4 = 2013

SECRET_KEY = 'evertec-sinqia-atlas-risk-ifrs9'

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'redis:6379:0',
    },
}

HTTP_HOST = '/'
DB_PREFIX = ''

# FOR VERBOSE JS OUTPUT
DEV = True

DEBUG = True
TEMPLATE_DEBUG = DEBUG
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en'
SITE_ID = 1
USE_I18N = True
DEFAULT_CHARSET = "utf-8"
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "atlas.context_processors.supported_langs",
    "atlas.context_processors.settings_view",
)
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/media/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'atlas.middleware.PrerenderMiddleware'
)

ROOT_URLCONF = 'atlas.urls'
WSGI_APPLICATION = 'atlas.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'rest_framework_swagger',
    'observatory',
    'compressor'
)

ALLOWED_HOSTS = ['*']
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha',
    'SECURITY_DEFINITIONS': None,
}

VERSION = '1.0.8'

CACHE_VERY_SHORT = 60 * 10  # 10 minutes
CACHE_SHORT = 60 * 60  # 1 hour
CACHE_LONG = 60 * 60 * 24  # 1 day
CACHE_VERY_LONG = 60 * 60 * 24 * 7  # 1 week

COMPRESS_DEBUG_TOGGLE = "no_compress"

# Use localization
USE_L10N = True

try:
    from settings_local import *
except ImportError:
    pass
