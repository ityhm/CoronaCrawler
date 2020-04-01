from scrapy.crawler import CrawlerProcess
from coronaDB import MyCoronaDB
from seleniums.arcgisDashboardSelenium import ArcgisDashSeleniumScraper
from seleniums.ynetSelenium import YnetSeleniumScraper
from spiders.WorldmetersSpider import WorldometersSpider
from spiders.WikipediaSpider import WikipediaSpider

print("Welcome to the Corona Data Fetcher for Israel's sick counter")

db = MyCoronaDB()
# db.print_db()

print("Let's start scraping!")

# s = YnetSeleniumScraper()
# s.scrape()
#
# s = ArcgisDashSeleniumScraper()
# s.scrape()

process = CrawlerProcess()
process.crawl(WorldometersSpider)
process.crawl(WikipediaSpider)
process.start()



db.print_db()
db.close()
