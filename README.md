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

重庆模式

response.css('table.gk_list_table tr‘)
response.css('table.gk_list_table tr')
len(response.css('table.affairs-detail-head td'))
len(response.css('table.gk_list_table tr'))
response.css('table.gk_list_table tr')[1:].css('a::attr(href)').get()
response.css('table.gk_list_table tr')[1:].css('a::attr(title)').get()
response.css('table.gk_list_table tr')[1:].css('td.textCenter::text').get()
response.css('table.gk_list_table tr')[1:].css('td[align="center"]::text').get()

response.css('div.zfwj_news_table')
response.css('div.zfwj_news_table tr')
response.css('div.zfwj_news_table tr td')
len(response.css('div.zfwj_news_table tr td'))
response.css('div.zfwj_news_table tr td')[0].css('*::text').get()
response.css('div.zfwj_news_table tr td')[1].css('*::text').get()
response.css('div#info_content p *::text').getall()
response.css('div.xzfwj_rig a[target="_blank"])
response.css('div.xzfwj_rig a[target="_blank"]')
response.css('div.xzfwj_rig a[href$=".pdf"]')
response.css('div.xzfwj_rig a[href$=".pdf"]::attr(href)')
response.css('div.xzfwj_rig a[href$=".pdf"]::attr(href)').get()

**Ningxia**

 该网站已接入<span style="font-size: 14px;color: #006cb8;"><strong>电信云堤&bull;网站安全防护服务</strong></span>，由于您使用的请求方法存在潜在安全风险，被云堤网站安全防护拦截。如果您有任何疑问或者认为这是一个误报，请您通过以下方式联系<span style="font-size: 14px;color: #006cb8;"><strong>7X24</strong></span>小时客服：

 数据最后是用我个人pc爬取的

Total page 48

http://www.nx.gov.cn/zwgk/qzfwj/list.html
http://www.nx.gov.cn/zwgk/qzfwj/list_2.html

response.css('ul.nx-list')
response.css('ul.nx-list li')
len(response.css('ul.nx-list li')) == 20
response.css('ul.nx-list li a')
len(response.css('ul.nx-list li a'))
response.css('ul.nx-list li a::attr(href)')
len(response.css('ul.nx-list li span'))
len(response.css('ul.nx-list li span.date'))
len(response.css('ul.nx-list li div.nx-contmtab'))
len(response.css('ul.nx-list li div.nx-conmtab'))
len(response.css('ul.nx-list li div.nx-conmtab')[0].css('p'))
len(response.css('ul.nx-list li div.nx-conmtab')[3].css('p'))
response.css('ul.nx-list li div.nx-conmtab')[3].css('p')[0].css('span.tt')
response.css('ul.nx-list li div.nx-conmtab')[3].css('p')[0].css('span.tt::text').get()
response.css('ul.nx-list li div.nx-conmtab')[3].css('p')[0].css('span.value::text').get()
response.css('ul.nx-list li span::text').get()
response.css('ul.nx-list li a::attr(href)')
response.css('ul.nx-list li a::attr(href)').get()
response.css('ul.nx-list li a::attr(title)').get()

'发文字号：'

response.text
response.css('div.view')
response.css('div.view p *::text').getall()

**Gansuu**

实际项目编程中注意文本为空的特殊情况

http://www.gansu.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord=82&endrecord=162&perpage=27&appid=1&webid=1&path=%2F&columnid=4729&sourceContentType=3&unitid=18064&webname=%E4%B8%AD%E5%9B%BD%C2%B7%E7%94%98%E8%82%83&permissiontype=0

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.gansu.gov.cn/col/col4729/index.html",
    "Host": "www.gansu.gov.cn",
    "Origin":"http://www.gansu.gov.cn"
}
req = scrapy.Request(url = "http://www.gansu.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord=82&endrecord=162&perpage=27",headers = headers)
req = scrapy.Request(url = "http://www.gansu.gov.cn/module/jslib/jquery/jpage/dataproxy.jsp?startrecord=82&endrecord=162&perpage=27&appid=1&webid=1&path=%2F&columnid=4729&sourceContentType=3&unitid=18064&webname=%E4%B8%AD%E5%9B%BD%C2%B7%E7%94%98%E8%82%83&permissiontype=0",headers = headers)
fetch(req)
response.text
len('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\ntotalRecord=714.0;totalPage = 27;dataStore = ')
import ast
l = ast.literal_eval(response.text[69:-1])
l
from scrapy.selector import Selector
Selector(text=l[0]).css('a')
Selector(text=l[0]).css('a::attr(href)').get()
Selector(text=l[0]).css('span::text')
Selector(text=l[0]).css('span::text').get()
Selector(text=l[0]).css('a::attr(title)').get()



response.css('div#zoom p *::text').getall() 

**Qinghai**

total page = 49

http://zwgk.qh.gov.cn/zdgk/zwgkzfxxgkml/list_1.html

response.text
response.css('li.clearfix')
response.css('li.clearfix')[0].css('p.tt a::attr(href)').get()
response.css('li.clearfix')[0].css('p.tt a::attr(title)').get()
response.css('li.clearfix')[0].css('p.num').get()
response.css('li.clearfix')[0].css('p.num::text').get()
response.css('li.clearfix')[0].css('p.span::text').get()
response.css('li.clearfix')[0].css('span::text').get()

response.css('ul.clearfix li')[-2].css('span')[1].css('::text').get() 
response.css('div.view p *::text').getall()     

**Xinjiang**

很多是复印件图片，没有文本，也不提供pdf下载

total page 34

http://www.xinjiang.gov.cn/xinjiang/gfxwj/zfxxgk_gknrz.shtml

response.css('div.gknr_list dd')
len(response.css('div.gknr_list dd'))
response.css('div.gknr_list dd')[0].css('a.attr(href)').get()
response.css('div.gknr_list dd')[0].css('a.attr(href)').get()
response.css('div.gknr_list dd')[0].css('a').get()
response.css('div.gknr_list dd')[0].css('a::attr(href)').get()
response.css('div.gknr_list dd')[0].css('a::attr(title)').get()
response.css('div.gknr_list dd')[0].css('span').get()
response.css('div.gknr_list dd')[0].css('span::text').get()


response.css('ul.clearfix')
response.css('ul.clearfix li')
response.css('ul.clearfix li')[0].css('*::text').getall()
response.css('ul.clearfix li')[-2].css('*::text').getall()
response.css('ul.clearfix li')[0].css('*::text').getall()[0].split('：')
response.css('ul.clearfix li')[-3].css('*::text').getall()[0].split('：')
response.css('div.gknbxq_detail p *::text)').getall()
response.css('div.gknbxq_detail *::text)').getall()
response.css('div.gknbxq_detail p::text)').getall()
response.css('div.gknbxq_detail p b::text)').getall()
response.css('div.gknbxq_detail p b::text').getall()
response.css('div.gknbxq_detail p *::text').getall()


**Sichuan**

total page  = 716

http://www.sc.gov.cn/zcwj/default.aspx?p=6&gpiid=&dept=6

HTML

In [9]: response.css('table')[1].css('tr')[1:][0].css('td')                                                                                                                       
Out[9]: 
[<Selector xpath='descendant-or-self::td' data='<td height="15" align="center" style=...'>,
 <Selector xpath='descendant-or-self::td' data='<td align="left" style="color: #d3000...'>,
 <Selector xpath='descendant-or-self::td' data='<td align="center" style="color: #d30...'>,
 <Selector xpath='descendant-or-self::td' data='<td align="left" style="color: #d3000...'>]

In [10]: response.css('table')[1].css('tr')[1:][0].css('td')[1].css('a::attr(href)')                                                                                              
Out[10]: [<Selector xpath='descendant-or-self::a/@href' data='t.aspx?i=20200227194711-734258-00-000'>]

In [11]: response.css('table')[1].css('tr')[1:][0].css('td')[1].css('a::attr(href)').get()                                                                                        
Out[11]: 't.aspx?i=20200227194711-734258-00-000'

In [12]: response.css('table')[1].css('tr')[1:][0].css('td')[1].css('a::attr(title)').get()                                                                                       
Out[12]: '简报（第061期）'

In [13]: response.css('table')[1].css('tr')[1:][0].css('td')[2].css('::text').get()                                                                                               
Out[13]: '\r\n                                2020-02-27\r\n                            '

In [14]: response.css('table')[1].css('tr')[1:][0].css('td')[3].css('::text').get()                                                                                               
Out[14]: '\r\n                                \r\n                            '

response.text
response.css('tbody')
response.css('tr')
response.css('td p *::text').getall()

**Yunnan**

total page 27

http://www.yn.gov.cn/zwgk/zcwj/zxwj/index_1.html

response.css('ul.zclist')[0].css('li')[2].css("::text").get()
response.css('ul.zclist')[0].css('li')[1].css("a::attr(href)").get() 

response.css('div.view p *::text').getall()
response.css('div.arti a::attr(hred)').getall()
response.css('div.arti a::attr(hredf').getall()
response.css('div.arti a::attr(hredf)').getall()
response.css('div.arti a::attr(href)').getall()
response.css('div.arti span#fj a::attr(href)').getall()
response.css('div.arti span#fj')
response.css('span#fj')


# Guizhou

total page 

http://www.guizhou.gov.cn/zwgk/zcfg/szfwj_8191/qff_8193/index_1.html

28

http://www.guizhou.gov.cn/zwgk/zcfg/gfxwj/index_2.html

17

In [5]: response.css('div.right-list-box ul li')[0].css('a::attr(href)')                                                                                                          
Out[5]: [<Selector xpath='descendant-or-self::a/@href' data='http://www.guizhou.gov.cn/zwgk/zcfg/s...'>]

In [6]: response.css('div.right-list-box ul li')[0].css('a::attr(href)').get()                                                                                                    
Out[6]: 'http://www.guizhou.gov.cn/zwgk/zcfg/szfwj_8191/qff_8193/201902/t20190212_2255555.html'

In [7]: response.css('div.right-list-box ul li')[0].css('a::attr(title)').get()                                                                                                   
Out[7]: '省人民政府关于建立涉农资金统筹整合长效机制的实施意见（黔府发〔2019〕4号）'

In [8]: response.css('div.right-list-box ul li')[0].css('span::text').get()                                                                                                       
Out[8]: '2019-02-12  16:43'

response.css('div.view p *::text').getall()  


**Guangxi**

total page 163

In [22]: response.css('ul.more-list tr')[1:][4*29].css('a::text').get()                                                                                                           
Out[22]: '\n                                广西壮族自治区人民政府\r\n关于欧军、林春同志任免职的通知\r\n（桂政干〔2020〕68号）\n                            '

In [23]: response.css('ul.more-list tr')[1:][4*29].css('td')                                                                                                                      
Out[23]: 
[<Selector xpath='descendant-or-self::td' data='<td>\n                            30\n ...'>,
 <Selector xpath='descendant-or-self::td' data='<td align="left" onmouseenter="td_ove...'>,
 <Selector xpath='descendant-or-self::td' data='<td><strong>发文单位：</strong>\n          ...'>,
 <Selector xpath='descendant-or-self::td' data='<td><strong>成文日期：</strong>\n          ...'>,
 <Selector xpath='descendant-or-self::td' data='<td colspan="2"><strong>标\u3000\u3000题：</strong...'>,
 <Selector xpath='descendant-or-self::td' data='<td><strong>发文字号：</strong>\n          ...'>,
 <Selector xpath='descendant-or-self::td' data='<td><strong>发布日期：</strong>\n          ...'>,
 <Selector xpath='descendant-or-self::td' data='<td>\n                                ...'>,
 <Selector xpath='descendant-or-self::td' data='<td>\n                            有效\n ...'>,
 <Selector xpath='descendant-or-self::td' data='<td>\n                                ...'>,
 <Selector xpath='descendant-or-self::td' data='<td>\n                                ...'>]

In [24]: response.css('ul.more-list tr')[1:][4*29].css('td')[1].css('::text').get()                                                                                               
Out[24]: '\n                            '

In [25]: response.css('ul.more-list tr')[1:][4*29].css('td')[-5].css('::text').get()                                                                                              
Out[25]: '发布日期：'

In [26]: response.css('ul.more-list tr')[1:][4*29].css('td')[-4].css('::text').get()                                                                                              
Out[26]: '\n                                                        桂政干〔\n                            2020〕\n                            68号\n                                                    '

In [27]: response.css('ul.more-list tr')[1:][4*29].css('td')[-2].css('::text').get()                                                                                              
Out[27]: '\n                                                        2020年02月14日\n        

response.css('div.article-con p *::text').getall() 

**Guangdong**

total page 205

http://www.gd.gov.cn/zwgk/wjk/qbwj/index_2.html

In [3]: response.css('div.viewList ul li')[0].css('a::attr(href)').get()                                                                                                          
Out[3]: 'http://www.gd.gov.cn/zwgk/wjk/qbwj/yfb/content/post_2894098.html'

In [4]: response.css('div.viewList ul li')[0].css('a::text').get()                                                                                                                
Out[4]: '广东省人民政府办公厅关于印发广东省加快半导体及集成电路产业发展若干意见的通知'

In [5]: response.css('div.viewList ul li')[0].css('span.wh::text').get()                                                                                                          
Out[5]: '粤府办〔2020〕2号'

In [6]: response.css('div.viewList ul li')[0].css('span.date::text').get()                                                                                                        
Out[6]: '2020-02-13'

response.css('div.zw p *::text').getall() 


**Hunan**

total page 
http://www.hunan.gov.cn/hnszf/xxgk/wjk/szfwj/wjk_glrb_34.html
34
http://www.hunan.gov.cn/hnszf/xxgk/wjk/szfbgt/wjk_glrb_34.html
34

In [3]: response.css('tbody tr')[0].css('a::attr(href)').get()                                                                                                                    
Out[3]: '/hnszf/xxgk/wjk/szfwj/200908/t20090826_239811.html'

In [4]: response.css('tbody tr')[0].css('a::text').get()                                                                                                                          
Out[4]: '湖南省人民政府关于做好第六次全国人口普查工作的通知'

In [5]: response.css('tbody tr')[0].css('td')[-2].css('::text').get()                                                                                                             
Out[5]: '2009-08-04'

In [6]: response.css('tbody tr')[0].css('td')[-3].css('::text').get()                                                                                                             
Out[6]: "var fileNum='湘政发 〔2009〕30号';if(fileNum!='null'){document.write(fileNum)}"

In [7]: response.css('tbody tr')[0].css('td')[-3].css('::text').get().split("'")[1]  

response.css('div.TRS_PreAppend p *::text').getall() 

**Hubei**

http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=4&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4khp3EogDRyXCQnl7uG6zBIUNXk6_edeT6aGBf1NPP8OGt3S8PPBEpheaxOK4qtNCa1V.EYtI_.lexlJZIPC.EbeUlbaO0uXDzR_ikueHsEGHZ8OIWAzQsasy6Pjs5PXNl36ZkvA8JBUXxDn14wB5tQTdihJdorP88uNbV2IxDPb.O5ROkzGYU3k7S6cOeFUXYcAf9LeCn.im59VR9oGErB2qOMLXLImHPHJC5f4y6zeW2dUIR4km9sMTWfXhtbT6cnaUZwiW4J0kWs29B87NJEuanj5ZZhDp7coylrR9UZAyJBB5Jm0muIDq_GnhCv9QeSzrSCGv6Ky8L_YdOMUp_u6GatAbl1oa0mv0PGGYzqBcjrT6hQ_aJhHgh08x2JMQtayfImXbEEpKfvtUo4ZZYn7sYt1N_GuFta95f1.Jd7B4bHn4uzrKdL2tjdze9rRh._.RTFr6_ljnCpfqyzemLPM4

http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=6&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4sIVR3seoxz.6WbrzO0n7dh1L5Un4z.g0v92XSD7OntbfFW0InCjxrIgSR6s_A876GDpj3rH8jdrZRAEeHCuj3ngKR0xj.xfq3UQQa4vo_5S96U.BU_lh.7hOmILB2MvRqQ4dZkdko.9pBH2lksUw2D6QNnxQNFnciNprPpJDQ3N0uLN8jP8l.BJz9a6UKU8VfsC55rv1o_4yCHlCEx9qb7o2FYNPqwgZoy60b0HeOtMHEEAnlENVkJPKogE1JuZl9I9iCZwF4R0n8m2fouVWtnmQAbAVaR5OhlqzfCJiP7bubgYaZO1w_1wpihd1D23M_OWXNxHKHzu8jiQ5g2Q34.PIet_uELrVaYTIJImbuxAkMAtLkJO6Nnq7BYUCg772yAKe2G7rZtN8eHRq.RQnmQlX2ZpXXZG2wF2ODvpyQGrw7v1a2LgUkBxdVVTVcwQvmIW4zXsu_wIFthorLbOjKw4L

cookie = {
    "FSSBBIl1UgzbN7N80S":"bUU9HTDtknT3eWohpn7aYBk7k5POLVrW5Q8.C2kOwojIfXDhvNHwZmTx8lHn8_Y9", "Hm_lvt_5544783ae3e1427d6972d9e77268f25d":"1585408324", "token":"081f1405-45e2-4539-96c2-94add9b6b215","uuid":"081f1405-45e2-4539-96c2-94add9b6b215", "_trs_uv":"k8br6wjg_3027_60lu","_trs_ua_s_1":"k8br6wjg_3027_avg", "Hm_lpvt_5544783ae3e1427d6972d9e77268f25d":"1585408340","dataHide2":"22e65282-2deb-4725-87d4-d68222591f97",
    "FSSBBIl1UgzbN7N80T":"442F_aNu9fU2V9QHihiZHUSQhKzZ3mpCUH8.JRZPqFaLcnC_ZFW9jN2C1SJwRg9PVEZIxa4recmHISjD8vWexaECTXAYNvTKlwIiIWZObBwAD4bjJ1mQhs_L_L37wAmC3yneW_RRYhAUzK4a4BeNSFloZSFdhwIo9e2kbPATqQ8bMGmTSdU00VFhzVK5ybPm9aQI5Iy5zsJL_dor6pL.R7jqMBLyubMceC45V9.MWz9VeMsbTufJ0pLE2K6_UI2MtvbfRrWuW2mrJpVdvZZm2nB6NnOQhdhhPtGk6mGiLWn9732XlxAWvOLTXGz_hZCDobxDqOjb90_3bqo.BECy8Nb89haPBUjF_ax_3YvM1DfDF.AbWWY0N6x_mSakeSUmYm9g9PQwrrg130ceiIG3q6Z7x"
}


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.hubei.gov.cn/site/hubei/search.html?WxUg5ztDmi=1585408322959",
    'Host':www.hubei.gov.cn,
}

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.hubei.gov.cn/site/hubei/search.html?WxUg5ztDmi=1585408322959",
    'Host':'www.hubei.gov.cn',
}
req = scrapy.Request(url='http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=4&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4khp3EogDRyXCQnl7uG6zBIUNXk6_edeT6aGBf1NPP8OGt3S8PPBEpheaxOK4qtNCa1V.EYtI_.lexlJZIPC.EbeUlbaO0uXDzR_ikueHsEGHZ8OIWAzQsasy6Pjs5PXNl36ZkvA8JBUXxDn14wB5tQTdihJdorP88uNbV2IxDPb.O5ROkzGYU3k7S6cOeFUXYcAf9LeCn.im59VR9oGErB2qOMLXLImHPHJC5f4y6zeW2dUIR4km9sMTWfXhtbT6cnaUZwiW4J0kWs29B87NJEuanj5ZZhDp7coylrR9UZAyJBB5Jm0muIDq_GnhCv9QeSzrSCGv6Ky8L_YdOMUp_u6GatAbl1oa0mv0PGGYzqBcjrT6hQ_aJhHgh08x2JMQtayfImXbEEpKfvtUo4ZZYn7sYt1N_GuFta95f1.Jd7B4bHn4uzrKdL2tjdze9rRh._.RTFr6_ljnCpfqyzemLPM4',headers = headers)
fetch(req)
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.hubei.gov.cn/site/hubei/search.html?WxUg5ztDmi=1585408322959",
    'Host':"www.hubei.gov.cn",
    "Cookie": "Secure; FSSBBIl1UgzbN7N80S=bUU9HTDtknT3eWohpn7aYBk7k5POLVrW5Q8.C2kOwojIfXDhvNHwZmTx8lHn8_Y9; Secure; Hm_lvt_5544783ae3e1427d6972d9e77268f25d=1585408324; token=081f1405-45e2-4539-96c2-94add9b6b215; uuid=081f1405-45e2-4539-96c2-94add9b6b215; _trs_uv=k8br6wjg_3027_60lu; _trs_ua_s_1=k8br6wjg_3027_avg; Hm_lpvt_5544783ae3e1427d6972d9e77268f25d=1585408340; dataHide2=22e65282-2deb-4725-87d4-d68222591f97; FSSBBIl1UgzbN7N80T=4chrQxoLc3y5nwnVLnGvNXIozBkv5ZdzSCaa.G1ybO8u9h3fFOPdWAhz0EODdrtynS1lBxYFM4.VyElwg8PbBxbzsVozgD4fMB6ywNMwjahnHDkmTVpTVxLvtLims.uiZIka90VU2FzBO3RWO1H0RsbqHafXynQ_AcX20Th19FdEULoBexVaHwwYrCIKq5XogACvojsb0MrPvflemAzrkTABn5xjTF9lQmOi41Zj0faCAt2pfS89Hsmtidob.eTeX91zR3fVOPz9QIZGnCtZSvb3ej3iMpyLVH1YTfy6JGxFnAwjQp0JCASiBqi.QK1CSc.iDr3Qy6AN.eVUG.MDdZLavvTm0Od7GThwgCCC4UnClwCNrFfaGu5he9pNLp1yXNhhnFxQzAyL3bbrjD8hb2Jfa",
}
req = scrapy.Request(url='http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=4&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4khp3EogDRyXCQnl7uG6zBIUNXk6_edeT6aGBf1NPP8OGt3S8PPBEpheaxOK4qtNCa1V.EYtI_.lexlJZIPC.EbeUlbaO0uXDzR_ikueHsEGHZ8OIWAzQsasy6Pjs5PXNl36ZkvA8JBUXxDn14wB5tQTdihJdorP88uNbV2IxDPb.O5ROkzGYU3k7S6cOeFUXYcAf9LeCn.im59VR9oGErB2qOMLXLImHPHJC5f4y6zeW2dUIR4km9sMTWfXhtbT6cnaUZwiW4J0kWs29B87NJEuanj5ZZhDp7coylrR9UZAyJBB5Jm0muIDq_GnhCv9QeSzrSCGv6Ky8L_YdOMUp_u6GatAbl1oa0mv0PGGYzqBcjrT6hQ_aJhHgh08x2JMQtayfImXbEEpKfvtUo4ZZYn7sYt1N_GuFta95f1.Jd7B4bHn4uzrKdL2tjdze9rRh._.RTFr6_ljnCpfqyzemLPM4',headers = headers)
fetch(req)
req = scrapy.Request(url='http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=6&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4sIVR3seoxz.6WbrzO0n7dh1L5Un4z.g0v92XSD7OntbfFW0InCjxrIgSR6s_A876GDpj3rH8jdrZRAEeHCuj3ngKR0xj.xfq3UQQa4vo_5S96U.BU_lh.7hOmILB2MvRqQ4dZkdko.9pBH2lksUw2D6QNnxQNFnciNprPpJDQ3N0uLN8jP8l.BJz9a6UKU8VfsC55rv1o_4yCHlCEx9qb7o2FYNPqwgZoy60b0HeOtMHEEAnlENVkJPKogE1JuZl9I9iCZwF4R0n8m2fouVWtnmQAbAVaR5OhlqzfCJiP7bubgYaZO1w_1wpihd1D23M_OWXNxHKHzu8jiQ5g2Q34.PIet_uELrVaYTIJImbuxAkMAtLkJO6Nnq7BYUCg772yAKe2G7rZtN8eHRq.RQnmQlX2ZpXXZG2wF2ODvpyQGrw7v1a2LgUkBxdVVTVcwQvmIW4zXsu_wIFthorLbOjKw4L',headers = headers)
fetch(req)

cookie = {
    "FSSBBIl1UgzbN7N80S":"bUU9HTDtknT3eWohpn7aYBk7k5POLVrW5Q8.C2kOwojIfXDhvNHwZmTx8lHn8_Y9", "Hm_lvt_5544783ae3e1427d6972d9e77268f25d":"1585408324", "token":"081f1405-45e2-4539-96c2-94add9b6b215","uuid":"081f1405-45e2-4539-96c2-94add9b6b215", "_trs_uv":"k8br6wjg_3027_60lu","_trs_ua_s_1":"k8br6wjg_3027_avg", "Hm_lpvt_5544783ae3e1427d6972d9e77268f25d":"1585408340","dataHide2":"22e65282-2deb-4725-87d4-d68222591f97",
    "FSSBBIl1UgzbN7N80T":"442F_aNu9fU2V9QHihiZHUSQhKzZ3mpCUH8.JRZPqFaLcnC_ZFW9jN2C1SJwRg9PVEZIxa4recmHISjD8vWexaECTXAYNvTKlwIiIWZObBwAD4bjJ1mQhs_L_L37wAmC3yneW_RRYhAUzK4a4BeNSFloZSFdhwIo9e2kbPATqQ8bMGmTSdU00VFhzVK5ybPm9aQI5Iy5zsJL_dor6pL.R7jqMBLyubMceC45V9.MWz9VeMsbTufJ0pLE2K6_UI2MtvbfRrWuW2mrJpVdvZZm2nB6NnOQhdhhPtGk6mGiLWn9732XlxAWvOLTXGz_hZCDobxDqOjb90_3bqo.BECy8Nb89haPBUjF_ax_3YvM1DfDF.AbWWY0N6x_mSakeSUmYm9g9PQwrrg130ceiIG3q6Z7x"
}
req = scrapy.Request(url='http://www.hubei.gov.cn/igs/front/search/list.html?filter[FileName,DOCCONTENT,fileNum-or]=&pageNumber=6&pageSize=10&siteId=50&index=hbsrmzf-index-alias&type=governmentdocuments&filter[CHNLDESC]=&filter[fileYear]=&filter[fileYear-lte]=&filter[SITEID]=54&filter[CNAME]=&orderProperty=PUBDATE&orderDirection=desc&MmEwMD=4sIVR3seoxz.6WbrzO0n7dh1L5Un4z.g0v92XSD7OntbfFW0InCjxrIgSR6s_A876GDpj3rH8jdrZRAEeHCuj3ngKR0xj.xfq3UQQa4vo_5S96U.BU_lh.7hOmILB2MvRqQ4dZkdko.9pBH2lksUw2D6QNnxQNFnciNprPpJDQ3N0uLN8jP8l.BJz9a6UKU8VfsC55rv1o_4yCHlCEx9qb7o2FYNPqwgZoy60b0HeOtMHEEAnlENVkJPKogE1JuZl9I9iCZwF4R0n8m2fouVWtnmQAbAVaR5OhlqzfCJiP7bubgYaZO1w_1wpihd1D23M_OWXNxHKHzu8jiQ5g2Q34.PIet_uELrVaYTIJImbuxAkMAtLkJO6Nnq7BYUCg772yAKe2G7rZtN8eHRq.RQnmQlX2ZpXXZG2wF2ODvpyQGrw7v1a2LgUkBxdVVTVcwQvmIW4zXsu_wIFthorLbOjKw4L',headers = headers,cookies=cookie)
fetch(req)


http://www.hubei.gov.cn/site/hubei/search.html?WxUg5ztDmi=1585408322959

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.hubei.gov.cn/site/hubei/search.html?WxUg5ztDmi=1585408322959",
    'Host':"www.hubei.gov.cn",
    "Cookie": "Secure; FSSBBIl1UgzbN7N80S=bUU9HTDtknT3eWohpn7aYBk7k5POLVrW5Q8.C2kOwojIfXDhvNHwZmTx8lHn8_Y9; Secure; Hm_lvt_5544783ae3e1427d6972d9e77268f25d=1585408324; token=081f1405-45e2-4539-96c2-94add9b6b215; uuid=081f1405-45e2-4539-96c2-94add9b6b215; _trs_uv=k8br6wjg_3027_60lu; _trs_ua_s_1=k8br6wjg_3027_avg; Hm_lpvt_5544783ae3e1427d6972d9e77268f25d=1585408340; dataHide2=22e65282-2deb-4725-87d4-d68222591f97; FSSBBIl1UgzbN7N80T=4chrQxoLc3y5nwnVLnGvNXIozBkv5ZdzSCaa.G1ybO8u9h3fFOPdWAhz0EODdrtynS1lBxYFM4.VyElwg8PbBxbzsVozgD4fMB6ywNMwjahnHDkmTVpTVxLvtLims.uiZIka90VU2FzBO3RWO1H0RsbqHafXynQ_AcX20Th19FdEULoBexVaHwwYrCIKq5XogACvojsb0MrPvflemAzrkTABn5xjTF9lQmOi41Zj0faCAt2pfS89Hsmtidob.eTeX91zR3fVOPz9QIZGnCtZSvb3ej3iMpyLVH1YTfy6JGxFnAwjQp0JCASiBqi.QK1CSc.iDr3Qy6AN.eVUG.MDdZLavvTm0Od7GThwgCCC4UnClwCNrFfaGu5he9pNLp1yXNhhnFxQzAyL3bbrjD8hb2Jfa",
}


**Jiangxi**

Ok


**Anhui**

安徽也没爬成功

total page 448

In [4]: response.css('div.xxgk_navli')[0].css('a::attr(href)').get()                                                                                                              
Out[4]: 'http://www.ah.gov.cn/zmhd/xwfbhx/8288151.html'

In [5]: response.css('div.xxgk_navli')[0].css('a::attr(title)').get()                                                                                                             
Out[5]: '安徽省2020年3·15国际消费者权益日活动新闻发布会'

In [6]: response.css('div.xxgk_navli')[0].css('span.syh::text').get()                                                                                                             

In [7]: response.css('div.xxgk_navli')[0].css('span.date::text').get()                                                                                                            
Out[7]: '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2020-03-13\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'



In [7]: response.css('tbody')[0].css('td')[0].css('::text').getall()                                                                                                              
Out[7]: ['00298627-2/202003-00010']

In [8]: response.css('tbody')[0].css('th')[0].css('::text').getall()                                                                                                              
Out[8]: ['索', '引', '号：\n                        ']

In [9]: response.css('tbody')[0].css('th')[-2].css('::text').getall()                                                                                                             
Out[9]: ['文', '号：']

response.css('div.wzcon p *::text').getall() 

**Zhejiang**

total page 509

http://www.zj.gov.cn/module/xxgk/search.jsp?infotypeId=&jdid=3096&area=000014349&divid=div1551294&vc_title=&vc_number=&sortfield=,compaltedate:0&currpage=3&vc_filenumber=&vc_all=&texttype=0&fbtime=&texttype=0&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=3&sortfield=,compaltedate:0

http://www.zj.gov.cn/module/xxgk/search.jsp?infotypeId=&jdid=3096&area=000014349&divid=div1551294&vc_title=&vc_number=&sortfield=,compaltedate:0&currpage={0}&vc_filenumber=&vc_all=&texttype=0&fbtime=&texttype=0&fbtime=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage=3&sortfield=,compaltedate:0

In [5]: response.css('tr')[4:-2][0].css('a::attr(href)').get()                                                                                                                    
Out[5]: 'http://www.zj.gov.cn/art/2020/2/14/art_1551345_41917743.html'

In [6]: response.css('tr')[4:-2][0].css('a::attr(title)').get()                                                                                                                   

In [7]: response.css('tr')[4:-2][0].css('a::attr(mc)').get()                                                                                                                      
Out[7]: '浙江省人民政府关于朱林森等职务任免的通知'

In [8]: response.css('tr')[4:-2][0].css('a::attr(wh)').get()                                                                                                                      
Out[8]: '浙政干〔2019〕49号'

In [9]: response.css('tr')[4:-2][0].css('a::attr(rq)').get()                                                                                                                      
Out[9]: '2019-12-30'

response.css('div.bt_content p *::text').getall()  


**Fujian**

total page 655

http://www.fujian.gov.cn/was5/web/search?channelid=229105&templet=docs.jsp&sortfield=-pubdate&classsql=chnlid%3E22054*chnlid%3C22084&prepage=10&page={0}

raw = response.text
raw.remove('\n')
raw.replace('\n','')
raw.replace('\r','')
raw = raw.replace('\r','')
raw = raw.replace('\n','')
json.loads(raw)

response.css('div.xl-bk p *::text').getall() 

**Jiangsu**

total page 190

http://www.jiangsu.gov.cn/col/col76841/index.html?uid=297589&pageNum=1&col=1&appid=1&webid=1&path=%2F&columnid=76841&sourceContentType=1&unitid=297589&webname=%E6%B1%9F%E8%8B%8F%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&permissiontype=0

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0",
    'Referer': "http://www.jiangsu.gov.cn/col/col76841/index.html?uid=297589&pageNum=3",
    "Host": "www.jiangsu.gov.cn",
    "Origin":"http://www.jiangsu.gov.cn"
}

http://www.jiangsu.gov.cn/module/web/jpage/dataproxy.jsp?col=1&appid=1&webid=1&path=%2F&columnid=76841&sourceContentType=1&unitid=297589&webname=%E6%B1%9F%E8%8B%8F%E7%9C%81%E4%BA%BA%E6%B0%91%E6%94%BF%E5%BA%9C&permissiontype=0


Selector(text = response.css('div#297589 *::text').get()).css('record')

n [18]: response.css('::text').getall()[2:]                                                                                                                                      
Out[18]: 
['<li><a title="省政府关于进一步深化高考综合改革的若干意见" target="_blank" href="http://www.jiangsu.gov.cn/art/2020/3/23/art_46143_9019230.html">省政府关于进一步深化高考综合改革的若干意见</a><b>2020-03-23</b></li>',
 '<li><a title="省政府办公厅关于印发江苏省突发环境事件应急预案的通知" target="_blank" href="http://www.jiangsu.gov.cn/art/2020/3/19/art_46144_9017328.html">省政府办公厅关于印发江苏省突发环境事件应急预案的通知</a><b>2020-03-19</b></li>',
 '<li><a title="省政府办公厅关于印发江苏省太湖蓝藻暴发应急预案的通知" target="_blank" href="http://www.jiangsu.gov.cn/art/2020/3/19/art_46144_9017327.html">省政府办公厅关于印发江苏省太湖蓝藻暴发应急预案的通知</a><b>2020-03-19</b></li>',
 '<li><a title="省政府办公厅关于印发省政府2020年立法工作计划的通知" target="_blank" href="http://www.jiangsu.gov.cn/art/2020/3/19/art_46144_9017297.html">省政府办公厅关于印发省政府2020年立法工作计划的通知</a><b>2020-03-19</b></li>']

In [19]: Selector(text = response.css('::text').getall()[2:][0]).css('a::attr(title)').get()                                                                                      
Out[19]: '省政府关于进一步深化高考综合改革的若干意见'

In [20]: Selector(text = response.css('::text').getall()[2:][0]).css('a::attr(href)').get()                                                                                       
Out[20]: 'http://www.jiangsu.gov.cn/art/2020/3/23/art_46143_9019230.html'

In [21]: Selector(text = response.css('::text').getall()[2:][0]).css('b::text').get()                                                                                             
Out[21]: '2020-03-23'
________________________________________

In [45]: Selector(text = response.css('div#297589 *::text').get()).css('*')[7:][0].css('a')                                                                                       
Out[45]: [<Selector xpath='descendant-or-self::a' data='<a title="省政府关于进一步深化高考综合改革的若干意见" targ...'>]

In [46]: Selector(text = response.css('div#297589 *::text').get()).css('*')[7:][0].css('b')                                                                                       
Out[46]: [<Selector xpath='descendant-or-self::b' data='<b>2020-03-23</b>'>]

In [47]: Selector(text = response.css('div#297589 *::text').get()).css('*')[7:][1].css('b')                                                                                       
Out[47]: []

In [48]: Selector(text = response.css('div#297589 *::text').get()).css('*')[7:][0].css('b')                                                                                       
Out[48]: [<Selector xpath='descendant-or-self::b' data='<b>2020-03-23</b>'>]

In [49]: Selector(text = response.css('div#297589 *::text').get()).css('*')[7:][2].css('b')                                                                                       
Out[49]: [<Selector xpath='descendant-or-self::b' data='<b>2020-03-23</b>'>]

_____________________________

'文\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0号'

response.css('tbody')
response.css('tbody td')
len(response.css('tbody td'))
response.css('tbody td')[-8].css('::text').get()
response.css('tbody td')[-7].css('::text').get()
response.css('tbody td')[-9].css('::text').get()
response.css('tbody td')[-6].css('::text').get()

response.css('div#zoom p *::text').getall()

**Henan**

total page 369

http://wjbb.hnfzw.gov.cn/regulatory/viewQueryAll.do?offset=0&cdid=402881fa2d1738ac012d173a60930017

response.css('div.serListCon')
response.css('div.serListCon a')
response.css('div.serListCon a')[0].css('::attr(href)').get()
response.css('div.serListCon a')[0].css('::title').get()
response.css('div.serListCon a')[0].css('::attr(title)').get()


**Shandong**

total page 5835

http://www.shandong.gov.cn/module/xxgk/search_custom.jsp?fields=&fieldConfigId=247732&sortfield=compaltedate:0&fbtime=&texttype=&vc_all=&vc_filenumber=&vc_title=&vc_number=&currpage={0}&binlay=&c_issuetime=


In [2]: response.css('div.wip_lists')[0].css('a::attr(href)').get()                                                                                                               
Out[2]: 'http://www.shandong.gov.cn/art/2016/12/21/art_97741_53852.html?xxgkhide=1'

In [3]: response.css('div.wip_lists')[0].css('a::attr(title)').get()                                                                                                              

In [4]: response.css('div.wip_lists')[0].css('a::text').get()                                                                                                                     
Out[4]: '\n\t\t\t山东省人民政府办公厅关于印发山东省安全生产巡查工作制度的通知\n\t\t'


In [3]: response.css('div.wip_art_con p')[1].css('::text').get()                                                                                                                  
Out[3]: '鲁政字〔2011〕40号'

response.css('div.wip_art_con p *::text').getall()


**Hainan**

total page 486

http://www.hainan.gov.cn/u/search/wjk/rs?keywords=&docYear=&docName=&fwzh=&column=undefined&curPage=7&PageSize=15


In [7]: l['page']['list'][0]                                                                                  
response.text
import json
json.loads(response.txt)
json.loads(response.text)
l = json.loads(response.text)
l['page']['list']
l['page']['list'][0]

Out[7]: 
{'channel_name': '市县文件',
 'pubDate': '2020-01-10',
 'ccode': 'sxgw',
 'wcode': 'hainan',
 'website_name': '海南省人民政府网',
 'c_syh': '00817365-1/2020-44472',
 'url': '/hainan/sxgw/202001/8a1de39dadb74187bcfca788448d74dc.shtml',
 'channel_id': '0d690a95f6484047ae7f30a4424c9416',
 'c_wjbh': '',
 'c_ztc': '',
 'title': '关于五指山市、临高县、白沙黎族自治县退出贫困县序列的公示',
 'c_fbjg': '海南省扶贫开发领导小组办公室',
 'manuscript_id': '8a1de39dadb74187bcfca788448d74dc',
 'fwrq': '2020-01-10',
 'website_id': '18e6ca0ea4434f82ab06eb8dc11d926a'}

response.css('div#zoom p *::text').getall() 