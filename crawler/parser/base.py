# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class BaseParser:
    """Base parser super class
    """
    encoding = 'utf-8'
    parser = 'lxml'  # one of ['html.paraer', 'lxml', 'html5lib']
    _url = None

    def __init__(self):
        pass

    @property
    def url(self):
        if getattr(self, '_url', None) is None:
            raise NotImplementedError
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def after_parse(self, tag_list):
        """Do specific implemented job after getting soup from network.
        * Implementation required *

        :param tag_list: BeautifulSoup parsed tag element or python list
        :type tag_list: BeautifulSoup, list
        """
        raise NotImplementedError

    def parse(self, method='GET'):
        """This method parse with given :url:, :parser: and :selector: then pass data to  :after_parse:.

        :param method: http method for parsing page
        :type method: str get, post
        """
        raise NotImplementedError


class BaseHTMLParser(BaseParser):
    """Base HTML Parser
    """
    _selector = None

    @property
    def selector(self):
        if getattr(self, '_selector', None) is None:
            raise NotImplementedError
        return self._selector

    @selector.setter
    def selector(self, value):
        self._selector = value

    def parse(self, method='GET'):
        html = getattr(requests, str.lower(method))(self.url)
        soup = BeautifulSoup(html, self.parser)
        self.after_parse(soup.select(self.selector))


class BaseJSONParser(BaseParser):
    """Base JSON Parser
    """

    def parse(self, method='GET'):
        json_string = getattr(requests, str.lower(method))(self.url)
        self.after_parse(json_string.json())
