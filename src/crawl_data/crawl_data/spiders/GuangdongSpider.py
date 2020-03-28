import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class GuangdongSpider(scrapy.Spider):
    name = "Guangdong"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 205
        # total_page = 3 
        url_base = 'http://www.gd.gov.cn/zwgk/wjk/qbwj/index{0}.html'
        for i in range(total_page):
            page = '_'+ str(i+1) if i > 0 else ''
            yield scrapy.Request(url=url_base.format(page), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for li in response.css('div.viewList ul li'):
            url = response.urljoin(li.css('a::attr(href)').get())
            UID = url.split('/')[-1][:-5]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': li.css('a::text').get(),
                'date': li.css('span.date::text').get(),
                'FileNumber':li.css('span.wh::text').get(),
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-5]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        paragraph_list = response.css('div.zw p *::text').getall() 
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
