# -*- coding: utf-8 -*-

from crawler.serializer.base import BaseSerializer


class NaverComicSerializer(BaseSerializer):
    @property
    def work_list(self):
        def extract_work(item):
            work = {
                'model': 'work',
                'thumb': '',
                'title': '',
                'author': '',
                'is_updated': True or False,
            }
            work.update(self.extra_data)
            return work
        return map(extract_work, self.soup)

    @property
    def episode_list(self):
        def extract_episode(item):
            episode = {
                'model': 'episode',
                'thumb': '',
                'title': '',
                'author': '',
                'is_updated': True or False,
            }
            episode.update(self.extra_data)
            return episode
        return map(extract_episode, self.soup)

    def serialize(self):
        return {
            'service': 'naver',
            'type': 'comic',
            self.target: getattr(self, self.target),
        }


class NaverNovelSerializer(BaseSerializer):
    @property
    def work_list(self):
        def extract_work(item):
            work = {
                'model': 'work',
                'thumb': '',
                'title': '',
                'author': '',
                'is_updated': True or False,
            }
            work.update(self.extra_data)
            return work
        return map(extract_work, self.soup)

    @property
    def episode_list(self):
        def extract_episode(item):
            episode = {
                'model': 'episode',
                'thumb': '',
                'title': '',
                'author': '',
                'is_updated': True or False,
            }
            episode.update(self.extra_data)
            return episode
        return map(extract_episode, self.soup)

    def serialize(self):
        return {
            'service': 'naver',
            'type': 'comic',
            self.target: getattr(self, self.target),
        }
