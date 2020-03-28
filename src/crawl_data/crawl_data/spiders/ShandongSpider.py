import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class ShandongSpider(scrapy.Spider):
    name = "Shandong"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 5835
        # total_page = 3 
        url_base = 'http://www.shandong.gov.cn/module/xxgk/search_custom.jsp?fields=&fieldConfigId=247732&sortfield=compaltedate:0&fbtime=&texttype=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage={0}&binlay=&c_issuetime='

        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i+1), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for div in response.css('div.wip_lists'):
            url = div.css('a::attr(href)').get()
            UID = url.split('/')[-1][:-16]
            detail_page_links.append(url)
            date = '-'.join(url.split('/')[-4:-1])
            yield {
                'UID': UID,
                'title': div.css('a::text').get(),
                'date': date,
                'FileNumber':None,
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-16]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)

        paragraph_list = response.css('div.wip_art_con p *::text').getall()
        if len(paragraph_list) == 0:
            paragraph_list = response.css('div#zoom p *::text').getall()
        if len(response.css('div.wip_art_con p')) >= 2:
            File_num = response.css('div.wip_art_con p')[1].css('::text').get()
        else:
            File_num = None
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'FileNumber':File_num,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
