# -*- coding: utf-8 -*-

from celery import Celery
from crawler import celery_settings
from crawler.parser.naver import NaverComicParser

import codecs
import json

app = Celery('crawler')
app.config_from_object(celery_settings)


class CrawlerIterator(object):
    def __init__(self):
        self.crawlers = []

    def register_crawler(self, crawler):
        if crawler not in self.crawlers:
            self.crawlers.append(crawler)

    def get(self):
        return iter(self.crawlers)


jobs = CrawlerIterator()
jobs.register_crawler(NaverComicParser)


@app.task(name='tasks.crawls_per_hour')
def crawls_per_hour():
    for job in jobs.get():
        crawls_wall.delay(job)


@app.task(name='tasks.crawls_wall')
def crawls_wall(job, wall=None):
    parsed_wall = job(wall=job.wall_format(wall)).parse()

    with codecs.open('result.txt', 'w+', 'utf-8') as f:
        for work in parsed_wall.get('work_list', []):
            f.write(json.dumps(work) + ',\n')
        # crawls_work.delay(job, work)


@app.task(name='tasks.crawls_work')
def crawls_work(job, work):
    data = job(work=work).parse()
