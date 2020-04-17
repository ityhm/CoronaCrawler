import datetime
from abc import ABC, abstractmethod
import scrapy
from scrapy import Request
from Utilities.Logger import log_if_data_empty, log_to_file, log_info_line
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

    def custom_log(self, data):
        log_info_line(f"{self.source_name} - {data.strip()}")

    def parse(self, response):
        try:
            self.custom_log("Starting crawling")
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = self.corona_parse(response)
            self.send_result(result, date)

            self.custom_log(f"Found: '{result}'")
            self.custom_log("Finished crawling")
        except Exception as ex:
            print(f"\nFailed to get data from website {self.source_name}\n")
            log_to_file(self.source_name, f"Error: {str(ex)}")
            return

        # if crawl again, parse again the same url
        yield Request(response.url, callback=self.parse)

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

