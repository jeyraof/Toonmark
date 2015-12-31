# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class BaseParser:
    """Base parser super class
    """
    encoding = 'utf-8'
    parser = 'lxml'  # one of ['html.paraer', 'lxml', 'html5lib']

    def __init__(self, work=None, wall=None):
        if work:
            self.work = work
        elif wall:
            self.wall = wall

    @property
    def url(self):
        raise NotImplementedError

    @property
    def selector(self):
        raise NotImplementedError

    def parse(self, method='GET'):
        raise NotImplementedError

    def after_parse(self, parsed):
        raise NotImplementedError


class BaseHTMLParser(BaseParser):
    def parse(self, method='GET'):
        html = getattr(requests, str.lower(method))(self.url).text
        soup = BeautifulSoup(html, self.parser)
        return self.after_parse(soup.select(self.selector))


class BaseJSONParser(BaseParser):
    def parse(self, method='GET'):
        json_string = getattr(requests, str.lower(method))(self.url).json
        return self.after_parse(json_string.json())
