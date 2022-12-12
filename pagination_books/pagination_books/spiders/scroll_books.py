import scrapy
import scraper_helper as sh

base = 'http://quotes.toscrape.com/api/quotes?page={}'
class ScrollBooksSpider(scrapy.Spider):
    name = 'scroll_books'
    start_urls =[base.format(1)]
    
    def parse(self, response):
        data = response.json()
        #print (data['quotes']) 
        for quote in data['quotes']:
            yield {
                'Author': quote['author']['name'],
                'Quote': sh.cleanup(quote['text'])
            }
        current_page = data['page']
        if data['has_next']:
            next_page_url = base.format(current_page + 1 )
            yield scrapy.Request(next_page_url)