
import scrapy
import time


class SyrSpider(scrapy.Spider):
    name = "new_hotels2"
    start_urls = ["https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&reestrFilter_924_VALUE=%D0%9F%D1%80%D0%B8%D0%BC%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B9+%D0%BA%D1%80%D0%B0%D0%B9&PAGEN_1=1"]

    def parse(self, response):
        links = response.css("div.result-item ::attr('data-link')")
        for i in range(1,43):
            print(links.get())
            for link in links:
                #time.sleep(3)
                yield response.follow(link, self.parse_syr)
            links = response.xpath("//div[@class='result-pagination']/a")
            print(f'--------------------{link}-----------------------------')
       # yield response.follow(link, self.parse)

    def parse_syr(self, response):
        yield {
            'vid': response.xpath('//div[@class="card-info-block"]/div[1]/div[2]/p[2]/text()').get(),
            #vid = response.xpath('//div[@class="card-info-block"]/div[1]/div[1]/p[2]/text()'),
            #print(vid),
            #"name": response.css("div.row h1::text").get(),
            #"price": response.css("div.col-sm-6 span::text").get(),
            #"nal": response.css("div.product-description b::text").get(),
        }
