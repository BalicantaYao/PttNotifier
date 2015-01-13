#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kenny.tsai
# @Date:   2014-12-05 09:52:34
# @Last Modified by:   kenny.tsai
# @Last Modified time: 2014-12-08 10:35:17

# https://www.ptt.cc/bbs/BuyTogether/index.html
from bs4 import BeautifulSoup
import requests
import datetime
import logging
import os


logging.basicConfig(
    filename="PttNotifierLog.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s: %(message)s")

ptt_site = 'https://www.ptt.cc'
board = 'BuyTogether'

todaySendListSet = []


def send_simple_message(mail_to, subject, msg):
    log_msg = "To: {0}\nMsg: {1}".format(mail_to, msg)
    logging.info(log_msg)
    return requests.post(
        "https://api.mailgun.net/v2/sandbox3973be0c4dc3412f853adf1f3d669499.mailgun.org/messages",
        auth=("api", os.environ['MAILGUN_KEY']),
        data={
            "from": "PTTNotifier <postmaster@sandbox3973be0c4dc3412f853adf1f3d669499.mailgun.org>",
            "to": mail_to,
            "subject": subject,
            "text": msg
            })


def get_ptt_soup_obj(site_url):
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {"User-Agent": user_agent}
    requests.packages.urllib3.disable_warnings()
    return BeautifulSoup(requests.get(site_url, headers=headers, verify=False).text)


def get_match_items(entry_list, keywords):
    match_objs = []
    is_all_match = True
    # print entry_list
    for item in entry_list:
        is_all_match = True
        if len(item.select('.title > a')) <= 0:
            continue

        title = item.select('.title > a')[0].text
        # print title
        for keyword in input_keywords:
            is_all_match &= (keyword in title)

        if is_all_match:
            link = ptt_site + item.select('.title > a')[0]['href']
            author = item.select('.meta > .author')[0].text
            date = item.select('.meta > .date')[0].text
            match_objs.append({'topic': title, 'url': link, 'author': author, 'date': date})
            # print u"MATCH => {0}, {1}, {2}, {3}".format(title, link, author, date)
    return match_objs


def construct_mail_content_and_send(mail_address, match_objs):
    if match_objs:
        msg = ''
        for match_item in match_objs:
            msg += "Topic: {0} \nUrl: {1} \nAuthor: {2} \nDate: {3}\n\n".format(
                match_item['topic'].encode('utf-8'), match_item['url'], match_item['author'], match_item['date'])

        if isSendThisUserTheSameItemToday(mail_address, match_item['url']):
#            print u"Notify Had Been Send!"
             logging.info("Notify Had Been Send!")
        else:
#            print u"Send Notify Now!"
            subject = '{0} Notify'.format(board)
            send_simple_message(mail_address, subject, msg)


def isSendThisUserTheSameItemToday(mail, url):
    key = mail + '_' + url
    if (key in todaySendListSet):
        return True
    else:
        todaySendListSet.append(key)
        return False


def reset_today_send_list():
    dt_object = datetime.datetime.now()
    if dt_object.hour == 0 and dt_object.minute == 0:
        del todaySendListSet[:]
        logging.info("Reset TodaySendList")




url = 'https://www.ptt.cc/bbs/{0}/index.html'.format(board)
mail_address = 'bustta <bustta80980@gmail.com>'
# input_keywords = [u'威秀']
input_keywords = [u'3M', u'手套']
subscribers = []
subscribers.append({'mail': mail_address, 'keywords': input_keywords})

is_this_minute_exe = False
while True:
    now_min = datetime.datetime.now().minute
    if now_min % 5 == 0 and not is_this_minute_exe:
        # logging.info("Fetch at {0}".format(datetime.datetime.now()))
        # print "Fetch at {0}".format(datetime.datetime.now())
        is_this_minute_exe = True

        latest_soup = get_ptt_soup_obj(url).select('.r-ent')
        for each_client in subscribers:
            construct_mail_content_and_send(each_client['mail'], get_match_items(latest_soup, each_client['keywords']))

        reset_today_send_list()

    elif now_min % 5 != 0:
        is_this_minute_exe = False

