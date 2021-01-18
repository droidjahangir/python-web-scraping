import scrapy
from scrapy_splash import SplashRequest


class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['https://crypto.com/price']

    script = '''
        function main(splash, args)
            splash.private_mode_enabled=false
            url = args.url
            assert(splash:go(url))
            assert(splash:wait(3))
            run_tab = assert(splash:select(".table-body-module--tableBody__content--2a7es.table-body-module--tableBody__clickable--3u5qW a[href='https://crypto.com/price/ethereum']"))
            run_tab:mouse_click()
            assert(splash:wait(3))
            splash:set_viewport_full()
            return splash:png()
        end
    '''
    def start_requests(self):
        yield SplashRequest(url = "https://crypto.com/price", callback=self.parse, endpoint="execute", args={
            'lua_source': self.script
        })

    def parse(self, response):
        print(response.body)
