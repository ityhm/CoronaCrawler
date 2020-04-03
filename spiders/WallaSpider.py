import datetime
from spiders.CoronaSpider import CoronaSpider


class WallaSpider(CoronaSpider):
    source_name = "walla"
    name = "Walla Spider"
    start_urls = ['https://www.walla.co.il/']

    def corona_parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # All data of Israel state
        israel_data = response.xpath('//div[contains(@class, "homepage-corona-wrap")]/main/ul/'
                                     'li[contains(h3,"בישראל")]/ul/li[contains(h4,"נדבקים")]/span/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))
        CoronaSpider.send_result(self, sick_israel, date)

