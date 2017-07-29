from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from utils import split_elements, parse_element_to_json


class AutoEsporteSpider(Spider):
    name = 'revistaautoesporte'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['http://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    res = {
        'feed': []
    }

    def parse(self, response):

        itens_tag = response.xpath('//item')

        for t, l, d in list(zip(itens_tag.xpath('.//title/text()'),
                            itens_tag.xpath('.//link/text()'),
                            itens_tag.xpath('.//description/text()'))):

            desc = BeautifulSoup(d.extract(), 'html.parser')

            elementos_tag = split_elements(desc)

            description = [parse_element_to_json(element) for
                           element in elementos_tag
                           if parse_element_to_json(element) is not None]

            item = {
                'title': t.extract(),
                'link': l.extract(),
                'description': description
            }
            self.res['feed'].append({"item": item})

        return self.res
