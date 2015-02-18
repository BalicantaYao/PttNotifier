#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-25 22:01:35
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-26 23:09:28
from bs4 import BeautifulSoup
import requests
import re
from Util import Util


class BaseAgent():

    def __init__(self, target):
        self.target = target
        self.url = 'https://www.ptt.cc/bbs/{0}/index.html'.format(target)
        self.ptt_site = 'https://www.ptt.cc'
        self.last_scan_page_number = 0
        self.is_first_exe = True
        self.pre_page = 0
        self.util = Util()

    def _get_soup_object(self, target_url):
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        requests.packages.urllib3.disable_warnings()
        return BeautifulSoup(requests.get(target_url, headers=headers, verify=False).text)

    def _get_page_code(self, url):
        p = re.compile('\d+')
        code = p.findall(url)
        if len(code) > 0:
            return int(code[0])
        return 0

    def get_entries_after_last_fetch(self):
        this_page_number = -1
        entry_list = []
        self.util.logger("GetEntryStart:")
        while this_page_number != self.last_scan_page_number:
            soup = self._get_soup_object(self.url)
            if len(soup.select('.wide')) <= 0:   # html structure change or HTTPError
                return entry_list

            pre_page_url = self.ptt_site + soup.select('.wide')[1]['href']
            # self.url = pre_page_url
            self.pre_page = self._get_page_code(pre_page_url)
            this_page_number = self.pre_page + 1
            self.util.logger("LastScan: {0}; This page: {1}".format(
                self.last_scan_page_number, this_page_number)
            )

            if self.is_first_exe:
                self.last_scan_page_number = this_page_number
                self.is_first_exe = False

            entries = soup.select('.r-ent')

            for item in entries:
                if len(item.select('.title > a')) <= 0:
                    continue

                title = item.select('.title > a')[0].text
                link = self.ptt_site + item.select('.title > a')[0]['href']
                author = item.select('.meta > .author')[0].text
                date = item.select('.meta > .date')[0].text
                entry_list.append({'topic': title, 'url': link, 'author': author, 'date': date})

        self.last_scan_page_number = this_page_number

        return entry_list
