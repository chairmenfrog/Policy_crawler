import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class XinjiangSpider(scrapy.Spider):
    name = "Xinjiang"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 34
        # total_page = 3 
        url_base = 'http://www.xinjiang.gov.cn/xinjiang/gfxwj/zfxxgk_gknrz{0}.shtml'
        for i in range(total_page):
            page = '_'+ str(i+1) if i > 0 else ''
            yield scrapy.Request(url=url_base.format(page), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for dd in response.css('div.gknr_list dd'):
            url = response.urljoin(dd.css('a::attr(href)').get())
            UID = url.split('/')[-1][:-6]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': dd.css('a::attr(title)').get(),
                'date': dd.css('span::text').get(),
                'FileNumber':None,
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-6]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        for li in response.css('ul.clearfix li'):
            tmp_l = li.css('*::text').getall()
            if len(tmp_l) == 2:
                doc_info_dict[tmp_l[0]] = tmp_l[1]
            else:
                tmp_l = tmp_l[0].split('：')
                if len(tmp_l) == 2:
                    doc_info_dict[tmp_l[0]] = tmp_l[1]
        File_num = None
        if '发文字号' in doc_info_dict.keys():
            File_num = doc_info_dict['发文字号']
        paragraph_list = response.css('div.gknbxq_detail p *::text').getall()        
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'FileNumber':File_num,
            'mainText': paragraph_list,
            'doc_info_dict':doc_info_dict,
            'crawl state':'full',
        }
