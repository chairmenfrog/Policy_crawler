# Policy_crawler
爬取34个省份的公文数据。

**add splash**

pip install scrapy-splash
sudo apt  install docker.io
docker pull scrapinghub/splash
docker run -p 8050:8050 scrapinghub/splash


**useful index**

scrapy shell -s USER_AGENT="Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0"

if contain ?, url must have ''.

next_page = response.urljoin(next_page)

>>> from scrapy.selector import Selector
>>> body = '<html><body><span>good</span></body></html>'
>>> Selector(text=body).xpath('//span/text()').get()

js escape编码 https://www.cnblogs.com/yoyoketang/p/8058873.html

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://service.shanghai.gov.cn/pagemore/iframePagerIndex_12344_2_22.html?objtype=&nodeid=&pagesize=&page=13"
}

**Jiangxi**

total page 106

"文      号:"

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

"mainText" [0]

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

'date2'文号
'date3'发文日期

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


**Chongqing**

不爬取市政府内部细分部门文件和已经废止和失效的文件

doc_info_dict
"文 号："

content_list:
http://www.cq.gov.cn/zwgk/fdzdgknr/lzyj/zfgz/zfgz_52609/index_11.html
http://www.cq.gov.cn/zwgk/fdzdgknr/lzyj/xzgfxwj/szf_38655/index_22.html
http://www.cq.gov.cn/zwgk/fdzdgknr/lzyj/xzgfxwj/szfbgt_38656/index_32.html
http://www.cq.gov.cn/zwgk/fdzdgknr/lzyj/qtgw/index_33.html
http://www.cq.gov.cn/zwgk/fdzdgknr/lzyj/rsrm/index_2.html

response.css('ul.list-cont')
response.css('ul.list-cont li.w120')
len(response.css('ul.list-cont li.w120'))
len(response.css('ul.list-cont li.w400'))
len(response.css('ul.list-cont li.w172'))
len(response.css('ul.list-cont li.w110'))
response.css('ul.list-cont li.w120::text').getall()
response.css('ul.list-cont li.w400 a::text').getall()
response.css('ul.list-cont li.w172::text').getall()
response.css('ul.list-cont li.w110 span::text').getall()
response.css('ul.list-cont li.w400 a::attr(href)').getall()


response.text
response.css('table.gkxl-top')
response.css('table.gkxl-top td')
response.css('table.gkxl-top td::text').getall()
len(response.css('table.gkxl-top td::text').getall())
response.css('table.gkxl-top td').getall()
len(response.css('table.gkxl-top td').getall())
response.css('table.gkxl-top td').getall()[-1].get()
response.css('table.gkxl-top td').[-1].get()
response.css('table.gkxl-top td')[-1].get()
response.css('table.gkxl-top td')[-1].css('::text').get()
type(response.css('table.gkxl-top td')[-1].css('::text').get())
{'2':2}
{'2':response.css('table.gkxl-top td')[-1].css('::text').get()}
response.css('div.gkxl-article p *::text').getall()

**Heilongjiang**

http://www.hlj.gov.cn/gkml/ztfl.html?p=1&c=1&k=&t=

total_page 6398

http://gkml.dbw.cn/gkml/web/data/ztfl.ashx?s=20&p=6398&c=1&k=&t=

http://gkml.dbw.cn/gkml/web/data/detail.ashx?t=2&d=175185


In [5]: ast.literal_eval(response.text[25:-29])['data'][0]                                                                                                                        
Out[5]: 
{'title': '司法行政法制工作规定',
 'url': 'http://www.hlj.gov.cn/gkml/detail.html?t=2&d=175325',
 'time': '1990年8月18日',
 'IndexNumber': '001697444\x814-00546',
 'Name': '省司法厅',
 'longtitle': '司法行政法制工作规定',
 'Fenlei': '公安、安全、司法',
 'FileNumber': '司法部令第10号',
 'SubjectIterms': '',
 'number': '1',
 'ID': '175325'}

response.text[8:-6]
from scrapy.selector import Selector
Selector(text=response.text[8:-6]).css('div.zwnr').get()
Selector(text=response.text[8:-6]).css('div.zwnr')
Selector(text=response.text[8:-6]).css('div')
Selector(text=response.text[7:-6]).css('div')
response.text[7:-6]
from urllib import parse
new_text = parse.unquote_plus(response.text[7:-6])
new_text
Selector(text=new_text).css('div')
Selector(text=new_text).css('div.zwnr')
Selector(text=new_text).css('div.zwnr *::text').getall()
parse.unqote_plus(Selector(text=new_text).css('div.zwnr *::text').getall()[0])
parse.unquote_plus(Selector(text=new_text).css('div.zwnr *::text').getall()[0])
new_text
parse.unquote(Selector(text=new_text).css('div.zwnr *::text').getall()[0])
parse.quote(Selector(text=new_text).css('div.zwnr *::text').getall()[0])
new_text.decode('unicode_escape')
decode(new_text,'unicode_escape')
'苏'.encode('unicode_escape')
response.body
response.body.decode.('unicode_escape')
response.body.decode('unicode_escape')
urllib.unquote(response.body.decode('unicode_escape'))
parse.unquote(response.body.decode('unicode_escape'))
Selector(text=new_text).css('div.zwnr *::text').getall()[0].replace("%","\\")
Selector(text=new_text).css('div.zwnr *::text').getall()[0].replace("%","\\").encode("utf-8").decode("unicode_escape")



**Jilin**

total page 173

http://infogate.jl.gov.cn/govsearch/jsonp/zf_jd_list.jsp?page=6&lb=134657&callback=result&sword=&searchColumn=all&searchYear=all&pubURL=http%3A%2F%2Fxxgk.jl.gov.cn%2F&SType=1&searchColumnYear=all&searchYear=all&pubURL=&SType=1&channelId=134657&_=1585041673815

response.text
import json
len('\r\n\r\n\r\n\r\n\r\n\r\n\ufeff\r\n\r\n\r\n\r\n\r\n  \r\n \r\n\r\n\r\n\r\n\r\n  \r\n \r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nresult(')
len(');\r\n')
json.loads(response.text[67:-4])
response.text[67:-4]
response.text[66:-4]
json.loads(response.text[66:-4])
json_dict = json.loads(response.text[66:-4])
json_dict['data']
json_dict['data'][0]['puburl']
json_dict['data'][0]['MetaDataId']
json_dict['data'][0]['tip']['dates']
json_dict['data'][0]['tip']['filenum']
json_dict['data'][0]['tip']['publisher']
json_dict['data'][0]['tip']['title']

response.text
response.css('tbody')
response.css('table')
response.css('table.zly_xxgk_20170802')
response.css('table.zly_xxgk_20170802 tbody')
response.css('table.zly_xxgk_20170802 tbody').get()
response.css('div.zlyxwz_t2a p *::text').getall()
response.css('div.zlyxwz_t2a p a::attr(href)').getall()

**Hebei**

total_page 83

http://info.hebei.gov.cn/eportal/ui?pageId=6817552&currentPage=1&moduleId=3bb45f8814654e33ae014e740ccf771b&formKey=GOV_OPEN&columnName=EXT_STR7&relationId=

http://info.hebei.gov.cn/eportal/ui?pageId=6806152&articleKey=6903671&columnId=6806589

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://info.hebei.gov.cn/eportal/ui?pageId=6817552"
}
Request(url="http://info.hebei.gov.cn/eportal/ui?pageId=6817552&currentPage=1&moduleId=3bb45f8814654e33ae014e740ccf771b&formKey=GOV_OPEN&columnName=EXT_STR7&relationId=",headers=headers)
scrapy.Request(url="http://info.hebei.gov.cn/eportal/ui?pageId=6817552&currentPage=1&moduleId=3bb45f8814654e33ae014e740ccf771b&formKey=GOV_OPEN&columnName=EXT_STR7&relationId=",headers=headers)
req = scrapy.Request(url="http://info.hebei.gov.cn/eportal/ui?pageId=6817552&currentPage=1&moduleId=3bb45f8814654e33ae014e740ccf771b&formKey=GOV_OPEN&columnName=EXT_STR7&relationId=",headers=headers)
fetch(req)
response
response.text
response.css('table.xxgkzclbtab3')
len(response.css('table.xxgkzclbtab3'))
response.css('table.xxgkzclbtab3')[0].css('td a::text')getall()
response.css('table.xxgkzclbtab3')[0].css('td a::text').getall()
response.css('table.xxgkzclbtab3')[0].css('td a::text').get()
response.css('table.xxgkzclbtab3')[0].css('td a::attr(href)').get()
response.css('table.xxgkzclbtab3')[0].css('td[align="left"]::text').get()
response.css('table.xxgkzclbtab3')[0].css('td[align="center"]::text').get()
response.css('table.xxgkzclbtab3')[0].css('td[align="center"]::text').getall()
response.css('table.xxgkzclbtab3')[0].css('td[align="center"]::text').getall()[-1]
response.css('table.xxgkzclbtab3')[0].css('td[align="center",width="60"]::text').get()
response.css('table.xxgkzclbtab3')[0].css('td[align="center"][width="60"]::text').get()
response.css('table.xxgkzclbtab3')[0].css('td[align="center"][width="150"]::text').get()

response.css('div.xxgk_bmxl')
response.css('div.xxgk_bmxl td')
len(response.css('div.xxgk_bmxl td'))
response.css('div.xxgk_bmxl td')[0].css('*::text').get()
response.css('div.xxgk_bmxl td')[1].css('*::text').get()
response.css('div.xxgk_bmxl td')[2].css('*::text').get()
response.css('div.xxgk_bmxl td')[3].css('*::text').get()
response.css('div.xxgk_bmxl td')[4].css('*::text').get()
response.css('div.xxgk_bmxl td')[9].css('*::text').get()
response.css('div.xxgk_bmxl td')[8].css('*::text').get()
response.css('div#zoom')
response.css('div#zoom div')
response.css('div#zoom div::text').getall()
response.css('div#zoom div *::text').getall()

**Neimenggu**

total_page 119

http://www.nmg.gov.cn/module/xxgk/search.jsp?infotypeId=&jdid=2&area=1115000001151201XD&divid=div1686&vc_title=&vc_number=&sortfield=compaltedate:0&currpage=4&vc_filenumber=&vc_all=&texttype=&fbtime=&texttype=&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=4&sortfield=compaltedate:0&fields=&fieldConfigId=&hasNoPages=&infoCount=

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.nmg.gov.cn/col/col1686/index.html",
    'Host':'www.nmg.gov.cn',
    'Origin':'http://www.nmg.gov.cn'
}
req = scrapy.Request(url="http://www.nmg.gov.cn/module/xxgk/search.jsp?texttype=&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=4&sortfield=compaltedate:0&fields=&fieldConfigId=&hasNoPages=&infoCount=",headers=headers)
fetch(req)
response.text
req = scrapy.Request(url="http://www.nmg.gov.cn/module/xxgk/search.jsp?infotypeId=&jdid=2&area=1115000001151201XD&divid=div1686&vc_title=&vc_number=&sortfield=compaltedate:0&currpage=4&vc_filenumber=&vc_all=&texttype=&fbtime=&texttype=&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=4&sortfield=compaltedate:0&fields=&fieldConfigId=&hasNoPages=&infoCount=",headers=headers)
fetch(req)
response.text
response.css('tr.tr_main_value_odd')
response.css('tr.tr_main_value_even')
response.css('tr.tr_main_value_even')[0].css('td a::text').get()
response.css('tr.tr_main_value_even')[0].css('td a::attr(title)').get()
response.css('tr.tr_main_value_even')[0].css('td a::attr(href)').get()
response.css('tr.tr_main_value_even')[0].css('td[width="120"]::text').get()

'文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号'

response.css('table.xxgk_table')
response.css('table.xxgk_table td')
len(response.css('table.xxgk_table td'))
response.css('table.xxgk_table td')[0].css('*::text').get()
response.css('table.xxgk_table td')[-4].css('*::text').get()
response.css('div#zoom p *::text').getall()

**Shanxi_jin**

很多pdf

total page 138

http://www.shanxi.gov.cn/sxszfxxgk/index_100.shtml

http://www.shanxi.gov.cn/sxszfxxgk/sxsrmzfzcbm/sxszfbgt/flfg_7203/szfgfxwj_7205/200808/t20080812_145981.shtml


response.css('td.affaires-doc-title a::attr(title)').getall()
response.css('td.affaires-doc-title a::attr(href').getall()
response.css('td.affaires-doc-title a::attr(href)').getall()
response.css('td.affaires-doc-sizes::text').getall()
response.css('td.affaires-doc-published::text').getall()
response.css('table.affairs-document-titbar').getall()
response.css('table.affairs-document-box').getall()
response.css('table.affairs-document-box')
response.css('table.affairs-document-box tr')
response.css('table.affairs-document-box tr')[1:]
response.css('table.affairs-document-box tr')[1:][0]
response.css('table.affairs-document-box tr')[1:][0].css('td.affaires-doc-title a::attr(href)').get()
response.css('table.affairs-document-box tr')[1:][0].css('td.affaires-doc-title a::attr(title)').get()
response.css('table.affairs-document-box tr')[1:][0].css('td.affaires-doc-sizes::text').get()
response.css('table.affairs-document-box tr')[1:][0].css('td.affaires-doc-published::text').get()

response.css('table.affairs-detail-head')
response.css('table.affairs-detail-head').get()
response.css('table.affairs-detail-head td')
len(response.css('table.affairs-detail-head td'))
response.css('table.affairs-detail-head td')[0].css('*::text').get()
response.css('div[style="FONT-SIZE: 16px; LINE-HEIGHT: 160%"])
response.css('div[style="FONT-SIZE: 16px; LINE-HEIGHT: 160%"]')
response.css('div[style="FONT-SIZE: 16px; LINE-HEIGHT: 160%"] *::text').getall()

**Shanxi_shan**
