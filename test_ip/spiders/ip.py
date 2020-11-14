import scrapy


class IpSpider(scrapy.Spider):
    name = 'ip'

    def start_requests(self):
        urls = ['https://www.myip.com/']
        for _ in range(self.settings.getint('TEST_PROXY_COUNT')):
            for url in urls:
                yield scrapy.Request(url=url,
                                     callback=self.parse,
                                     dont_filter=True)

    def parse(self, response):
        ip = response.css('#ip::text').get()
        yield {'ip': ip,
               'ua': str(response.request.headers['User-Agent'])}
