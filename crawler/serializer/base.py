# -*- coding: utf-8 -*-


class BaseSerializer:
    def __init__(self, target=None, soup=None, extra_data=None):
        self.target = target
        self.soup = soup
        self.extra_data = extra_data or {}

    @property
    def episode_list(self):
        raise NotImplementedError

    @property
    def work_list(self):
        raise NotImplementedError

    def serialize(self):
        raise NotImplementedError
