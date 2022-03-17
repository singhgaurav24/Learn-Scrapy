import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LoggingDemo(scrapy.Spider):
    name = "logging_demo"
    start_urls = {
        'https://quotes.toscrape.com/login'
    }

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        # print(token)
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'gauravsingh',
            'password' : 'gaurav'
        },callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        title = response.css('title::text').extract()
        yield {'title_text': title}
