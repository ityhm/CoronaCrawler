from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class ArcgisDashSeleniumScraper(CoronaSeleniumScraper):
    source_name = "Johns Hopkins University"
    source_html = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

    def get_data_from_element(self, browser):
        web_element_israel_data = WebDriverWait(browser, self.MAX_TIME_WAIT_LOAD).until(
            ec.visibility_of_element_located((By.XPATH, '//h5[span[contains(text(), "Israel")]]')))

        # The number of sick people in the first of <strong>
        sick_israel = web_element_israel_data.find_elements_by_xpath('span/strong')[0].text

        return sick_israel.replace(',', '')


# s = ArcgisDashSeleniumScraper()
# s.scrape()
