import scrapy
from ..items import Demo01Item


class QuoteSpider(scrapy.Spider):
    name = 'quotes_details'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        self.logger.info("This will show title author and tags of all quotes")

        items = Demo01Item()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tags'] = tags

            yield items
