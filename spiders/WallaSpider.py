import datetime

from scrapy.crawler import CrawlerProcess

from spiders.CoronaSpider import CoronaSpider


class WallaSpider(CoronaSpider):
    source_name = "walla"
    name = "Walla Spider"
    start_urls = ['https://www.walla.co.il/']

    def corona_parse(self, response):
        # All data of Israel state
        israel_data = response.xpath('//div[contains(@class, "homepage-corona-wrap")]/main/section'
                                     '[h3[contains(text(),"בישראל")]]/div/ul//li[h4[contains(text(),"נדבקים")]]'
                                     '/span/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', ''))

        return sick_israel

# process = CrawlerProcess()
# process.crawl(WallaSpider)
# process.start()