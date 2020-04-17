from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Utilities.Logger import print_flush, selenium_save_source_to_file
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class GuardianScraper(CoronaSeleniumScraper):
    source_name = "guardian"
    source_html = "https://www.theguardian.com/world/2020/apr/07/coronavirus-world-map-which-countries-have-the-most-cases-and-deaths"

    def get_data_from_element(self, browser):
        # web_element_israel_data = WebDriverWait(browser, self.MAX_TIME_WAIT_LOAD).until(ec.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "interactive-atom-fence")))
        # print("FOUND!")

        # selenium_save_source_to_file(browser, "Guardian3.html")
        # web_element_israel_data = WebDriverWait(browser, 12).until(
        #         ec.presence_of_element_located((By.ID, "coronavirus-emea-map-svg")))
        sleep(30)
        selenium_save_source_to_file(browser, "Guardian2.html")
        #
        # selenium_save_source_to_file(browser, "Guardian.html")
        # <tr data-name="Israel" data-cases="9248" data-deaths="65">
        # ...
        # </tr>
        # israel_data = web_element_israel_data.find_elements_by_xpath("./g/text[tspan[contains(text(), 'Israel')]]/tspan")
        # sick_israel = israel_data[1].text

        # return sick_israel


# s = GuardianScraper()
# s.scrape()

