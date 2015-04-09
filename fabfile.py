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
        run('''
            . {0}/venv/pttnotifier/bin/activate &&
            python manage.py collectstatic --noinput &&
            pip install -r requirements.txt &&
            python manage.py makemigrations &&
            python manage.py migrate
            '''.format(path))


def restartGunicorn():
    with cd(PROJECT_PATH):
        run('supervisorctl restart gunicorn')


def restartCeleryd():
    sudo('service celeryd restart')


def restartCeleryBeat():
    sudo('service celerybeat restart')


def build_nodejs_env():
    with cd(PROJECT_PATH + '/websocket'):
        run('npm install')


def restart_ws_server():
    with cd(PROJECT_PATH):
        run('supervisorctl restart ws_server')
