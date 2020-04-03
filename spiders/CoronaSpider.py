from abc import ABC, abstractmethod
import scrapy

from Utilities.Logger import log_if_data_empty, log_to_file
from Utilities.coronaDB import MyCoronaDB


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
    def corona_parse(self):
        pass

    def parse(self, response):
        try:
            self.corona_parse(response)
        except Exception as ex:
            print(f"\nFailed to get data from website {self.source_name}\n")
            log_to_file(self.source_name, str(ex))
            return
        pass

    def send_result(self, sick, date):
        if not log_if_data_empty(sick, self.source_name):
            db = MyCoronaDB()
            db.insert_record(self.source_name, sick, date)
            # db.print_db()
            db.close()

        # yield {
        #     'source': self.sourceName,
        #     'sick': sick,
        #     'date': date
        # }

