# -*- coding: utf-8 -*-

#Author: Abdoul-Nourou Yigo

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# get Video VideogameItem from the items class 
from videogame.items import VideogameItem

#CrawlSpider
class VideogamesSpider( CrawlSpider ):

    name = 'videogames'
	
    allowed_domains = ['www.ebay.com']

	# Main URL to start the scripting from
    start_urls = [

                'https://www.ebay.com/b/Video-Games/139973?Platform=Nintendo%2520Switch%7CSony%2520PlayStation%25204%7CMicrosoft%2520Xbox%2520One%7CPC&rt=nc&_fsrp=0&_pgn=3&_sacat=139973'
                

            ]

	# This rule is used to got through URLs that contains this format
    rules = (

            Rule( LinkExtractor( allow=(r'Video-Games/139973?')),

                callback = 'parse_item',
                
                follow = True


                ),
            
            )

	# This function is used to extract data 
	# from the html content 
    def parse_item(self, response):
        
	# Create a item object from 
	# item class
	item = VideogameItem()

	# get the item name from the html content 
	name = response.css('.s-item__title::text').extract_first()
	
	# get the price from the html
	price = response.css('.s-item__price::text').extract()[0].strip()

	# get customer rating from the html content
	rating = response.css('span.b-starrating__star > span.clipped::text').extract()[0].strip()
	
	# pass the items to the item object
        item['rating'] = rating
        item['price'] = price
        item['name'] = name


        yield item














