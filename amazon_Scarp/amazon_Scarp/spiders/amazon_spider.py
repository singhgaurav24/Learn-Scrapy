import scrapy
from ..items import AmazonScarpItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031&dc&qid=1647849531&rnid=2684818031&ref=sr_nr_p_n_publication_date_1'
    ]

    def parse(self, response):
        items = AmazonScarpItem()
        product = response.css('.a-size-medium.a-text-normal::text').getall()
        product_author = response.css('.a-color-secondary .a-size-base+ .a-size-base::text').getall()
        product_price = response.css('.s-price-instructions-style .a-price-whole::text').getall()
        product_imagelink = response.css('.s-image::text').getall()

        # product = response.xpath('//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span//text()').get()


        items['product'] = product
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items