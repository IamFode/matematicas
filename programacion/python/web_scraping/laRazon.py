from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess


class Periodico(Item):
    titulo = Field()
    fecha = Field()
    hora = Field()

class laRazon(CrawlSpider):
    name = "laRazon"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36',
        'FEED_EXPORT_FIELDS': ["titulo","fecha","hora"],
        'CLOSESPIDER_PAGECOUNT': 2,
        'CLOSESPIDER_ITEMCOUNT': 2,
        'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes
    }
    download_delay = 1
    allowed_domains = ['www.la-razon.com']
    start_urls = [
            'https://www.la-razon.com/nacional/'
            ]

    rules = (
        Rule(
            LinkExtractor(
                allow=r'/nacional/page/\d+/'
            ), follow=True
        ),
        Rule(
            LinkExtractor(
                allow=r'/nacional/\d+/\d+/\d+/'
                #tags=('a'),
                #attrs=('href')
            ), follow=True, callback='parse_items'
        ),
    )

    def parse_items(self, response):
        item = ItemLoader(Periodico(), response)
        item.add_xpath('titulo', '//div[@class="col-12 col-lg-8"]/div[1]/h1/text()')
        item.add_xpath('fecha', '//div[@class="col-12 col-lg-8"]/div[2]/div[3]/div[2]/div/div/p/span[2]/text()')
        item.add_xpath('hora', '//div[@class="col-12 col-lg-8"]/div[2]/div[3]/div[2]/div/div/p/span[3]/text()')
        yield item.load_item()

process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # formato del archivo generado
    'FEED_URI': './data/laRazon.json',  # nombre del archivo generado
    'FEED_EXPORT_ENCODING': 'utf-8'
    })
process.crawl(laRazon)
process.start() # the script will block here until the crawling is finished
