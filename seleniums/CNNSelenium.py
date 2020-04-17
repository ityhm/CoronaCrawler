import datetime
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class CNNSeleniumScraper(CoronaSeleniumScraper):
    source_name = "cnn"
    source_html = "https://edition.cnn.com/interactive/2020/health/coronavirus-maps-and-cases/"

    def get_data_from_element(self, browser):
        web_element_israel_data = WebDriverWait(browser, self.MAX_TIME_WAIT_LOAD).until(
                ec.presence_of_element_located((By.CLASS_NAME, "region-table-list")))

        # <tr data-name="Israel" data-cases="9248" data-deaths="65">
        # ...
        # </tr>
        israel_data = web_element_israel_data.find_elements_by_xpath("./tbody/tr[contains(@data-name, 'Israel')]")
        sick_israel = israel_data[0].get_attribute("data-cases")

        return sick_israel


# s = CNNSeleniumScraper()
# s.scrape()
