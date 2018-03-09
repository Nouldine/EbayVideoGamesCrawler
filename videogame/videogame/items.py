# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideogameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass

     # create fields for data needed for the csv file
    rating = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()

    
