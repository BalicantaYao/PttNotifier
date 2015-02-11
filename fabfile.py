# -*- coding:utf-8 -*-  

from fabric.api import run, local, roles, env, cd  
env.hosts=['128.199.232.167']

env.user="balicanta"
env.password="0975000354"
env.port=22

def pull():
    with cd('/home/balicanta/PttNotifier'):
        run('git pull')
