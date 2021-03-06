from Utilities.Logger import print_flush, reset_log_info
from Utilities.coronaDB import MyCoronaDB
from seleniums.CNNSelenium import CNNSeleniumScraper
from seleniums.arcgisDashboardSelenium import ArcgisDashSeleniumScraper
from seleniums.calcalistSelenium import CalcalistSeleniumScraper
from seleniums.haaretzSelenium import HaaretzSeleniumScraper
from seleniums.ynetSelenium import YnetSeleniumScraper
from spiders.AlJazeeraSpider import AlJazeeraSpider
from spiders.BbcSpider import BbcSpider
from spiders.ClalitSpider import ClalitSpider
from spiders.MakoSpider import MakoSpider
from spiders.StatistaSpider import StatistaSpider
from spiders.WallaSpider import WallaSpider
from spiders.WorldmetersSpider import WorldometersSpider
from spiders.WikipediaSpider import WikipediaSpider
from spiders.ynetSpider import YnetSpider
from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerRunner
from multiprocessing import Process
import datetime
from time import sleep


def crawl_selenium_scrapers():
    s = ArcgisDashSeleniumScraper()
    s.scrape()

    s = CalcalistSeleniumScraper()
    s.scrape()

    s = CNNSeleniumScraper()
    s.scrape()

    s = HaaretzSeleniumScraper()
    s.scrape()

    # s = YnetSeleniumScraper()
    # s.scrape()


def run_seleniums_once():
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print_flush(f"Let's start scraping SELENIUM! {cur_time}")

    crawl_selenium_scrapers()

    db.print_db()

    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print_flush(f"FINISHED scraping SELENIUM! {cur_time}")


def run_seleniums_in_loops():
    while True:
        run_seleniums_once()

        # print_flush(f"Finished! {current_time}")
        sleep(60 * 10)


def crawl_spiders(runner):
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print_flush(f"Let's start scraping SPIDERS! {cur_time}")

    runner.crawl(AlJazeeraSpider)
    runner.crawl(BbcSpider)
    runner.crawl(ClalitSpider)
    runner.crawl(MakoSpider)
    runner.crawl(StatistaSpider)
    runner.crawl(WallaSpider)
    runner.crawl(WikipediaSpider)
    runner.crawl(WorldometersSpider)
    runner.crawl(YnetSpider)

    db.print_db()
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    print_flush(f"FINISHED scraping SPIDERS! {cur_time}")


def crawl_spiders_once():
    configure_logging()
    runner = CrawlerRunner()

    crawl_spiders(runner)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()


def one_time_scrape():
    crawl_spiders_once()
    run_seleniums_once()


def scrape_all_for_loop(runner):
    crawl_spiders(runner)
    run_seleniums_once()


def crawl_spiders_in_loop():
    configure_logging()
    runner = CrawlerRunner()
    task = LoopingCall(lambda: crawl_spiders(runner))
    task.start(60 * 10)
    reactor.run()


def loop_scraper():
    if __name__ == '__main__':
        p1 = Process(target=run_seleniums_in_loops)
        p1.start()
        p2 = Process(target=crawl_spiders_in_loop)
        p2.start()
        p1.join()
        p2.join()


def scrape_loop_together():
    configure_logging()
    runner = CrawlerRunner()
    task = LoopingCall(lambda: scrape_all_for_loop(runner))
    task.start(60 * 20)
    reactor.run()


print_flush("Welcome to the Corona Data Fetcher for Israel's sick counter")
# db.print_db()
current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
print_flush(f"Let's start scraping! {current_time}")

db = MyCoronaDB()
reset_log_info()
scrape_loop_together()
# loop_scraper()
# one_time_scrape()

db.print_db()
db.close()


