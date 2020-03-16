# -*- coding: utf-8 -*-

import pymongo

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CrawlDataPipeline(object):
    def process_item(self, item, spider):
        return item

class PolicyMongoPipeline(object):
    collection = 'sample_task'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[self.collection].drop()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        table = self.db[self.collection]
        if 'date' in item.keys():
            table.insert(item)
        else:
            table.update_one({'UID':item['UID']},{'$set':item},upsert=True)
        return item