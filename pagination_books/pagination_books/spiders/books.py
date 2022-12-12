import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        # print(response.css('li.current ::text').get().strip())
        # print(response.xpath('//h3/a/text()').get().strip())
        print(response.xpath('//h3/a/@title').get().strip())

        next_link = response.css('li.next > a ::attr(href)').get()

        yield scrapy.Request(response.urljoin(next_link))
