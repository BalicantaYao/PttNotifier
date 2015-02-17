#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-22 23:32:19
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-01 02:47:13
import os
import requests
from LogUtil.LogUtil import LogUtil


class Mail():
    _mail_gun_sandbox = "https://api.mailgun.net/v2/sandbox3973be0c4dc3412f853adf1f3d669499.mailgun.org/messages"
    _mail_from = "PTTNotifier <postmaster@sandbox3973be0c4dc3412f853adf1f3d669499.mailgun.org>"

    def __init__(self, mail_to, subject, content):
        super(Mail, self).__init__()
        self.mailgun_auth = ("api", os.environ['MAILGUN_KEY'])
        self.mail_data = {
            'from': self._mail_from,
            'to': mail_to,
            'subject': subject,
            'text': content
        }
        self.logging = LogUtil()

    def send_mail(self):
        self.logging.logger("Send to Mailgun: {0} - {1}".format(
            str(self.mail_data['to']), str(self.mail_data['subject'])))
        return requests.post(
            self._mail_gun_sandbox,
            auth=self.mailgun_auth,
            data=self.mail_data
            )
