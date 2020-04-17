import datetime

from scrapy.crawler import CrawlerProcess

from spiders.CoronaSpider import CoronaSpider


class ClalitSpider(CoronaSpider):
    source_name = "clalit"
    name = "Clalit Spider"
    start_urls = ['https://www.clalit.co.il/he/your_health/family/Pages/coronavirus_situation_update_worldwide.aspx']

    def corona_parse(self, response):
        # All data of Israel state
        israel_data = response.xpath('//tr[td[span[strong[text()[contains(.,"ישראל")]]]]]/td/span/span/text()').getall()
        
        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))

        return sick_israel


# process = CrawlerProcess()
# process.crawl(ClalitSpider)
# process.start()
