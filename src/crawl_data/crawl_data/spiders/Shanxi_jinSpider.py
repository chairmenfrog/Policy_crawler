import scrapy
import pickle
import os

class Shanxi_jinSpider(scrapy.Spider):
    name = "Shanxi_jin"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        total_page = 138
        # total_page = 3
        
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
            'Referer': "http://www.shanxi.gov.cn/sxszfxxgk/index.shtml",
        }
        url_base = "http://www.shanxi.gov.cn/sxszfxxgk/index{0}.shtml"
        for i in range(total_page):
            page = '_%s' % (i+1) if i >0 else ''
            yield scrapy.Request(url=url_base.format(page), headers =headers,callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        hrefs = response.css('table.affairs-document-box tr td.affaires-doc-title a::attr(href)').getall()
        filenums = response.css('table.affairs-document-box tr td.affaires-doc-sizes::text').getall()
        dates = response.css('table.affairs-document-box tr td.affaires-doc-published::text').getall()
        titles = response.css('table.affairs-document-box tr td.affaires-doc-title a.doc-title::attr(title)').getall()
        for i in range(len(hrefs)):
            url = hrefs[i]
            url = response.urljoin(url)
            UID = url.split('/')[-1][:-6]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': titles[i],
                'date': dates[i],
                'FileNumber': filenums[i],
                'url': url,
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('/')[-1][:-6]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        count = 0
        for td in response.css('table.affairs-detail-head td'):
            if count % 2 == 0:
                key = td.css('*::text').get()
            else:
                value = td.css('*::text').get()
                doc_info_dict[key] = value
            count+=1
        paragraph_list = response.css('div[style="FONT-SIZE: 16px; LINE-HEIGHT: 160%"] *::text').getall()
        pdf_links = [response.urljoin(response.css('div.article-body a::attr(href)').getall()[-1])]
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
            'attachment_links':pdf_links,
            'crawl state':'full',
        }

