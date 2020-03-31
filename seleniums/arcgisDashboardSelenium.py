from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from seleniums.coronaSeleniumScraper import CoronaSeleniumScraper


# Class for selenium scrapers for Johns Hopkins University's Arcgis dashboard
class ArcgisDashSeleniumScraper(CoronaSeleniumScraper):
    source_name = "Johns Hopkins University"
    source_html = "https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6"

    def get_data_from_element(self, browser):
        try:
            wait = WebDriverWait(browser, 8)
            webElementIsraelData = wait.until(
                ec.visibility_of_element_located((By.XPATH, '//h5[span[contains(text(), "Israel")]]')))
        except ex:
            print("Wait didn't work: " + ex)
            # wait for page to load
            time.sleep(8)
            # <h5><span style="color:#e60000"><strong>1.656</strong></span><span style="color:#ffffff">&nbsp;</span><span style="color:#d6d6d6">Israel</span></h5>
            webElementIsraelData = browser.find_element_by_xpath('//h5[span[contains(text(), "Israel")]]')

        # The number of sick people in the first of <strong>
        sick_israel = webElementIsraelData.find_elements_by_xpath('span/strong')[0].text

        return sick_israel.replace(',', '')
