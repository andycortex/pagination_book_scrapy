import scrapy

url = 'http://quotes.toscrape.com/api/quotes?page={}'
class ScrollBooksSpider(scrapy.Spider):
    name = 'scroll_books'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    def parse(self, response):
        pass
