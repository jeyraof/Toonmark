# -*- coding: utf-8 -*-

import gevent.monkey
gevent.monkey.patch_all()

import datetime
import gevent
import gevent.queue
import pytz
import pprint

from crawler.parser import NaverComicParser


def crawl_wall(queue, db):
    while 1:
        # naver
        day = datetime.datetime.now(tz=pytz.timezone('Asia/Seoul')).strftime("%A")[:3]
        works = NaverComicParser(wall=day).parse()
        queue.put(works)

        gevent.sleep(60 * 60)


def crawl_work(queue, db):
    while 1:
        wall = queue.get()
        for work in wall.get('work_list', []):
            # work : work dict
            # TODO: work 를 db에 넣고 initial 일경우와 아닐경우 판단
            pprint.pprint(work)
            # pprint.pprint(NaverComicParser(work=work.get('uid')).parse())


def main():
    db = 1
    queue = gevent.queue.Queue()

    a = gevent.spawn(crawl_wall, queue, db)
    b = gevent.spawn(crawl_work, queue, db)

    gevent.joinall([a, b])


if __name__ == '__main__':
    # pprint.pprint(NaverComicParser(work=602921).parse())
    # pprint.pprint(NaverComicParser(wall='thu').parse())
    main()
