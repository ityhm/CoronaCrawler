import datetime
from spiders.CoronaSpider import CoronaSpider


class BbcSpider(CoronaSpider):
    source_name = "bbc"
    name = "Bbc Spider"
    start_urls = ['https://www.bbc.com/news/world-51235105']

    def corona_parse(self, response):
        # All data of Israel state
        # <h3>Israel - 9,006 cases, 60 deaths</h3>
        israel_data = response.xpath('//tbody/tr[td[contains(text(), "Israel")]]'
                                     '/td[contains(@class, "core__value")]/text()').getall()
        sick_israel = str(israel_data[0].strip().replace(',', ''))

        return sick_israel

