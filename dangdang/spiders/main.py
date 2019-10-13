from scrapy import cmdline
cmdline.execute('scrapy crawl dangdang_spider -o book.json -s FEED_EXPORT_ENCODING=UTF-8'.split())
