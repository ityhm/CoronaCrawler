from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class HaaretzSeleniumScraper(CoronaSeleniumScraper):
    source_name = "haaretz"
    source_html = "https://www.haaretz.co.il/"

    def get_data_from_element(self, browser):
        web_element_israel_data = WebDriverWait(browser, self.MAX_TIME_WAIT_LOAD).until(
            ec.presence_of_element_located((By.CLASS_NAME, "corona-israel-infected")))

        # In case text is not loaded yet inside <span></span>
        # WebDriverWait(browser, self.MAX_TIME_WAIT_LOAD)\
        #     .until(lambda driver: web_element_israel_data.find_elements_by_xpath("./span")[0].text.strip() != '')

        # <span>num</span>
        sick_israel = web_element_israel_data.find_elements_by_xpath("./span")[0].text
        return sick_israel.replace(',', '')


# s = HaaretzSeleniumScraper()
# s.scrape()
