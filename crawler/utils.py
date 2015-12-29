# -*- coding: utf-8 -*-

import urlparse


def get_url_query_dict(url):
    o = urlparse.urlparse(url)
    return dict(urlparse.parse_qsl(o.query))
