import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class SichuanSpider(scrapy.Spider):
    name = "Sichuan"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 716
        # total_page = 3 
        url_base = 'http://www.sc.gov.cn/zcwj/default.aspx?p={0}&gpiid=&dept=6'
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i+1), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for tr in response.css('table')[1].css('tr')[1:]:
            url = response.urljoin(tr.css('td')[1].css('a::attr(href)').get())
            UID = url.split('=')[-1]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': tr.css('td')[1].css('a::attr(title)').get(),
                'date': tr.css('td')[2].css('::text').get(),
                'FileNumber':tr.css('td')[3].css('::text').get(),
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('=')[-1]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        paragraph_list = response.css('td p *::text').getall()
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
