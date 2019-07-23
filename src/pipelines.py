# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
from scrapy.conf import settings
import logging
import pymongo
import json
import os
import time

from scrapy import signals
from TweetScraper.items import Tweet, User
from TweetScraper.utils import mkdirs
from scrapy.exporters import JsonLinesItemExporter

logger = logging.getLogger(__name__)
class JsonLinesPipeline(object):
    def __init__(self):
        self.files = {}
      

    def open_spider(self, spider):
        print(spider.name, 'open spider')
        self.name = spider.name
        print(self.name)
        self.time = spider.start
        self.saveUserPath = settings['SAVE_USER_PATH']
        self.saveTweetPath = settings['SAVE_TWEET_PATH']
        mkdirs(self.saveTweetPath) # ensure the path exists
        mkdirs(self.saveUserPath)
        
        file = open(f'{self.saveUserPath}/{self.name}.json', 'wb')
        self.files[spider] = file
        
        self.exporter = JsonLinesItemExporter(file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
    
    def close_spider(self, spider):
        print(spider.name, self.name)
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()
        logger.warning(f'{self.name} finish {time.time() - self.time}')

    def process_item(self, item, spider):
        if item['usernameTweet'] == self.name:
            self.exporter.export_item(item)
            return item


class SaveToFilePipeline(object):
    ''' pipeline that save data to disk '''
    def __init__(self):
        self.saveTweetPath = settings['SAVE_TWEET_PATH']
        self.saveUserPath = settings['SAVE_USER_PATH']
        mkdirs(self.saveTweetPath) # ensure the path exists
        mkdirs(self.saveUserPath)

    def process_item(self, item, spider):
        print(spider)
        if isinstance(item, Tweet):
            savePath = os.path.join(self.saveTweetPath, item['usernameTweet']+item['ID'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.info("Update tweet:%s"%dbItem['url'])
            else:
                self.save_to_file(item,savePath)
                logger.debug("Add tweet:%s" %item['url'])

        elif isinstance(item, User):
            savePath = os.path.join(self.saveUserPath, item['usernameTweet']+item['ID'])
            if os.path.isfile(savePath):
                pass # simply skip existing items
                ### or you can rewrite the file, if you don't want to skip:
                # self.save_to_file(item,savePath)
                # logger.info("Update user:%s"%dbItem['screen_name'])
            else:
                self.save_to_file(item, savePath)
                logger.debug("Add user:%s" %item['screen_name'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))


    def save_to_file(self, item, fname):
        ''' input: 
                item - a dict like object
                fname - where to save
        '''
        with open(fname,'w') as f:
            json.dump(dict(item), f)
