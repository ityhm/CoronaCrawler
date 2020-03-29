import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from coronaDB import MyCoronaDB

source_name = "Jerusalem Post"
browser = webdriver.Firefox()
browser.get('https://www.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6')

try:
    wait = WebDriverWait(browser, 8)
    webElementIsraelData = wait.until(ec.visibility_of_element_located((By.XPATH, '//h5[span[contains(text(), "Israel")]]')))
except ex:
    print("Wait didn't work: " + ex)
    # wait for page to load
    time.sleep(8)
    # <h5><span style="color:#e60000"><strong>1.656</strong></span><span style="color:#ffffff">&nbsp;</span><span style="color:#d6d6d6">Israel</span></h5>
    webElementIsraelData = browser.find_element_by_xpath('//h5[span[contains(text(), "Israel")]]')

stateTextList=webElementIsraelData.find_elements_by_xpath('span')

# The state name is in the last cell, number of sick people in the first of <strong>
stateName=stateTextList[-1].text
sick_israel=webElementIsraelData.find_elements_by_xpath('span/strong')[0].text

browser.quit()

print(source_name)
print(sick_israel)
print(time)

db = MyCoronaDB()
result = "%s, %s, %s" % (source_name, sick_israel, time)
print(result)
db.insert_record(source_name, sick_israel.replace(',', ''), time)
# db.print_db()
db.close()


# OLD CODE - getting the data from page source
# html_source = browser.page_source
# print("Found: " + Selector(text=html_source).xpath('//h5[span[contains(text(), "Israel")]]/span/strong/text()').get())
# f = open("src.html","w+")
# f.write(html_source)
# f.close()


