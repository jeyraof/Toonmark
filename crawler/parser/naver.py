# -*- coding: utf-8 -*-

from crawler.parser.base import BaseHTMLParser


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
        host = 'http://m.comic.naver.com/webtoon'

        if self.work:
            return '{host}/list.nhn?titleId={work}'.format(host=host, work=self.work)
        elif self.wall:
            return '{host}/weekday.nhn?week={wall}&sort=Update&order=Update'.format(host=host, wall=self.wall)

        raise AttributeError("'NaverComicParser' object must have one of wall or work attribute.")

    @property
    def selector(self):
        if self.work:
            return 'ul#pageList > li'
        elif self.wall:
            return 'ul#pageList > li'

        raise AttributeError("'NaverComicParser' object must have one of wall or work attribute.")

    def after_parse(self, parsed):
        return


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
        return
