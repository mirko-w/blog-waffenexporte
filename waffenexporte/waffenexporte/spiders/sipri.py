# -*- coding: utf-8 -*-
import scrapy,re
from scrapy.selector import Selector
from waffenexporte.items import WaffenexporteItem


class SipriSpider(scrapy.Spider):
    name = "sipri"
    allowed_domains = ["sipri.org"]
    start_urls = (
            'http://armstrade.sipri.org/armstrade/page/values.php',
    )

    def parse(self, response):
        values = response.xpath('//select[@name="country_code"]/option/@value').extract()
        names = response.xpath('//select[@name="country_code"]/option/text()').extract()
        name_val = zip(names, values)
        for n in name_val:
            request = scrapy.FormRequest(
                    'http://armstrade.sipri.org/armstrade/html/export_values.php',
                    formdata = {
                        'Action': 'Download',
                        'country_code': n[1],
                        'filetype': 'html',
                        'high_year': '2013',
                        'low_year': '1950',
                        'import_or_export': 'export',
                        'summarize': 'country'
                        },
                    callback = self.parse_data,
                    method = 'POST'
                    )
            request.meta['name'] = n[0]
            yield request

    def parse_data(self, response):
        ##from scrapy.shell import inspect_response
        ##inspect_response(response)
        sel = Selector(response)
        item = WaffenexporteItem()
        ## die Reihen mit den Daten auswaehlen
        data = sel.xpath('//tr')[12:-2]
        years = range(1950,2014)
        if data:
            for d in data:
                for i in range(64):
                    n = i+2
                    tiv = d.xpath('./td/text()')[n].extract()
                    if re.match('\d+', tiv):
                        item['supplier'] = response.meta['name']
                        item['recipient'] = d.xpath('./td[2]/text()').extract()
                        item['year'] = years[i]
                        item['tiv'] = tiv
                        yield item
