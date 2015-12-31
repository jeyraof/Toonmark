# -*- coding: utf-8 -*-


class BaseSerializer:
    def __init__(self, target=None, soup=None, extra_data_wrap=None, extra_data_item=None):
        self.target = target
        self.soup = soup
        self.extra_data_wrap = extra_data_wrap or {}
        self.extra_data_item = extra_data_item or {}

    @property
    def episode_list(self):
        raise NotImplementedError

    @property
    def work_list(self):
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError
