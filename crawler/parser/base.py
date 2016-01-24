# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class BaseParser:
    """Base parser super class
    """
    encoding = 'utf-8'
    parser = 'lxml'  # one of ['html.paraer', 'lxml', 'html5lib']

    def __init__(self, work=None, wall=None, initial=False, page=0):
        if work:
            self.work = work
        elif wall:
            self.wall = wall

        self.initial = initial
        self.page = page

    @property
    def url(self):
        raise NotImplementedError

    @property
    def selector(self):
        raise NotImplementedError

    @staticmethod
    def wall_format(wall):
        raise NotImplementedError

    def parse(self, method='GET'):
        raise NotImplementedError

    def after_parse(self, parsed):
        raise NotImplementedError


class BaseHTMLParser(BaseParser):
    def parse(self, method='GET'):
        def parse_html(u):
            html = getattr(requests, str.lower(method))(u).text
            soup = BeautifulSoup(html, self.parser)
            return soup.select(self.selector)

        url = self.url if isinstance(self.url, list) else [self.url]
        return self.after_parse(map(parse_html, url))


class BaseJSONParser(BaseParser):
    def parse(self, method='GET'):
        def parse_json(u):
            json_string = getattr(requests, str.lower(method))(u).json
            # TODO: navigate json tree
            return json_string.json()

        url = self.url if isinstance(self.url, list) else [self.url]
        return self.after_parse(map(parse_json, url))
