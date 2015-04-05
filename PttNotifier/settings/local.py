#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2014-12-09 23:18:11
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-08 00:17:29

from .base import *
import os

SECRET_KEY = get_env_var('LOCAL_SECRET')

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

BROKER_URL = 'django://'
