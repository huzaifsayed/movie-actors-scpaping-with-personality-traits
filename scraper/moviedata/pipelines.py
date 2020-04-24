# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class MoviedataPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('database/movie_actor_data.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS actor_tb""")
        self.curr.execute("""CREATE TABLE actor_tb(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    actor_name TEXT,
                                    actor_born TEXT,
                                    actor_bio TEXT,
                                    actor_height TEXT,
                                    actor_nickname TEXT,
                                    actor_imagelink TEXT                           
                                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        actor_bio = ' '.join(map(str, item['actor_bio']))
        actor_nickname = ' '.join(map(str, item['actor_nickname']))

        self.curr.execute("""INSERT INTO actor_tb (actor_name,actor_born,actor_bio,actor_height,actor_nickname,actor_imagelink) VALUES (?,?,?,?,?,?)""",(
            item['actor_name'] or 'Not Found',
            item['actor_born'] or 'Not Found',
            actor_bio or 'Not Found',
            item['actor_height'] or 'Not Found',
            actor_nickname or 'Not Found',
            item['actor_imagelink'] or 'Not Found'
        ))
        
        self.conn.commit()
