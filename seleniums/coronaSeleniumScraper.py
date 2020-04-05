from abc import ABC, abstractmethod
from selenium import webdriver
import datetime

from Utilities.Logger import log_if_data_empty, log_to_file
from Utilities.coronaDB import MyCoronaDB


# Abstract class for selenium scrapers
class CoronaSeleniumScraper(ABC):
    db = None

    @property
    @abstractmethod
    def source_name(self):
        pass

    @property
    @abstractmethod
    def source_html(self):
        pass

    def insert_data_to_db(self, sick_israel, current_time):
        if not log_if_data_empty(sick_israel, self.source_name):
            self.db = MyCoronaDB()
            self.db.insert_record(self.source_name, sick_israel, current_time)
            # self.db.print_db()
            self.db.close()

    def scrape(self):
        browser = webdriver.Firefox()
        browser.minimize_window()
        browser.get(self.source_html)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            sick_israel = self.get_data_from_element(browser)
        except Exception as ex:
            print(f"\nFailed to get data from website {self.source_name}\n")
            log_to_file(self.source_name, str(ex))
            browser.quit()
            return

        browser.quit()
        print(f"\nFound: {self.source_name}, {sick_israel}, {current_time}\n")

        self.insert_data_to_db(sick_israel, current_time)


    @abstractmethod
    def get_data_from_element(self, browser):
        pass
