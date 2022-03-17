import scrapy
from ..items import AmazonScarpItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031&dc&crid=J8NIS8N46TA3&qid=1647517415&rnid'
        '=2684818031&sprefix=books%2Caps%2C1682&ref=sr_nr_p_n_publication_date_1 '
    ]

    def parse(self, response):

        items = AmazonScarpItem()

        # product_name = response.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[
        # 3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2').extract()
        product_name = response.css('.s-access-title').extract()
        items['Name_Of_Product'] = product_name

        yield items
