import datetime
from spiders.CoronaSpider import CoronaSpider


class WorldometersSpider(CoronaSpider):
    source_name = "worldmeters"
    name = "Worldmeters Spider"
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # All data of Israel state
        israel_data = response.xpath('//table[@id="main_table_countries_today"]//tr[td[a[contains(text(),"Israel")]]]/td/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))
        CoronaSpider.send_result(self, sick_israel, date)

        # columnSelector = response.xpath('//table[@id="main_table_countries_today"]/thead/tr/th')
        # columns = []
        #
        # for selector in columnSelector:
        #     column = " ".join(selector.xpath('text()').getall())
        #     columns.append(column)
