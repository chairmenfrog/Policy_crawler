import scrapy
import pickle
import os

class HebeiSpider(scrapy.Spider):
    name = "Hebei"
    if not os.path.exists('../../data/HTML_pk/%s' % name):
        os.makedirs('../../data/HTML_pk/%s' % name)
    if not os.path.exists('../../data/text/%s' % name):
        os.makedirs('../../data/text/%s' % name)
    def start_requests(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
            'Referer': "http://info.hebei.gov.cn/eportal/ui?pageId=6817552"
        }
        total_page = 83
        # total_page = 3
        url_base = 'http://info.hebei.gov.cn/eportal/ui?pageId=6817552&currentPage={0}&moduleId=3bb45f8814654e33ae014e740ccf771b&formKey=GOV_OPEN&columnName=EXT_STR7&relationId='
        for i in range(total_page):
            yield scrapy.Request(url=url_base.format(str(i+1)),headers=headers, callback=self.parse)

    def parse(self,response):
        detail_page_links = []
        for piece in response.css('table.xxgkzclbtab3'):
            url = response.urljoin(piece.css('td a::attr(href)').get())
            UID = url.split('=')[-2].split('&')[0]
            detail_page_links.append(url)
            yield {
                'UID': UID,
                'title': piece.css('td a::text').get(),
                'date': piece.css('td[align="center"][width="150"]::text').get(),
                'url': url,
                'FileNumber':piece.css('td[align="left"]::text').get(),
                'crawl state':'half'
            }
        yield from response.follow_all(detail_page_links, callback = self.parse_content)

    def parse_content(self, response):
        UID = response.url.split('=')[-2].split('&')[0]
        with open('../../data/HTML_pk/%s/%s.pkl' % (self.name,UID), 'wb') as f:
            pickle.dump(response.text,f)
        doc_info_dict = {}
        count = 0
        for td in response.css('div.xxgk_bmxl td'):
            if count % 2 == 0:
                key = td.css('*::text').get()
            else:
                value = td.css('*::text').get()
                doc_info_dict[key] = value
            count+=1
        paragraph_list = response.css('div#zoom div *::text').getall()
        with open('../../data/text/%s/%s.txt' % (self.name,UID), 'w') as f:
            f.write('\n'.join(paragraph_list))
        return {
            'UID': UID,
            'doc_info_dict': doc_info_dict,
            'mainText': paragraph_list,
            'crawl state':'full',
        }

