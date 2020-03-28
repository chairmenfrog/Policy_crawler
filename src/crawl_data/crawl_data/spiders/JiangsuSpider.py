import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class JiangsuSpider(scrapy.Spider):
    name = "Jiangsu"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
            'Referer': "http://www.jiangsu.gov.cn/col/col76841/index.html?uid=297589&pageNum=3",
            "Host": "www.jiangsu.gov.cn",
            "Origin":"http://www.jiangsu.gov.cn"
        }

        total_page = 190
        # total_page = 2
        # url_base = "http://www.jiangsu.gov.cn/module/web/jpage/dataproxy.jsp?col=1&appid=1&webid=1&path=%2F&columnid=76841&sourceContentType=1&unitid=297589&webname=%E6%B1%9F%E8%8B%8F%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&permissiontype=0"
        url_base = 'http://www.jiangsu.gov.cn/col/col76841/index.html?uid=297589&pageNum={0}&col=1&appid=1&webid=1&path=%2F&columnid=76841&sourceContentType=1&unitid=297589&webname=%E6%B1%9F%E8%8B%8F%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&permissiontype=0'
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i+1),headers=headers, callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for record in Selector(text = response.css('div#297589 *::text').get()).css('record'):
            url = record.css('a::attr(href)').get()
            detail_page_links.append(url)
            UID = url.split('/')[-1][:-5]
            yield {
                'UID': UID,
                'title': record.css('a::attr(title)').get(),
                'date': record.css('b::text').get(),
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
        count = 0
        for td in response.css('tbody td'):
            if count % 2 == 0:
                key = td.css("::text").get()
            else:
                value = td.css("::text").get()
                doc_info_dict[key] = value
            count+=1
        file_num = doc_info_dict['文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号'] if '文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号' in doc_info_dict.keys() else  None
        paragraph_list = response.css('div#zoom p *::text').getall() 
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'FileNumber': file_num,
            'crawl state':'full',
        }
