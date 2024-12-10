
import scrapy
import time


class SyrSpider(scrapy.Spider):
    name = "new_hotels"
    start_urls = ["https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&reestrFilter_924_VALUE=Республика+Саха+%28Якутия%29"]



    def parse(self, response):
        links = response.css("div.result-item ::attr('data-link')")
        for link in links:
            time.sleep(3)
            yield response.follow(link, self.parse_syr)
        link = response.xpath("//div[@class='result-pagination']/a/@href").get()
        yield response.follow(link, self.parse)


    def parse_syr(self, response):
        yield {
            'vid': response.xpath('//div[@class="card-info-block"]/div[1]/div[1]/p[2]/text()').get(),
            'polnoe_naimenovanie': response.xpath('//div[@class="card-info-block"]/div[1]/div[2]/p[2]/text()').get(),
            'socrshenoe_naimenovanie': response.xpath('//div[@class="card-info-block"]/div[1]/div[3]/p[2]/text()').get(),
            'naimenovanie_ur_litca_ip': response.xpath('//div[@class="card-info-block"]/div[1]/div[4]/p[2]/text()').get(),
            'region': response.xpath('//div[@class="card-info-block"]/div[1]/div[5]/p[2]/text()').get(),
            'inn': response.xpath('//div[@class="card-info-block"]/div[1]/div[6]/p[2]/text()').get(),
            'ogrn_ogrnip': response.xpath('//div[@class="card-info-block"]/div[1]/div[7]/p[2]/text()').get(),
            'adres': response.xpath('//div[@class="card-info-block"]/div[1]/div[8]/p[2]/text()').get(),
            'telephon': response.xpath('//div[@class="card-info-block"]/div[1]/div[9]/p[2]/text()').get(),
            'email': response.xpath('//div[@class="card-info-block"]/div[1]/div[10]/a/text()').get(),
            'sait': response.xpath('//div[@class="card-info-block"]/div[1]/div[11]/a/text()').get(),

            'spectialist_po_classificatci': response.xpath('//p[contains(text(), "Специалист по классификации")]/../p[2]/text()').get(),
            'prisvoenay_categoriya': response.xpath('//p[contains(text(), "Присвоенная категория")]/../p[2]/text()').get(),
            'nomer_resheniya_o_prisvoenii_categorii': response.xpath('//p[contains(text(), "Номер решения о присвоении категории")]/../p[2]/text()').get(),
            'data_resheniya_o_prisvoenii_categorii': response.xpath('//p[contains(text(), "Дата решения о присвоении категории")]/../p[2]/text()').get(),
            'registratcionnyi_nomer_svidetelstva': response.xpath('//p[contains(text(), "Регистрационный номер свидетельства")]/../p[2]/text()').get(),
            'data_vydachi_svidetelstva': response.xpath('//p[contains(text(), "Дата выдачи свидетельства")]/../p[2]/text()').get(),
            'srok_deistviya': response.xpath('//p[contains(text(), "Срок действия")]/../p[2]/text()').get()[3:],
            'acreditovanaya_organizatciya': response.xpath('//p[contains(text(), "Аккредитованная организация")]/../a/text()').get(),

            'categoria_1': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[1]/td[1]/text()').get(),
            'kol_vo_nomerov_categoria_1': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[1]/td[2]/text()').get(),
            'kol_vo_mest_categoria_1': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[1]/td[3]/text()').get(),

            'categoria_2': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[2]/td[1]/text()').get(),
            'kol_vo_nomerov_categoria_2': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[2]/td[2]/text()').get(),
            'kol_vo_mest_categoria_2': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[2]/td[3]/text()').get(),

            'categoria_3': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[3]/td[1]/text()').get(),
            'kol_vo_nomerov_categoria_3': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[3]/td[2]/text()').get(),
            'kol_vo_mest_categoria_3': response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[3]/td[3]/text()').get(),

            'itogo_nomerov': int(response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[1]/td[3]/text()').get() or 0) +
                                                   int(response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[2]/td[3]/text()').get() or 0) + 
                                                   int(response.xpath('//div[@class="card-info-block"]/div[3]/table/tbody/tr[3]/td[3]/text()').get() or 0),
        }