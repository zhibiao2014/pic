# -*- coding: utf-8 -*-
import urllib.request
import os
import redis
import pymysql
from scrapy.conf import settings

class PicPipeline(object):
    def process_item(self, item, spider):
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        # req = urllib.request.Request(url=item['addr'],headers=headers)
        # res = urllib.request.urlopen(req)
        # filename = os.path.join(r'D:\pic',item['name']+'.jpg')
        # with open(filename,'wb') as fp:
        #     fp.write(res.read()) 
        # r = redis.Redis(host='127.0.0.1',port=6379,db=0)
        # r.lpush('urls',item['addr'])
        dbargs = dict(
                host=settings['MYSQL_HOST'],		
                db=settings['MYSQL_DB'],
                user=settings['MYSQL_USER'],
                passwd=settings['MYSQL_PASS'],
                charset='utf8',
                use_unicode=True,
	    )
        dbpool = pymysql.connect(dbargs)
        return dbpool
        # return item
