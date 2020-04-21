import datetime
from spiders.CoronaSpider import CoronaSpider


class StatistaSpider(CoronaSpider):
    source_name = "Statista"
    name = "Statista Spider"
    start_urls = ['https://www.statista.com/statistics/1043366/novel-coronavirus-2019ncov-cases-worldwide-by-country/']

    def corona_parse(self, response):
        # ['Israel', <sick>]
        israel_data = response.xpath('//table[@id="statTableHTML"]//tr[td[contains(text(),"Israel")]]/td/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[1].replace(',', '')).strip()

        return sick_israel
