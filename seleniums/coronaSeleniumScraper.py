from abc import ABC, abstractmethod
from selenium import webdriver
import datetime
from Utilities import Logger
from Utilities.Logger import log_if_data_empty, log_to_file, print_flush, selenium_save_source_to_file, log_info_line
from Utilities.coronaDB import MyCoronaDB


# Abstract class for selenium scrapers
class CoronaSeleniumScraper(ABC):
    db = None
    selenium_log_file = f"{Logger.logs_dir}/geckodriver.log"

    @property
    @abstractmethod
    def source_name(self):
        pass

    @property
    @abstractmethod
    def source_html(self):
        pass

    @abstractmethod
    def get_data_from_element(self, browser):
        pass

    def custom_log(self, data):
        log_info_line(f"{self.source_name} - {data.strip()}")

    def save_source_page(self, browser):
        selenium_save_source_to_file(browser, f"{Logger.html_dir}/{self.source_name}.html")

    def insert_data_to_db(self, sick_israel, current_time):
        if not log_if_data_empty(sick_israel, self.source_name):
            self.db = MyCoronaDB()
            self.db.insert_record(self.source_name, sick_israel, current_time)
            # self.db.print_db()
            self.db.close()

    def handle_error(self, browser, message):
        self.save_source_page(browser)
        print_flush(f"\nFailed to get data from website {self.source_name}")
        print_flush(f"Error: {str(message)}\n")
        log_to_file(self.source_name, str(message))
        browser.quit()

    def scrape(self):
        self.custom_log("Starting scrape")
        browser = webdriver.Firefox(log_path=self.selenium_log_file)
        browser.minimize_window()
        browser.get(self.source_html)

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            sick_israel = self.get_data_from_element(browser)

            if sick_israel is None or sick_israel == "":
                self.handle_error(browser, "Result is empty string")
        except Exception as ex:
            self.handle_error(browser, str(ex))
            return

        browser.quit()
        result_string = f"Found: '{sick_israel}'"

        self.custom_log(result_string)
        self.custom_log("Finished scrape")

        self.insert_data_to_db(sick_israel, current_time)
