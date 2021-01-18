import scrapy
from scrapy.shell import inspect_response

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    # start_urls = [
    #     'http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # # title = response.xpath("//h1/text()").get()
        # # countries = response.xpath("//td/a").getall()
        # countries = response.xpath("//td/a")

        # for country in countries:
        #     name = country.xpath(".//text()").get()
        #     link = country.xpath(".//@href").get()

        #     # absolute_url = f"https://www.worldometers.info{link}"
        #     # absolute_url = response.urljoin(link)

        yield response.follow(url="https://www.worldometers.info/world-population/china-population/", callback=self.parse_country, meta={'country_name': "China"})
            # yield scrapy.Request(url=absolute_url)

            # yield {
            #     # 'title': title,
            #     # 'countries': countries
            #     'country_name': name,
            #     'country_link': link
            # }
    def parse_country(self, response):
        # inspect_response(response, self)
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }
