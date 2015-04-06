# -*- coding:utf-8 -*-

import os
from fabric.api import run, env, cd, sudo
env.hosts = ['128.199.232.167']

env.user = os.environ['PRODUCTION_USER_NAME']
env.password = os.environ['PRODUCTION_PASSWORD']
env.port = 22

PROJECT_PATH = '/var/www/webApps/PttNotifier'
path = '/var/www/webApps'


def pull():
    with cd(PROJECT_PATH):
        run('git pull')


def restartNginx():
    sudo('service nginx restart')


def collectStatic():
    with cd(PROJECT_PATH):
        run('. %s/venv/pttnotifier/bin/activate && python manage.py collectstatic --noinput ' % path)
        run('pip install -r requirements.txt')
        run('python manage.py makemigrations')
        run('python manage.py migrate')


def restartGunicorn():
    with cd(PROJECT_PATH):
        run('supervisorctl reload')


def restartCeleryd():
    sudo('service celeryd restart')


def restartCeleryBeat():
    sudo('service celerybeat restart')
