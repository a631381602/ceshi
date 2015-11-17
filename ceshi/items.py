# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CeshiItem(scrapy.Item):
	rank = scrapy.Field()
	title = scrapy.Field()
	lading = scrapy.Field()
	time = scrapy.Field()
	size = scrapy.Field()
	query = scrapy.Field()
	update = scrapy.Field()
	CLASS = scrapy.Field()