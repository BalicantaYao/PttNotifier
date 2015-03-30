#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-22 23:32:19
# @Last Modified by:   bustta
# @Last Modified time: 2015-03-30 21:40:23
import os
import requests
import logging


class Mail():
    _mail_gun_sandbox = "https://api.mailgun.net/v3/buzz3.co/messages"
    _mail_from = "Buzz3 <postmaster@buzz3.co>"

    def __init__(self, mail_to, subject, content):
        super(Mail, self).__init__()
        self.mailgun_auth = ("api", os.environ['MAILGUN_KEY'])
        self.mail_data = {
            'from': self._mail_from,
            'to': mail_to,
            'subject': subject,
            'text': content
        }

    def send_mail(self):
        logging.info("Send to Mailgun: {0} - {1}".format(
            str(self.mail_data['to']), str(self.mail_data['subject'])))
        return requests.post(
            self._mail_gun_sandbox,
            auth=self.mailgun_auth,
            data=self.mail_data
            )
