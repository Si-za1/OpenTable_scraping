# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class OpentableItem(scrapy.Item):
	name = scrapy.Field()
	area = scrapy.Field()
	price = scrapy.Field()
	location = scrapy.Field()
	cuisine = scrapy.Field()
	review_count = scrapy.Field()
	promoted = scrapy.Field()
	address = scrapy.Field()