import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class HenanSpider(scrapy.Spider):
    name = "Henan"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        url_dict = {
            'http://wjbb.hnfzw.gov.cn/regulatory/viewQueryAll.do?offset={0}&cdid=402881fa2d1738ac012d173a60930017':369,
            'http://wjbb.hnfzw.gov.cn/rules/viewQueryAll.do?offset={0}&cdid=402881fa2d1738ac012d173a60930017':3
        }
        # test_page = 2
        for url_base, max_page in url_dict.items():
            for i in range(max_page):
                yield scrapy.Request(url=url_base.format(i*15), callback=self.parse)

    def parse(self,response):
        for a in response.css('div.serListCon a'):
            url = response.urljoin(a.css('::attr(href)').get())
            UID = url.split('/')[-1][:-4]
            title = a.css('::attr(title)').get()
            file_num = title.split('(')[-1]
            file_num = file_num.split('（')[-1][:-1]
            date = '-'.join(url.split('/')[-4:-1])
            yield {
                'UID': UID,
                'title': title,
                'date': date,
                'FileNumber':file_num,
                'url': url,
                'crawl state':'full',
                'mainText':[url]
            }

