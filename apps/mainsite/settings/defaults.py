"""
Default Django settings for the project.
"""

import os
import sys
from mainsite import TOP_DIR

from .fragments import load_settings_fragment
settings_fragment = lambda f: globals().update(load_settings_fragment(f))



###
#
# Miscellaneous
#
###

SITE_ID = 1

ROOT_URLCONF = 'mainsite.urls'

WSGI_APPLICATION = 'mainsite.wsgi.application'


###
#
# Internationalization / Localization
#
###

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###
#
# Static files
#
###

STATIC_ROOT = os.path.join(TOP_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(TOP_DIR, 'breakdown', 'static'),
]

settings_fragment('static')


###
#
# Media Files
#
###

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(TOP_DIR, 'mediafiles')
ADMIN_MEDIA_PREFIX = STATIC_URL+'admin/'



##
#
#   Fixtures
#
##

FIXTURE_DIRS = [
    os.path.join(TOP_DIR, 'fixtures'),
]


###
#
# Installed Apps
#
###

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)


###
#
# Middleware
#
###

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'mainsite.middleware.TrailingSlashMiddleware',
)
APPEND_SLASH = False


### 
#
# Templates
#
###

TEMPLATES = [
    # Jinja2 Teplates: ./breakdown/templates/jinja/*
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            os.path.join(TOP_DIR, 'breakdown', 'jinja2'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'mainsite.template.jinja2_environment',
        },
    },

    # Django Templates: ./breakdown/templates/django/*
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(TOP_DIR, 'breakdown', 'templates'),
        ],
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



