# -*- coding: utf-8 -*-

from crawler.parser.base import BaseHTMLParser


class DaumComicParser(BaseHTMLParser):
    @property
    def url(self):
        return 1

    @property
    def selector(self):
        return 1

    def after_parse(self, parsed):
        pass
