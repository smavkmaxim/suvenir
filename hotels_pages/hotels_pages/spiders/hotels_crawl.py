import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HotelsCrawlSpider(CrawlSpider):
    name = 'hotels-crawl'
    #allowed_domains = ['tourism.gov.ru']
    start_urls = ['https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya']

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css="div.result-item ::attr('data-link')"), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths="//div[@class='result-pagination']/a/@href"))
    )

    def parse_item(self, response):
        print("111111111111111111111111111111111:wq")
        item = {}
        item['vid'] = response.xpath('//div[@class="card-info-block"]/div[1]/p[2]/text()').get()    
        #item['name'] = response.xpath('//div[@class="card-info-block"]/div[2]/p[2]/text()').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
