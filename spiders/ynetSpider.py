import datetime

import scrapy
from scrapy.crawler import CrawlerRunner, CrawlerProcess
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from Utilities.Logger import print_flush
from spiders.CoronaSpider import CoronaSpider


class YnetSpider(CoronaSpider):
    source_name = "ynet"
    name = "Ynet Spider"
    # start_urls = ['https://www.ynet.co.il']
    start_urls = ['https://z.ynet.co.il/fast/content/2020/coronavirus/status3.aspx']

    def corona_parse(self, response):
        # should get a list with current and yesterday's number of sick in israel
        israel_list = response.xpath('//script').re('\"author\"\: \"(.*)"')

        # take the max value, should be the correct one
        sick_israel = max(israel_list)

        return sick_israel


# process = CrawlerProcess()
# process.crawl(YnetSpider)
# process.start()
#
# configure_logging()
# runner = CrawlerRunner()
#
# d = runner.crawl(YnetSpider)
# d.addBoth(lambda _: reactor.stop())
# reactor.run()
