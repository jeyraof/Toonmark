# -*- coding: utf-8 -*-

from crawler.parser.base import BaseJSONParser


class Gae9NovelParser(BaseJSONParser):
    @property
    def url(self):
        return 1

    @property
    def selector(self):
        return 1

    def after_parse(self, parsed):
        pass
