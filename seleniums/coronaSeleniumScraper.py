from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import datetime
from coronaDB import MyCoronaDB


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

    def scrape(self):
        self.db = MyCoronaDB()
        browser = webdriver.Firefox()
        browser.get(self.source_html)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        sick_israel = self.get_data_from_element(browser)

        browser.quit()
        print(f"\nFound: {self.source_name}, {sick_israel}, {current_time}\n")
        self.db.insert_record(self.source_name, sick_israel, current_time)
        # self.db.print_db()
        self.db.close()

    @abstractmethod
    def get_data_from_element(self, browser):
        pass
