import datetime
from spiders.CoronaSpider import CoronaSpider


class ClalitSpider(CoronaSpider):
    source_name = "clalit"
    name = "Clalit Spider"
    start_urls = ['https://www.clalit.co.il/he/your_health/family/Pages/coronavirus_situation_update_worldwide.aspx']

    def corona_parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # All data of Israel state
        israel_data = response.xpath('//tr[td[span[strong[text()[contains(.,"ישראל")]]]]]/td/span/text()').getall()
        
        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))
        CoronaSpider.send_result(self, sick_israel, date)

