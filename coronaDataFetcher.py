from scrapy.crawler import CrawlerProcess
from Utilities.coronaDB import MyCoronaDB
from seleniums.arcgisDashboardSelenium import ArcgisDashSeleniumScraper
from seleniums.calcalistSelenium import CalcalistSeleniumScraper
from seleniums.haaretzSelenium import HaaretzSeleniumScraper
from seleniums.ynetSelenium import YnetSeleniumScraper
from spiders.ClalitSpider import ClalitSpider
from spiders.MakoSpider import MakoSpider
from spiders.StatistaSpider import StatistaSpider
from spiders.WallaSpider import WallaSpider
from spiders.WorldmetersSpider import WorldometersSpider
from spiders.WikipediaSpider import WikipediaSpider
import datetime
from time import sleep


def run_selenium_scrapers():
    s = YnetSeleniumScraper()
    s.scrape()

    s = ArcgisDashSeleniumScraper()
    s.scrape()

    s = HaaretzSeleniumScraper()
    s.scrape()

    s = CalcalistSeleniumScraper()
    s.scrape()


def run_spiders():
    p = CrawlerProcess()
    p.crawl(WorldometersSpider)
    p.crawl(WikipediaSpider)
    p.crawl(StatistaSpider)
    p.crawl(WallaSpider)
    p.crawl(MakoSpider)
    p.crawl(ClalitSpider)
    p.start()


print("Welcome to the Corona Data Fetcher for Israel's sick counter")

db = MyCoronaDB()
# db.print_db()

while True:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print(f"Let's start scraping! {current_time}")

    run_selenium_scrapers()
    run_spiders()

    db.print_db()

    sleep(10 * 60)

# run_selenium_scrapers()
# run_spiders()

db.print_db()

db.close()
