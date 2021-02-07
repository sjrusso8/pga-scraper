import scrapy


class PgaStatsV2Spider(scrapy.Spider):
    """Spider used to collect each of the html pages containing PGA tour stats"""

    name = 'pga_stats_v2'
    allowed_domains = ['pgatour.com']
    start_urls = ['http://pgatour.com/stats/']

    def parse(self, response):
        links = response.xpath(
            "*//ul[contains(@class, 'nav-tabs-drop')]/li/a[not(@data-toggle)]/@href")[1:8]  # exclude the first and last url as those don't matter

        for link in links:
            stats_page = link.get()
            yield response.follow(stats_page, callback=self.parse_stats)

    def parse_stats(self, response):
        links = response.xpath(
            "*//div[contains(@class, 'table-content')]//a/@href")

        for link in links:
            # change this if you want a different year
            stats_table = link.get()[:-5] + ".y2020.html" # Change this line to a different year to collect different stats. Format y.YYYY.html
            yield response.follow(stats_table, callback=self.parse_stats_table)

    def parse_stats_table(self, response):
        pga_stats = {}

        pga_stats['stat_group'] = response.xpath(
            "*//ul[contains(@class, 'nav-tabs-drop')]//li[@class='active']/a/text()").get()

        pga_stats['stat_name'] = response.xpath(
            "*//div[@class='header']/h1/text()").get()

        pga_stats['stat_table'] = response.xpath("*//table[@id='statsTable']").get()

        yield pga_stats
