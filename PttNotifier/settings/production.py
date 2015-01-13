#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-09 23:18:19
# @Last Modified by:   bustta
# @Last Modified time: 2014-12-30 16:35:13
from .base import *
import os

DEBUG = False
TEMPALTE_DEBUG = False

#SECRET_KEY = get_env_var('PTTNOTIFIER_SECRET')
SECRET_KEY = 'upv&_lu&5zk)3q-*(wu0*583!10q6tf2m3$91&m#t0t3j!g==q'

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
logging.debug("STATIC_ROOT: {0}".format(STATIC_ROOT))
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
