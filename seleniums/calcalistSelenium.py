from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class CalcalistSeleniumScraper(CoronaSeleniumScraper):
    source_name = "calcalist"
    source_html = "https://newmedia.calcalist.co.il/data_journalism/corona/index.html"

    def get_data_from_element(self, browser):
        web_element_israel_data = WebDriverWait(browser, 12).until(
            ec.presence_of_element_located((By.CLASS_NAME, "datafield_israel_sick")))

        sick_israel = web_element_israel_data.text

        return sick_israel.replace(',', '')
