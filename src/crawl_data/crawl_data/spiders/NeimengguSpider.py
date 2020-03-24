import scrapy
import pickle
import os

class NeimengguSpider(scrapy.Spider):
    name = "Neimenggu"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
            'Referer': "http://www.nmg.gov.cn/col/col1686/index.html",
            'Host':'www.nmg.gov.cn',
            'Origin':'http://www.nmg.gov.cn'
        }
        total_page = 119
        # total_page = 3
        url_base = "http://www.nmg.gov.cn/module/xxgk/search.jsp?infotypeId=&jdid=2&area=1115000001151201XD&divid=div1686&vc_title=&vc_number=&sortfield=compaltedate:0&currpage={0}&vc_filenumber=&vc_all=&texttype=&fbtime=&texttype=&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage={0}&sortfield=compaltedate:0&fields=&fieldConfigId=&hasNoPages=&infoCount="
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(str(i+1)),headers=headers, callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for sign in ['odd','even']:
            for piece in response.css('tr.tr_main_value_%s' % sign):
                url = piece.css('td a::attr(href)').get()
                UID = url.split('/')[-1][:-5]
                detail_page_links.append(url)
                yield {
                    'UID': UID,
                    'title': piece.css('td a::attr(title)').get(),
                    'date': piece.css('td[width="120"]::text').get(),
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
        for td in response.css('table.xxgk_table td'):
            if count % 2 == 0:
                key = td.css('*::text').get()
            else:
                value = td.css('*::text').get()
                doc_info_dict[key] = value
            count+=1
        filenum = doc_info_dict['文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号'] if '文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号' in doc_info_dict.keys() else ''
        paragraph_list = response.css('div#zoom p *::text').getall()
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'doc_info_dict': doc_info_dict,
            'FileNumber':filenum,
            'mainText': paragraph_list,
            'crawl state':'full',
        }

