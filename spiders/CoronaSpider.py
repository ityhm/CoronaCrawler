from abc import ABC, abstractmethod
import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from coronaDB import MyCoronaDB


# Abstract class for selenium scrapers
class CoronaSpider(ABC, scrapy.Spider):

    @property
    @abstractmethod
    def source_name(self):
        pass

    @property
    @abstractmethod
    def start_urls(self):
        pass

    @property
    @abstractmethod
    def parse(self, response):
        pass

    def send_result(self, sick, date):
        db = MyCoronaDB()
        db.insert_record(self.source_name, sick, date)
        # db.print_db()
        db.close()

        # yield {
        #     'source': self.sourceName,
        #     'sick': sick,
        #     'date': date
        # }

