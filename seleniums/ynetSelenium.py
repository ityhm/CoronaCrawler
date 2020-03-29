import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from coronaDB import MyCoronaDB
import time

sourceName = "ynet"
browser = webdriver.Firefox()
browser.get('https://www.ynet.co.il')

try:
    webElementIsraelData = WebDriverWait(browser, 8).until(ec.presence_of_element_located((By.ID, "israel_sicks_counter")))
except ex:
    print("Wait didn't work: " + ex)


# OLD CODE - getting the data from page source
html_source = browser.page_source
f = open("ynetSrc.html","w+")
f.write(html_source)
f.close()

time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sick_israel = webElementIsraelData.text

browser.quit()

db = MyCoronaDB()
result = "%s, %s, %s" % (sourceName, sick_israel, time)
print(result)
db.insert_record(sourceName, sick_israel.replace(',', ''), time)
# db.print_db()
db.close()

# print("ynet")
# print(webElementIsraelData.text)
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# stateTextList=webElementIsraelData.find_elements_by_xpath('span')
#
# # The state name is in the last cell, number of sick people in the first of <strong>
# stateName=stateTextList[-1].text
# stateNumber=webElementIsraelData.find_elements_by_xpath('span/strong')[0].text
#

# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# print("stateName: " + stateName)
# print("stateNumber: " + stateNumber)


