import scrapy
import pickle
import os

class JiangxiSpider(scrapy.Spider):
    name = "Jiangxi"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 106
        url_base = 'http://www.jiangxi.gov.cn/module/xxgk/subjectinfo.jsp?sortfield=compaltedate:0&fbtime=&texttype=0&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage={0}&binlay=&c_issuetime='
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(str(i+1)), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for piece in response.css('tr.tr_main_value_odd'):
            href = piece.css('td a::attr(href)').get()
            UID = href.split('/')[-1]
            UID = UID.split('?')[0][:-5]
            detail_page_links.append(href)
            yield {
                'UID': UID,
                'docID': piece.css('td a::attr(syh)').get(),
                'title': piece.css('td a::attr(mc)').get(),
                'date': piece.css('td a::attr(rq)').get(),
                'href': href,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1]
        UID = UID.split('?')[0][:-5]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        values = response.css('div.bt-article-y')[0].css('tr td::text').getall()
        keys = response.css('div.bt-article-y')[0].css('tr td b span::text').getall() +\
           response.css('div.bt-article-y')[0].css('tr td b::text').getall()
        doc_info_dict = {}
        if len(keys) == len(values):
            for i in range(len(keys)):
                doc_info_dict[keys[i]] = values[i]
        
        full_tittle = ''.join(response.css('div.bt-article-y p.sp_title::text').getall())
        paragraph_list = response.css('div.bt-article-y div#zoom p::text').getall()
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        attachment_link = response.css('div.bt-article-y div#zoom p a::attr(href)').getall()
        attachment_link = [link for link in attachment_link if link[:16]=='/module/download']
        return {
            'UID': UID,
            'full_tittle': full_tittle,
            'url':response.url,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
            'attachment_link': attachment_link,
            'crawl state':'full',
        }

