import scrapy
import datetime
from scrapy.crawler import CrawlerProcess
from coronaDB import MyCoronaDB


class WorldometersSpider(scrapy.Spider):
    sourceName = "worldmeters"
    name = "Worldometers Spider"
    # start_urls = ['https://www.ynet.co.il/home/0,7340,L-184,00.html']
    # //td[@class="ghciMivzakimHeadlines1"]/table/tr/td/text()
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)

        israelData = response.xpath('//table[@id="main_table_countries_today"]//tr[td[a[contains(text(),"Israel")]]]/td/text()').getall()
        columnSelector = response.xpath('//table[@id="main_table_countries_today"]/thead/tr/th')
        columns = []

        for selector in columnSelector:
            column = " ".join(selector.xpath('text()').getall())
            #print ("@@@@@@@@@@@@@@@@@@@@@@@ new column: " + column)
            columns.append(column)

        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sick_israel = str(israelData[0].replace(',', ''))
        db = MyCoronaDB()
        self.logger.info(", ".join([self.sourceName, sick_israel, time]))
        db.insert_record(self.sourceName, sick_israel, time)
        # db.print_db()
        db.close()

        yield {
            'source' : self.sourceName,
            'date' : time,
            'columns' : columns,
            'israelData' : israelData
        }

        #print(*columns, sep="|")
        #print(*israelData, sep="|")

process = CrawlerProcess()

process.crawl(WorldometersSpider)
process.start()


