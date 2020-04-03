from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class YnetSeleniumScraper(CoronaSeleniumScraper):
    source_name = "ynet"
    source_html = "https://www.ynet.co.il"

    def get_data_from_element(self, browser):
        web_element_israel_data = WebDriverWait(browser, 8).until(
            ec.presence_of_element_located((By.ID, "israel_sicks_counter")))

        # The number of sick people in the first of <strong>
        sick_israel = web_element_israel_data.text

        return sick_israel.replace(',', '')
