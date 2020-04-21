import datetime
from spiders.CoronaSpider import CoronaSpider


class WikipediaSpider(CoronaSpider):
    source_name = "wikipedia"
    name = "Wikipedia Spider"
    start_urls = ['https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory']

    def corona_parse(self, response):
        # All data of Israel state
        israel_data = response.xpath('//tr[th[a[contains(text(),"Israel")]]]/td/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', '')).strip()

        return sick_israel
