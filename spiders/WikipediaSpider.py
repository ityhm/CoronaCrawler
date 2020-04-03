import datetime
from spiders.CoronaSpider import CoronaSpider


class WikipediaSpider(CoronaSpider):
    source_name = "wikipedia"
    name = "Wikipedia Spider"
    start_urls = ['https://en.wikipedia.org/wiki/2019%E2%80%9320_coronavirus_pandemic_by_country_and_territory']

    def corona_parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # All data of Israel state
        israel_data = response.xpath('//tr[th[a[contains(text(),"Israel")]]]/td/text()').getall()

        # The first cell is the number of sick people
        sick_israel = str(israel_data[0].replace(',', '')).strip()
        CoronaSpider.send_result(self, sick_israel, date)

        # dirty_columns_values = response.xpath('//div[@id="covid19-container"]/table/tbody/tr[@class="covid-sticky"]/th')
        # first_part_columns = dirty_columns_values.xpath('./text()').getall()
        # second_part_columns = dirty_columns_values.xpath('./abbr/text()').getall()
        #
        # clean_columns_values = list(filter(lambda a: a != '\n', first_part_columns + second_part_columns))
        # print(f"Columns: {clean_columns_values}")
