
1. Отредактировать new_hotels_crawl.py, установить стартовый URL
start_urls = ["https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&reestrFilter_924_VALUE=Республика+Саха+%28Якутия%29"]

2. Запустить crawl из директории /../../hotels_pages
scrapy crawl new_hotels -o respublica_saha.csv

