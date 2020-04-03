from scrapy.crawler import CrawlerProcess
from Utilities.coronaDB import MyCoronaDB
from seleniums.arcgisDashboardSelenium import ArcgisDashSeleniumScraper
from seleniums.ynetSelenium import YnetSeleniumScraper
from spiders.StatistaSpider import StatistaSpider
from spiders.WorldmetersSpider import WorldometersSpider
from spiders.WikipediaSpider import WikipediaSpider


def run_selenium_scrapers():
    s = YnetSeleniumScraper()
    s.scrape()

    s = ArcgisDashSeleniumScraper()
    s.scrape()


def run_spiders():
    p = CrawlerProcess()
    p.crawl(WorldometersSpider)
    p.crawl(WikipediaSpider)
    p.crawl(StatistaSpider)
    p.start()


print("Welcome to the Corona Data Fetcher for Israel's sick counter")

db = MyCoronaDB()
# db.print_db()

print("Let's start scraping!")

run_selenium_scrapers()
run_spiders()

db.print_db()
db.close()
