# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem


class DangdangSpiderSpider(scrapy.Spider):
    name = 'dangdang_spider'
    allowed_domains = ['bang.dangdang.com']
    # start_urls = ['http://bang.dangdang.com/books/fivestars/1-1']
    def start_requests(self):
        for i in range(1,26):
            yield scrapy.Request('http://bang.dangdang.com/books/fivestars/1-' + str(i), callback=self.parse)

    def parse(self, response):
        # print(response.text)
        book_list = response.xpath('//div[@class="bang_list_box"]/ul/li')
        # print(book_list)
        ch1 = '（'
        ch2 = '('
        for book in book_list:
            dangdang_item = DangdangItem()
            serial = book.xpath('./div[1]/text()').extract_first()
            # print(serial[0])
            dangdang_item['serial'] = serial[:-1]
            name_raw = book.xpath('./div[@class="name"]/a/text()').extract_first()
            if name_raw.find(ch1) != -1:
                dangdang_item['name'] = name_raw[:name_raw.find(ch1)]
            elif name_raw.find(ch2) != -1:
                dangdang_item['name'] = name_raw[:name_raw.find(ch2)]
            else:
                dangdang_item['name'] = name_raw
            score_raw = book.xpath('./div[@class="star"]/span[@class="level"]/span/@style').extract_first()
            dangdang_item['score'] = float(score_raw[7:-2])
            dangdang_item['publisher'] = book.xpath('./div[6]/a/text()').extract_first()
            dangdang_item['price'] = book.xpath('./div[@class="price"]/p/span[@class="price_n"]/text()').extract_first()
            # print(dangdang_item['star'])
            yield dangdang_item

