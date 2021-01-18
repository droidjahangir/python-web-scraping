import scrapy


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['https://crypto.com/price/']
    start_urls = ['http://https://crypto.com/price//']

    def parse(self, response):
        pass
