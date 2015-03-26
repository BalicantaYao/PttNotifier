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

    PTT_PREFIX = 'https://www.ptt.cc'
    URL_CONTAIN_PAGE_NUMBER = 'https://www.ptt.cc/bbs/{0}/index{1}.html'
    INDEX_URL = 'https://www.ptt.cc/bbs/{0}/index.html'

    def __init__(self, board_name):
        self.target = board_name
        self.url = self.INDEX_URL.format(board_name)
        self.entry_list = []
        try:
            self.last_scan_page_number = BoardScanning.objects.filter(
                board_name=board_name).order_by('-page_number_of_last_scan').first().page_number_of_last_scan
        except (BoardScanning.DoesNotExist, AttributeError):
            self.last_scan_page_number = self._get_newest_page_code()

    def _get_soup_object(self, target_url):
        user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
        headers = {"User-Agent": user_agent}
        cookie = {'over18': '1'}
        requests.packages.urllib3.disable_warnings()
        context = requests.get(target_url, headers=headers, cookies=cookie, verify=False).text
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

    def _get_newest_page_code(self):
        soup = self._get_soup_object(self.url)
        try:
            pre_page_url = self.PTT_PREFIX + soup.select('.wide')[1]['href']
        except (IndexError):
            logging.info('Got ' + self.url + ' pre page URL fail')
            return -1
        pre_page_num = self._get_page_code(pre_page_url)
        newest_page_num = pre_page_num + 1
        return newest_page_num

    def _get_entries_from_url(self, url):

        entry_list = []
        soup = self._get_soup_object(url)
        if len(soup.select('.wide')) <= 0:   # html structure change or HTTPError
                return entry_list

        entries = soup.select('.r-ent')

        for item in entries:
            if len(item.select('.title > a')) <= 0:
                continue

            title = item.select('.title > a')[0].text
            link = self.PTT_PREFIX + item.select('.title > a')[0]['href']
            author = item.select('.meta > .author')[0].text
            date = item.select('.meta > .date')[0].text
            entry_list.append({'topic': title, 'url': link, 'author': author, 'date': date})
        return entry_list

    def get_entries_after_last_fetch(self):

        # if already get the articles, return list directly
        if self.entry_list:
            return self.entry_list

        # Get prepare to scan range
        newest_page_code = self._get_newest_page_code()
        if newest_page_code == -1:
            return []
        prepare_scanned_page_numbers = range(self.last_scan_page_number, newest_page_code + 1)

        # Scan page and append to all entries
        all_entries = []
        for page_number in prepare_scanned_page_numbers:
            scan_url = self.URL_CONTAIN_PAGE_NUMBER.format(self.target, page_number)
            entries = self._get_entries_from_url(scan_url)
            all_entries = all_entries + entries

        # Assign to self entry list for cache and recrod scan status
        self.entry_list = all_entries
        BoardScanning.objects.create(board_name=self.target,
                                     page_number_of_last_scan=newest_page_code,
                                     last_scan_pages_count=len(prepare_scanned_page_numbers))
        return all_entries
