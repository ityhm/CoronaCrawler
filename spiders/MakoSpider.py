import datetime
from spiders.CoronaSpider import CoronaSpider


class MakoSpider(CoronaSpider):
    source_name = "mako"
    name = "Mako"
    start_urls = ['https://corona.mako.co.il']

    def corona_parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # All data of Israel state
        israel_data = response.xpath('//section[contains(@class,"section stats-section")]'
                                     '/div/div/div/a/div/div[h5[contains(text(),"מספר הנדבקים")]]/p/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))
        CoronaSpider.send_result(self, sick_israel, date)

