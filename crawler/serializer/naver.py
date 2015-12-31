# -*- coding: utf-8 -*-

from crawler.serializer.base import BaseSerializer
from crawler.utils import get_url_query_dict


class NaverComicSerializer(BaseSerializer):
    @property
    def work_list(self):
        def extract_work(tag):
            work = {
                'author': tag.select_one('.sub_info').string.strip() or None,
                'model': 'work',
                'uid': get_url_query_dict(tag.select_one('a.right_arr').get('href')).get('titleId', None),
                'thumb': tag.select_one('.im_inbr > img').get('src', None),
                'title': tag.select_one('.toon_name span').string.strip() or None,
                'is_updated': True if tag.select_one('.ico_up') else False,
            }
            work.update(self.extra_data_item)
            return work
        return map(extract_work, self.soup)

    @property
    def episode_list(self):
        def extract_episode(tag):
            episode = {
                'model': 'episode',
                'uid': get_url_query_dict(tag.select_one('.lst > a').get('href')).get('no', None),
                'thumb': tag.select_one('.im_inbr > img').get('src', None),
                'title': tag.select_one('.toon_name span').string.strip() or None,
                'is_updated': True if tag.select_one('.ico_up') else False,
            }
            episode.update(self.extra_data_item)
            return episode
        return map(extract_episode, self.soup)

    def serialize(self, item_only=0):
        if item_only:
            return getattr(self, self.target)

        serialized = {
            'service': 'naver',
            'type': 'comic',
            self.target: getattr(self, self.target),
        }
        serialized.update(self.extra_data_wrap)
        return serialized


class NaverNovelSerializer(BaseSerializer):
    @property
    def work_list(self):
        def extract_work(tag):
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
        def extract_episode(tag):
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

    def serialize(self, item_only=0):
        if item_only:
            return getattr(self, self.target)

        return {
            'service': 'naver',
            'type': 'comic',
            self.target: getattr(self, self.target),
        }
