# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviedataItem(scrapy.Item):
    # define the fields for your item here like:
    actor_name = scrapy.Field()
    actor_bio = scrapy.Field()
    movie_name = scrapy.Field()
    actor_imagelink = scrapy.Field()
    pass

class ActordataItem(scrapy.Item):
    # define the fields for your item here like:
    actor_name = scrapy.Field()
    actor_born = scrapy.Field()
    actor_bio = scrapy.Field()
    actor_height = scrapy.Field()
    actor_imagelink = scrapy.Field()
    actor_nickname = scrapy.Field()
    pass