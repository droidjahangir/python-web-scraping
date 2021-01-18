import scrapy

class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['www.cigabuy.com']
    # start_urls = ['https://www.cigabuy.com/specials.html']

    def start_requests(self):
        yield scrapy.Request(url='https://www.cigabuy.com/specials.html', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
        })

    def parse(self, response):
        for product in response.xpath('//ul[@class="productlisting-ul"]/div[@class="p_box_wrapper"]'):
            yield {
                'title': product.xpath('.//div/a[@class="p_box_title"]/text()').get(),
                'url': product.xpath('.//div/a[@class="p_box_title"]/@href').get(),
                # if href have no domain name then manually add this by using response.urljoin() method
                # 'url': response.urljoin(product.xpath('.//div[@class="p_box_wrapper"]/div/a[@class="p_box_title"]/@href').get()),
                'special_price': product.xpath('.//div/div[@class="p_box_price cf"]/span[@class="productSpecialPrice fl"]/text()').get(),
                'original_price': product.xpath('.//div/div[@class="p_box_price cf"]/text()').get(),
                # another original price --> //div[@class="p_box_wrapper"]/div/div[@class="p_box_price cf"]/span[@class="normalprice fl"]
                'another_price': product.xpath('//div[@class="p_box_wrapper"]/div/div[@class="p_box_price cf"]/span[@class="normalprice fl"]/text()').get(),
                'User-Agent': response.request.headers['User-Agent']
            }
        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
            })

