import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class AnhuiSpider(scrapy.Spider):
    name = "Anhui"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 448
        # total_page = 3 
        url_base = 'http://www.ah.gov.cn/site/label/8888?IsAjax=1&dataType=html&_=0.42568734060518776&siteId=6781961&pageSize=16&pageIndex={0}&action=list&isDate=true&dateFormat=yyyy-MM-dd&length=46&organId=1681&type=4&catId=&cId=&result=%E6%9A%82%E6%97%A0%E7%9B%B8%E5%85%B3%E4%BF%A1%E6%81%AF&searchType=&keyWords=&specialCatIds=6708451%2C6708461%2C6708471&catIdExplainType=6711101tp_explain%2C6711111xwfbh_explain%2C6711121sp_explain%2C6711131ft_explain&labelName=publicInfoList&file=%2Fahxxgk%2FpublicInfoList-an-new'
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i+1), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for div in response.css('div.xxgk_navli'):
            url = response.urljoin(div.css('a::attr(href)').get())
            UID = url.split('/')[-1][:-5]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': div.css('a::attr(title)').get(),
                'date': div.css('span.date::text').get(),
                'FileNumber':None,
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-5]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        td_list = response.css('tbody')[0].css('td')
        th_list = response.css('tbody')[0].css('th')
        for i in range(len(th_list)):
            key = ''.join(th_list[i].css('::text').getall())
            value = ''.join(td_list[i].css('::text').getall())
            doc_info_dict[key] = value
        File_num = None
        if '文号：' in doc_info_dict.keys():
            File_num = doc_info_dict['文号：']
        paragraph_list =  response.css('div.wzcon p *::text').getall() 
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'FileNumber':File_num,
            'mainText': paragraph_list,
            'doc_info_dict':doc_info_dict,
            'crawl state':'full',
        }
