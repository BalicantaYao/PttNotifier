#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-25 22:01:35
# @Last Modified by:   bustta
# @Last Modified time: 2015-01-26 23:09:28
from bs4 import BeautifulSoup
from ...models import BoardScanning
import requests
import re
import logging


class BaseAgent():

    def __init__(self, board_name):
        self.target = board_name
        self.url = 'https://www.ptt.cc/bbs/{0}/index.html'.format(board_name)
        self.ptt_site = 'https://www.ptt.cc'
        self.is_first_exe = True
        try:
            self.last_scan_page_number = BoardScanning.objects.filter(
                board_name=board_name).order_by('-page_number_of_last_scan').first().page_number_of_last_scan
        except BoardScanning.DoesNotExist:
            self.last_scan_page_number = 0
        self.pre_page = 0
        self.entry_list = []

    def _get_soup_object(self, target_url):
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        requests.packages.urllib3.disable_warnings()
        context = requests.get(target_url, headers=headers, verify=False).text
        if context:
            return BeautifulSoup(context)
        else:
            return None

    def _get_page_code(self, url):
        p = re.compile('\d+')
        code = p.findall(url)
        if len(code) > 0:
            return int(code[0])
        return 0

    def get_entries_after_last_fetch(self):

        if self.entry_list:
            return self.entry_list

        this_page_number = -1
        entry_list = []
        logging.debug("GetEntryStart:")
        scan_count = 0
        scanned_page_numbers = []
        while this_page_number != self.last_scan_page_number:

            soup = self._get_soup_object(self.url)
            if not soup:
                return

            # Never Scan the board
            if(self.last_scan_page_number == 0):
                break

            pre_page_url = self.ptt_site + soup.select('.wide')[1]['href']
            self.url = pre_page_url
            self.pre_page = self._get_page_code(pre_page_url)
            this_page_number = self.pre_page + 1

            scan_count += 1
            if len(soup.select('.wide')) <= 0:   # html structure change or HTTPError
                return entry_list

            logging.info("LastScan: {0}; This page: {1}".format(self.last_scan_page_number, this_page_number))
            scanned_page_numbers.append(this_page_number)

            entries = soup.select('.r-ent')

            for item in entries:
                if len(item.select('.title > a')) <= 0:
                    continue

                title = item.select('.title > a')[0].text
                link = self.ptt_site + item.select('.title > a')[0]['href']
                author = item.select('.meta > .author')[0].text
                date = item.select('.meta > .date')[0].text
                entry_list.append({'topic': title, 'url': link, 'author': author, 'date': date})

        self.entry_list = entry_list
        BoardScanning.objects.create(board_name=self.target,
                                     page_number_of_last_scan=max(scanned_page_numbers)-1,
                                     last_scan_pages_count=scan_count)
        return entry_list
