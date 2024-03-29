import scrapy

class PolicySpider(scrapy.Spider):
    name = "Policy"
    def start_requests(self):
        total_page = 20
        url_base = 'http://www.beijing.gov.cn/zhengce/zhengcefagui/index'
        for i in range(total_page):
            ref = '.html' if i == 0 else '_%s.html' % i 
            yield scrapy.Request(url=url_base + ref, callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for piece in response.css('div.listBox ul.list li'):
            href = piece.css('a::attr(href)').get()
            detail_page_links.append(href)
            UID = href.split('/')[-1][:-5]
            #response.follow(href, callbak = self.parse_content)
            yield {
                'UID': UID,
                'tittle': piece.css('a::text').get(),
                'date': piece.css('span::text').get(),
                'href': href,
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-5]
        doc_info_dict = {}
        container = response.css('div.container')[0]
        for doc_info in container.css('ol li'):
            doc_info_l = doc_info.css('::text').getall()
            if len(doc_info_l) == 2:
                key,value = doc_info_l
            elif len(doc_info_l) == 1:
                key = doc_info_l[0]
                value = ''
            doc_info_dict[key] = value
        full_tittle = container.css('div.header p::text').get()
        paragraph_list = container.css('div.mainTextBox p::text').getall()
        return {
            'UID': UID,
            'full_tittle': full_tittle,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
        }

