# Policy_crawler
爬取34个省份的公文数据。

**useful index**
scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0"

if contain ?, url must have ''.

**Jiangxi**

scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0" 'http://www.jiangxi.gov.cn/module/xxgk/subjectinfo.jsp?sortfield=compaltedate:0&fbtime=&texttype=0&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=2&binlay=&c_issuetime='

response.css('tr.tr_main_value_odd')[0].css('td a::attr()').getall()

response.css('div.bt-article-y')
response.css('div.bt-article-y')[0].css('tr td::text').getall()
response.css('div.bt-article-y')[0].css('tr td b::text').getall()
response.css('div.bt-article-y')[0].css('tr td b').text
response.css('div.bt-article-y')[0].css('tr td b')[0].text
response.css('div.bt-article-y')[0].css('tr td b::text').getall()
response.css('div.bt-article-y')[0].css('tr td b span::text').getall()
response.css('div.bt-article-y p.sp_title')
response.css('div.bt-article-y p.sp_title::text')
response.css('div.bt-article-y p.sp_title::text').get()
response.css('div.bt-article-y p.sp_title::text').data
response.css('div.bt-article-y p.sp_title::data')
response.css('div.bt-article-y p.sp_title::text')
response.css('div.bt-article-y p.sp_title::text').getall()
response.css('div.bt-article-y div#zoom').getall()
response.css('div.bt-article-y div#zoom')
response.css('div.bt-article-y div#zoom p')
response.css('div.bt-article-y div#zoom p::text')
response.css('div.bt-article-y div#zoom p::text').getall()
response.css('div.bt-article-y div#zoom p a::href').getall()
response.css('div.bt-article-y div#zoom p a::attr(href)').getall()

**Shanghai**
total page 1305

http://www.shanghai.gov.cn/nw2/nw2314/nw2319/nw12344/index.html

response.css('div.pageList')
response.css('ul.pageList')
response.css('ul.pageList li')
response.css('ul.pageList li')[0].css('span::text').get()
response.css('ul.pageList li')[0].css('a::attr(href)').get()
response.css('ul.pageList li')[0].css('a::attr(title)').get()

response.css('small.PBtime p::text').get()
response.css('small.PBtime p::text')
response.css('small.PBtime p')
response.css('small.PBtime')
response.css('small.PBtime p')
response.css('small.PBtime::text')
response.css('small.PBtime::text').get()
response.css('small.PBtime').get()
response.css('div#ivs_content').get()
response.css('div#ivs_content')
response.css('div#ivs_content p')
response.css('div#ivs_content p::text')
response.css('div#ivs_content p::text').getall()
response.css('ul.nowrapli')
response.css('ul.nowrapli')[0].text
response.css('ul.nowrapli')[0].get()
response.css('ul.nowrapli li')
response.css('ul.nowrapli li a')
response.css('ul.nowrapli li a::attr(tittle)')
response.css('ul.nowrapli li a::attr(title')
response.css('ul.nowrapli li a::attr(title)')
response.css('ul.nowrapli li a::attr(title)').getall()
response.css('ul.nowrapli li a::attr(href)').getall()

**Tianjin**

http://gk.tj.gov.cn/index_47.shtml

total page:7516

real_site:
http://gk.tj.gov.cn/govsearch/search.jsp?SType=1&page=3

In [4]: response.css('div.index_right_content ul li')[0].css('a::attr(href)').get()                                                                                               
Out[4]: 'http://gk.tj.gov.cn/gkml/000125014/202003/t20200316_87172.shtml'

In [5]: response.css('div.index_right_content ul li')[0].css('a::attr(title)').get()                                                                                              
Out[5]: '天津市人民政府关于李志荣等任职的通知'

In [6]: response.css('div.index_right_content ul li')[0].css('span.date1::text').get()                                                                                            
Out[6]: '索引号：000125014/2020-00025'

In [7]: response.css('div.index_right_content ul li')[0].css('span.date2::text').get()                                                                                            
Out[7]: '文号：津政人〔2020〕33号'

In [8]: response.css('div.index_right_content ul li')[0].css('span.date3::text').get()                                                                                            
Out[8]: '发文日期：2020年03月16日'

response.css('table.table_key').get()
response.css('table.table_key tr').get()
response.css('table.table_key tr')
response.css('table.table_key tr')[0]
response.css('table.table_key tr')[0].css('td *::text')
response.css('table.table_key tr')[0].css('td *::text').getall()
response.css('table.table_key tr')[0].css('td::text').getall()
response.css('table.table_key tr')[0].css('td *::text').getall()
response.css('table.table_key tr')[3].css('td *::text').getall()
response.css('div.TRS_PreAppend p::text').get()
response.css('div.TRS_PreAppend p *::text').get()
response.css('div.TRS_PreAppend p::text').getall()
response.css('div.TRS_PreAppend p 8::text').getall()
response.css('div.TRS_PreAppend p *::text').getall()