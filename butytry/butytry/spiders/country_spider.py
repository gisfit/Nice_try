import scrapy
import pprint


def prn_obj(obj):
  print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


class CountrySpider(scrapy.Spider):
    name = "country"

    def start_requests(self):
        urls = [
            'http://data.stats.gov.cn/easyquery.htm?cn=C01',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        print("*"*100)
        print(response.url)
        print("*"*100)
        print(response.body)
        print("$"*100)
        pprint.pprint(response.__dict__.items())
        print("$"*100)

        filename = 'country-stat.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
