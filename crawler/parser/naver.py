# -*- coding: utf-8 -*-

from crawler.parser.base import BaseHTMLParser
from crawler.serializer import NaverComicSerializer, NaverNovelSerializer
from crawler.utils import build_query_string


class NaverComicParser(BaseHTMLParser):
    _target = (None, None)

    @property
    def work(self):
        if self._target[0] == 'work':
            return self._target[1]
        return None

    @work.setter
    def work(self, value):
        if not str.isdigit(value):
            raise ValueError("work must have digit value.")
        self._target = ('work', value)

    @property
    def wall(self):
        if self._target[0] == 'wall':
            return self._target[1]
        return None

    @wall.setter
    def wall(self, value):
        white_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        if str.lower(value) not in white_list:
            raise ValueError("wall must be a element contained by [{wl}]".format(wl=', '.join(white_list)))
        self._target = ('wall', str.lower(value))

    @property
    def url(self):
        if not self.work and not self.wall:
            raise AttributeError("'NaverComicParser' object must have one of wall or work attribute.")

        host = 'http://m.comic.naver.com/webtoon'

        if self.work:  # in case: work
            template = host + '/list.nhn?{query}'
            queries = {'titleId': self.work}

            if self.initial and self.page:
                url = []
                for p in xrange(1, self.page + 1):
                    dummy_queries = queries.copy()
                    dummy_queries.update({'page': p})
                    url.append(template.format(query=build_query_string(**dummy_queries)))
            elif self.page:
                queries.update({'page': self.page})
                url = template.format(query=build_query_string(**queries))
            else:
                url = template.format(query=build_query_string(**queries))

        else:  # in case: wall
            template = host + '/weekday.nhn?{query}'
            queries = {'week': self.wall, 'sort': 'Update', 'order': 'Update'}
            url = template.format(query=build_query_string(**queries))

        return url

    @property
    def selector(self):
        if not self.work and not self.wall:
            raise AttributeError("'NaverComicParser' object must have one of wall or work attribute.")

        if self.work:
            return 'ul#pageList > li'
        elif self.wall:
            return 'ul#pageList > li'

    def after_parse(self, parsed):
        if self.work:
            if isinstance(parsed, list):
                serialized = None
                for parsed_one in parsed:
                    serializer = NaverComicSerializer(target='episode_list',
                                                      soup=parsed_one,
                                                      extra_data={'work': self.work})
                    if not serialized:
                        serialized = serializer.serialize()
                    else:
                        serialized['episode_list'].extend(serializer.serialize(item_only=1))
                return serialized

            else:
                serializer = NaverComicSerializer(target='episode_list', soup=parsed, extra_data={'work': self.work})
                return serializer.serialize()

        elif self.wall:
            serializer = NaverComicSerializer(target='work_list', soup=parsed)
            return serializer.serialize()

        raise AttributeError("'NaverComicParser' object must have one of wall or work attribute.")


class NaverNovelParser(BaseHTMLParser):
    _target = (None, None)

    @property
    def work(self):
        if self._target[0] == 'work':
            return self._target[1]
        return None

    @work.setter
    def work(self, value):
        if not str.isdigit(value):
            raise ValueError("work must have digit value.")
        self._target = ('work', value)

    @property
    def wall(self):
        if self._target[0] == 'wall':
            return self._target[1]
        return None

    @wall.setter
    def wall(self, value):
        white_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        if str.upper(value) not in white_list:
            raise ValueError("wall must be a element contained by [{wl}]".format(wl=', '.join(white_list)))
        self._target = ('wall', str.upper(value))

    @property
    def url(self):
        host = 'http://m.novel.naver.com/webnovel'

        if self.work:
            return '{host}/list.nhn?novelId={work}'.format(host=host, work=self.work)
        elif self.wall:
            return '{host}/weekdayList.nhn?week={wall}&genre=all&order=Read'.format(host=host, wall=self.wall)

        raise AttributeError("'NaverNovelParser' object must have one of wall or work attribute.")

    @property
    def selector(self):
        if self.work:
            return 'ul.lst_type2.num_list > li'
        elif self.wall:
            return 'ul.lst_type2 > li'

        raise AttributeError("'NaverNovelParser' object must have one of wall or work attribute.")

    def after_parse(self, parsed):
        if self.work:
            serializer = NaverNovelSerializer(target='episode_list', soup=parsed, extra_data={'work': self.work})
            return serializer.serialize()

        elif self.wall:
            serializer = NaverNovelSerializer(target='work_list', soup=parsed)
            return serializer.serialize()

        raise AttributeError("'NaverNovelParser' object must have one of wall or work attribute.")
