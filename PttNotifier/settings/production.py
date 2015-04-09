#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-09 23:18:19
# @Last Modified by:   bustta
# @Last Modified time: 2014-12-31 16:26:44
from .base import *
import os

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
SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_UNIX_DOMAIN_SOCKET_PATH = '/var/run/redis/redis.sock'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PREFIX = 'session'

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
logging.debug("STATIC_ROOT: {0}".format(STATIC_ROOT))
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
