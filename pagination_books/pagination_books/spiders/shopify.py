import scrapy
import math

class ShopifySpider(scrapy.Spider):
    name = 'shopify'
    start_urls = ['https://techinstr.myshopify.com/collections/all']

    def parse(self, response):
        raw = response.css('.filters-toolbar__product-count::text').get()
        total_count = int(raw.replace('products', ''))
        total_pages = math.ceil(total_count/8)
        print ('Total', total_pages)
        # header = {
        #     'accept': '*/*',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
        #     'referer': 'https://techinstr.myshopify.com/collections/all',
        #     'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'same-origin',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        # }
        # yield {
        #     'products': response.css('.grid-view-item__link > span::text').getall()
        # }
        for i in range(2, total_pages+1):
            url = 'https://techinstr.myshopify.com/collections/all?page={}'.format(i)
            yield scrapy.Request(url, callback=self.parse_api)
    
    def parse_api(self, response):
        yield {
            'products': response.css('.grid-view-item__link > span::text').getall()
        }