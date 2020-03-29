import scrapy
import pickle
import os
import json

class CentralSpider(scrapy.Spider):
    name = "Central"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 2466
        # total_page = 3 
        url_base = 'http://sousuo.gov.cn/data?t=zhengcelibrary&q=&timetype=timeqb&mintime=&maxtime=&sort=pubtime&sortType=1&searchfield=title&pcodeJiguan=&childtype=&subchildtype=&tsbq=&pubtimeyear=&puborg=&pcodeYear=&pcodeNum=&filetype=&p={0}&n=5&inpro=&bmfl=&dup=&orpro='
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(i), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for item in json.loads(response.text)['searchVO']['catMap']['gongbao']['listVO']:
            url = item['url']
            UID = url.split('/')[-1][:-4]
            item['UID'] = UID
            item['date'] = item['pubtimeStr']
            item['FileNumber'] = item['wenhao']
            item['crawl state'] = 'half'
            detail_page_links.append(url)
            yield item
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-4]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        
        paragraph_list = response.css('div.pages_content p *::text').getall()        
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'mainText': paragraph_list,
            'crawl state':'full',
        }
