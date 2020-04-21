import datetime
from spiders.CoronaSpider import CoronaSpider


class AlJazeeraSpider(CoronaSpider):
    source_name = "al jazeera"
    name = "Al Jazeera Spider"
    start_urls = ['https://www.aljazeera.com/news/2020/01/countries-confirmed-cases-coronavirus-200125070959786.html']

    def corona_parse(self, response):
        # All data of Israel state
        # <h3>Israel - 9,006 cases, 60 deaths</h3>
        israel_data = response.xpath('//h3[contains(text(), "Israel")]/text()').get()
        sick_israel = str(israel_data.split(" ")[2].replace(',', ''))

        return sick_israel

