#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-01-26 23:08:06
# @Last Modified by:   bustta
# @Last Modified time: 2015-02-01 02:46:50
import logging
import sys
import traceback


class LogUtil():
    def __init__(self):
        logging.basicConfig(
            filename="workerLog.txt",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s: %(message)s")

    def logger(self, msg):
        logging.info(msg)

    def log_exception(self):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        logging.exception(''.join('!! ' + line for line in lines))
