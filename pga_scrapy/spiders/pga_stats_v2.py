import scrapy


class PgaStatsV2Spider(scrapy.Spider):
    name = 'pga_stats_v2'
    allowed_domains = ['pgatour.com']
    start_urls = ['http://pgatour.com/stats/']

    def parse(self, response):
        links = response.xpath(
            "*//ul[contains(@class, 'nav-tabs-drop')]/li/a[not(@data-toggle)]/@href")[1:8]

        for link in links:
            stats_page = link.get()
            yield response.follow(stats_page, callback=self.parse_stats)

    def parse_stats(self, response):
        links = response.xpath(
            "*//div[contains(@class, 'table-content')]//a/@href")

        for link in links:
            stats_table = link.get()[:-5] + ".y2020.html"
            yield response.follow(stats_table, callback=self.parse_stats_table)

    def parse_stats_table(self, response):
        pga_stats = {}

        pga_stats['name'] = response.xpath(
            "*//div[@class='header']/h1/text()").get()

        pga_stats['table'] = response.xpath("*//table[@id='statsTable']").get()

        yield pga_stats
