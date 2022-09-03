# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class UseragentPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):
    def __int__(self):
        super().__init__()

    def open_spider(self, spider):
        self.file = open(f'{spider.name}.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        if item['category'] == 'Browsers':
            self.file.write(f"{item['useragent']}\n")
        return item
