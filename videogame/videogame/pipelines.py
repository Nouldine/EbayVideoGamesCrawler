# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
import csv


#ITEM_PIPELINES = {

        #'videogame.pipelines.VideogamePipeline': 300,


        #}


class VideogamePipeline(object):

    def process_item(self, item, spider):
                
        return item

