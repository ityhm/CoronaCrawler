from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class YnetSeleniumScraper(CoronaSeleniumScraper):
    source_name = "ynet"
    source_html = "https://www.ynet.co.il"

    def get_data_from_element(self, browser):
        try:
            webElementIsraelData = WebDriverWait(browser, 8).until(
                ec.presence_of_element_located((By.ID, "israel_sicks_counter")))
        except ex:
            print("Wait didn't work: " + ex)

        # The number of sick people in the first of <strong>
        sick_israel = webElementIsraelData.text

        return sick_israel.replace(',', '')
