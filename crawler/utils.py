# -*- coding: utf-8 -*-

import urllib
import urlparse


def get_url_query_dict(url):
    o = urlparse.urlparse(url)
    return dict(urlparse.parse_qsl(o.query))


def build_query_string(**kwargs):
    return urllib.urlencode(kwargs)
