import scrapy
import pickle
import os

class TianjinSpider(scrapy.Spider):
    name = "Tianjin"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 7516
        #total_page = 3
        url_base = 'http://gk.tj.gov.cn/govsearch/search.jsp?SType=1&page={0}'
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(str(i+1)), callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for piece in response.css('div.index_right_content ul li'):
            href = piece.css('a::attr(href)').get()
            UID = href.split('/')[-1][:-6]
            detail_page_links.append(href)
            yield {
                'UID': UID,
                'title': piece.css('a::attr(title)').get(),
                'date': piece.css('span.date1::text').get(),
                'date2': piece.css('span.date2::text').get(),
                'date3': piece.css('span.date3::text').get(),
                'href': href,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-6]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        for line in response.css('table.table_key tr'):
            count = 0
            for td in line.css('td'):
                if count % 2 == 0:
                    key = td.css('*::text').get()
                else:
                    value = td.css('*::text').get()
                    doc_info_dict[key] = value
                count += 1
        FileNumber = ''
        if "文　　号：" in doc_info_dict.keys():
            FileNumber = doc_info_dict["文　　号："]
        paragraph_list = response.css('div.TRS_PreAppend p *::text').getall()
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
            'url':response.url,
            'crawl state':'full',
            'FileNumber' :FileNumber,
        }

