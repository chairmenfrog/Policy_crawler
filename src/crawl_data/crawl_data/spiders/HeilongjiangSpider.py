import scrapy
import pickle
import os
import ast
from urllib import parse
from scrapy.selector import Selector

class HeilongjiangSpider(scrapy.Spider):
    name = "Heilongjiang"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 6389
        url_base = 'http://gkml.dbw.cn/gkml/web/data/ztfl.ashx?s=20&p={0}&c=1&k=&t='
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(str(i+1)), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        detail_url_base = 'http://gkml.dbw.cn/gkml/web/data/detail.ashx?t=2&d={0}'
        for piece_dict in ast.literal_eval(response.text[25:-29])['data']:
            UID = piece_dict['ID']
            piece_dict['UID'] =  UID
            piece_dict['date'] = piece_dict['time']
            detail_page_links.append(detail_url_base.format(UID))
            piece_dict['crawl state'] = 'half'
            yield piece_dict
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('=')[-1]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        paragraph_list = []
        new_text = parse.unquote_plus(response.text[7:-6])
        for escape_text in Selector(text=new_text).css('div.zwnr *::text').getall():
            paragraph = escape_text.replace("%","\\").encode("utf-8").decode("unicode_escape") 
            paragraph_list.append(paragraph)
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
