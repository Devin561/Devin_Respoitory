#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import requests
from lxml import etree
import time
import pandas as pd
import re

url1 = ""
url = 'http://weather.sina.com.cn/zhenjiang'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
res = requests.get(url, headers=headers)
xp = etree.HTML(res.content, etree.HTMLParser(encoding='UTF-8'))# 将text换成content  乱码小时
# text1 = pd.DataFrame()
# for i in xp.xpath('//ul[@class="clearfix"]'):
#     # text1['日期'] = i.xpath('li[1]/h1')
#     date = i.xpath('//div[@class="t"]/ul[@class="clearfix"]/li[1]/h1/text()')
#     weather = i.xpath('//li[1]/p[@class="wea"]/text()')

date = xp.xpath('//div[@class="slider_ct"]/p')[0].text
tep = xp.xpath('//div[@class="slider_degree"]/text()')
tom = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[1]/text()')
tom_tep = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[5]/text()')
tom_tep1 = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[3]/img/@title')
clothes = xp.xpath('//div[@class="blk5_c clearfix png24"]/div[1]/p/text()')
# tom_tep1 = re.sub('Â', '', tom_tep)
# strs = (etree.tostring(date, encoding = "utf-8", pretty_print = True, method = "html"))
print(date)
print(tep)
print(tom)
print(tom_tep)
print(tom_tep1)
print(clothes)