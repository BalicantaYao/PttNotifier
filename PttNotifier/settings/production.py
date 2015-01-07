#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-09 23:18:19
# @Last Modified by:   bustta
# @Last Modified time: 2014-12-31 16:26:44
from .base import *

DEBUG = False
TEMPALTE_DEBUG = False

SECRET_KEY = get_env_var('PTTNOTIFIER_SECRET')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pttnotifier',
        'USER': get_env_var('PTTNOTIFIER_DB_DEFAULT_USER'),
        'PASSWORD': get_env_var('PTTNOTIFIER_DB_DEFAULT_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
