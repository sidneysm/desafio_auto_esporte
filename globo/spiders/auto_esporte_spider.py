from scrapy.spiders import Spider
from bs4 import BeautifulSoup
from ..utils import split_elements, parse_element_to_json


class AutoEsporteSpider(Spider):
    name = 'revistaautoesporte'
    allowed_domains = ['revistaautoesporte.globo.com']
    start_urls = ['http://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    res = {
        'feed': []
    }

    def parse(self, response):
        """
        Chamada dos contracts para testes do spider.
        @url http://revistaautoesporte.globo.com/rss/ultimas/feed.xml
        @returns item 1 10
        @returns requests 0 0
        @scrapes feed
        @has_itens X-CustomHeader
        @has_title
        @has_link
        @has_description
        @has_description_something
        """

        # Seleciona os itens do feed
        itens_tag = response.xpath('//item')

        # Faz a iteração com os elementos de cada item
        # (title, link e description)
        for t, l, d in list(zip(itens_tag.xpath('.//title/text()'),
                            itens_tag.xpath('.//link/text()'),
                            itens_tag.xpath('.//description/text()'))):

            # Prepara o nó description para extração
            desc = BeautifulSoup(d.extract(), 'html.parser')

            # Separa cada elemento
            elementos_tag = split_elements(desc)

            # Examina e retorna cada elemento no formato json
            description = [parse_element_to_json(element) for
                           element in elementos_tag
                           if parse_element_to_json(element) is not None]

            # Compoe o item com as informações extraídas.
            item = {
                'title': t.extract(),
                'link': l.extract(),
                'description': description
            }
            # Adiciona o item ao feed
            self.res['feed'].append({"item": item})
        # o output será o feed já completo
        return self.res
