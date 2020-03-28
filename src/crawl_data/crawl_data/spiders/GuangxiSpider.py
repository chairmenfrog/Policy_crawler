import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class GuangxiSpider(scrapy.Spider):
    name = "Guangxi"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 163
        # total_page = 3 
        url_base = 'http://fun.gxzf.gov.cn/php/index.php?c=file&pageno={0}'
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i+1), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        tr_list = response.css('ul.more-list tr')[1:]
        for i in range(len(tr_list)//4):
            url = response.urljoin(tr_list[4*i].css('a::attr(href)').get())
            UID = url.split('=')[-1]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': tr_list[4*i].css('a::text').get(),
                'date': tr_list[4*i].css('td')[-2].css('::text').get(),
                'FileNumber':tr_list[4*i].css('td')[-4].css('::text').get(),
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('=')[-1]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        paragraph_list = response.css('div.article-con p *::text').getall()         
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
