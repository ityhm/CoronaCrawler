import datetime
from spiders.CoronaSpider import CoronaSpider


class WorldometersSpider(CoronaSpider):
    source_name = "worldmeters"
    name = "Worldmeters Spider"
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def corona_parse(self, response):
        # All data of Israel state
        israel_data = response.xpath('//table[@id="main_table_countries_today"]'
                                     '//tr[td[a[contains(text(),"Israel")]]]/td/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))

        return sick_israel
