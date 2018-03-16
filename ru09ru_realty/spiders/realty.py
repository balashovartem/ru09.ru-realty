# -*- coding: utf-8 -*-
import scrapy
import logging


class RealtySpider(scrapy.Spider):
    name = 'realty'
    allowed_domains = ['www.tomsk.ru09.ru']
    start_urls = ['http://www.tomsk.ru09.ru/realty']

    def parse(self, response):
        pass
