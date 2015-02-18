#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-02-01 02:00:32
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-01 03:03:17
from agent.NotifyUtil.Mail import Mail


class Notification():
    def __init__(self, action, target, subject, content):
        super(Notification, self).__init__()
        self._target = target
        self._subject = subject
        self._content = content
        self._action = action

    def notify_user(self):
        if self._action == 'email':
            Mail(self._target, self._subject, self._content).send_mail()
        elif self._action == 'line':
            pass
        else:
            pass
