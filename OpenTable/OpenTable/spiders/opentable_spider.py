import scrapy
from OpenTable.items import OpentableItem

class OpentableSpiderSpider(scrapy.Spider):
    name = 'opentable_spider'
    #allowed_urls = ['https://www.opentable.com']
    start_urls = ['https://www.opentable.com/api/v1/cities/new-york-ny/restaurants/?sort=bestMatches']

   
    def parse(self, response):
        rows = response.xpath('//*[@id="mainContent"]/div/div')
        area = "New York"  # we are scraping only New York restaurants, so area 

        for row in rows:
            name = row.xpath('//span[@class="rest-row-name-text"]/text()').extract_first()
            location = row.xpath('//span[@class="Sxd1R5Ec4LTXhBThEBvw DUkDy8G7CgNvYcWgJYPN A1IRrGEyp8xe7pseBxZd"]').extract_first()
            price = row.xpath('//h5[@id="prices-title"]').extract_first()
            cuisine = row.xpath('//div[3]/div//text()').extract_first()
            review_count = row.xpath('//a//span[@class="underline-hover"]//text()').extract_first()
            promoted = row.xpath('//div[1]/span//text()').extract_first()

            item = OpentableItem()
            item['name'] = name
            item['area'] = area
            item['price'] = price
            item['location'] = location
            item['cuisine'] = cuisine
            item['review_count'] = review_count
            item['promoted'] = promoted

            yield item


# import scrapy

# class OpentableSpiderSpider(scrapy.Spider):
#     name = 'opentable_spider'

#     def start_requests(self):
#         url = 'https://www.opentable.co.uk/new-york-restaurant-listings'
#         yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         restaurants = response.json()
#         for restaurant in restaurants['results']:
#             title = restaurant['name']
#             yield {'title': title}



