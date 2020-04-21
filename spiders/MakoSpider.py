import datetime

from scrapy.crawler import CrawlerProcess

from spiders.CoronaSpider import CoronaSpider


class MakoSpider(CoronaSpider):
    source_name = "mako"
    name = "Mako"
    start_urls = ['https://corona.mako.co.il']

    def corona_parse(self, response):
        # All data of Israel state
        israel_data = response.xpath('//section[contains(@class,"section stats-section")]/div/div/div/a/div/div/'
                                     'p[contains(text()," בסך הכל")]/strong/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))

        return sick_israel


# process = CrawlerProcess()
# process.crawl(MakoSpider)
# process.start()
