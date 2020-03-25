import pickle
import os
import scrapy

class Shaanxi_shanSpider(scrapy.Spider):
    name = "Shaanxi_shan"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        url_dict = {
            'http://www.shaanxi.gov.cn/info/iList.jsp?node_id=GKszfbgt&file_head=%E9%99%95%E8%A5%BF%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C%E4%BB%A4&tm_id=69&cur_page={0}':10,
            'http://www.shaanxi.gov.cn/info/iList.jsp?node_id=GKszfbgt&file_head=%E9%99%95%E6%94%BF%E5%8A%9E%E5%8F%91&tm_id=69&cur_page={0}':146,
            'http://www.shaanxi.gov.cn/info/iList.jsp?node_id=GKszfbgt&file_head=%E9%99%95%E6%94%BF%E5%8F%91&tm_id=385&cur_page={0}':75,
            'http://www.shaanxi.gov.cn/info/iList.jsp?node_id=GKszfbgt&file_head=%E9%99%95%E6%94%BF%E5%8A%9E%E5%8F%91%E6%98%8E%E7%94%B5&tm_id=69&cur_page=2':14,
        }
        #test_page = 2
        for url_base, max_page in url_dict.items():
            for i in range(max_page):
                yield scrapy.Request(url=url_base.format(i+1), callback=self.parse)

    def parse(self,response):
        detail_page_links=[]
        for tr in response.css('table.gk_list_table tr')[1:]:
            href = tr.css('a::attr(href)').get()
            url = response.urljoin(href)
            UID = href.split('/')[-1]
            if UID[:5] == 'iList':
                UID =  UID.split('=')[-1]
                type_ = 'jsp'
            else:
                UID = UID[:-4]
                type_ = 'htm'
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'type':type_,
                'title': tr.css('a::attr(title)').get(),
                'date': tr.css('td[align="center"]::text').get(),
                'FileNumber': tr.css('td.textCenter::text').get(),
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1]
        if UID[:5] == 'iList':
            UID =  UID.split('=')[-1]
        else:
            UID = UID[:-4]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        count = 0
        td_list = response.css('div.zfwj_news_table tr td')
        if len(td_list) == 0:
             td_list = response.css('div.gk_news_table tr td')   
        for td in td_list:
            if count % 2 == 0:
                key = td.css('*::text').get()
            else:
                value = td.css('*::text').get()
                doc_info_dict[key] = value
            count+=1
        paragraph_list = response.css('div#info_content p *::text').getall()
        attach = response.css('div.xzfwj_rig a[href$=".pdf"]::attr(href)').get()
        attach = response.urljoin(attach)
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
            'attachment_links': attach,
            'crawl state':'full',
        }

