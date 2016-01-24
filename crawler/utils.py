# -*- coding: utf-8 -*-

import datetime
import pytz
import urllib
import urlparse


def get_url_query_dict(url):
    o = urlparse.urlparse(url)
    return dict(urlparse.parse_qsl(o.query))


def build_query_string(**kwargs):
    return urllib.urlencode(kwargs)


def get_day_string(dt):
    """
    :param dt:
    :return: such as "monday", "tuesday", ..., "sunday".
    """
    if dt:
        return dt.strftime("%A")
    return datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime("%A")
