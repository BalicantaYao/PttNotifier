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
    _template_html = None

    def __init__(self, mail_to, subject, content):
        super(Mail, self).__init__()
        self.mailgun_auth = ("api", os.environ['MAILGUN_KEY'])
        self.mail_data = {
            'from': self._mail_from,
            'to': mail_to,
            'subject': subject,
            'text': '',
            # 'text': content
        }
        if not Mail._template_html:
            import datetime
            logging.info("GetMailTemplate at {0}".format(datetime.datetime.now()))
            self._template_html = self._get_mail_template_html()

        full_content = ''
        if content:
            for item in content:
                full_content += self._get_content_block_html(item['topic'], item['author'], item['url'])
        context = self._template_html.replace('{notification_count}', str(len(content)))
        context = context.replace('{content_block}', full_content)
        self.mail_data['html'] = context

    def send_mail(self):
        logging.info("Send to Mailgun: {0} - {1}".format(
            str(self.mail_data['to']), str(self.mail_data['subject'])))
        return requests.post(
            self._mail_gun_sandbox,
            auth=self.mailgun_auth,
            data=self.mail_data
            )

    def _get_content_block_html(self, title, author, link):
        html = '''
        <tr style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        box-sizing: border-box; font-size: 14px; margin: 0;">
            <td class="content-block notifications" style="font-family: 'Helvetica Neue',
             Helvetica, Arial, sans-serif; box-sizing: border-box; font-size: 14px;
             vertical-align: top; margin: 0; padding: 0 0 20px;
             border-bottom: 1px solid #e5e5e5" valign="top">
                <span class="title" style="display: block; font-size: 32px;">{t}</span>
                <span class="author" style="display: block;">{a}</span>
                <span class="link" style="display: block;">{l}</span>
            </td>
        </tr>
        '''.format(t=title, a=author, l=link)
        return html

    def _get_mail_template_html(self):
        dir_path = os.path.dirname(__file__)
        file_path = os.path.join(dir_path, 'mail_template.html')
        f = open(file_path, 'r')
        return f.read()
