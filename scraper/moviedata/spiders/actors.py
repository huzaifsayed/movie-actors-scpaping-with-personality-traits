# -*- coding: utf-8 -*-
import scrapy
from ..items import ActordataItem

class ActorsSpider(scrapy.Spider):
    name = 'actors'
    allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/list/ls068010962/']
    base_url = 'https://www.imdb.com'

    def parse(self, response):
        all_actors = response.css('div.mode-detail')

        for actor in all_actors:

            clean_url = actor.css('h3.lister-item-header a::attr(href)').extract_first().replace('?ref_=nmls_hd', '/bio?ref_=nm_ov_bio_sm') 
            actor_url = self.base_url + clean_url
            
            yield scrapy.Request(actor_url, callback=self.parse_actor)

        next_page = response.css('div.list-pagination a.next-page::attr(href)').get()
        if next_page != '#':
            yield response.follow(next_page, callback = self.parse)

    def parse_actor(self, response):

        item = ActordataItem()

        actor_name = response.css('.parent a::text').extract_first()
        actor_born = response.xpath("//table[@id='overviewTable']/tr[1]/td[2]//time/@datetime").extract_first()
        actor_nickname = response.xpath("//table[@id='overviewTable']/tr[2]/td[2]/text()").extract()
        actor_height = response.xpath("//table[@id='overviewTable']/tr[3]/td[2]/text()").extract_first()
        actor_bio = response.css('.odd p:nth-child(1)::text').extract()
        actor_imagelink = response.css('.poster::attr(src)').extract_first()
        item['actor_name'] = actor_name
        item['actor_born'] = actor_born
        item['actor_nickname'] = actor_nickname
        item['actor_bio'] = actor_bio
        item['actor_height'] = actor_height
        item['actor_imagelink'] = actor_imagelink

        yield item