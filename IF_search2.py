#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import requests
from lxml import etree
import time
import pandas as pd

def get_ISSN (Jounal_name, headers):
    issnList = [None]*20
    urlr = "https://www.medsci.cn/sci/index.do?action=search#result"
    value = {
        "fullname": "{0}".format(Jounal_name),
        "province": "",
        "city": '',
        "impact_factor_b": "",
        "impact_factor_s": "",
        "rank": "if_rank_b",
        "Submit": "我要查询"
    }
    res_I = requests.post(urlr, headers=headers, data=value)
    bs_I = etree.HTML(res_I.text)

    # issnList[0] = bs_I.xpath('//tbody[1]/tr/td[2]')[0].text
    # issnList[1] = bs_I.xpath('//tbody[2]/tr/td[2]')[0].text
    j = len( bs_I.xpath('//tbody[@class="lunzhu sci"]'))

    try:
        for i in range(1,j+1):
            issnList[i-1] = bs_I.xpath('//tbody[{0}]'.format(i)+'/tr/td[2]')[0].text
            i+=1
    except:
        pass
    finally:
        issnList = filter(None, issnList)

        return issnList

    # for i in bs_I.xpath('//tbody/tr/td[2]')[0].text:
    #     issnList[range(10)] = i


def get_IF(ISSN, headers):
    base_url = "https://www.greensci.net/search?kw="
    url = base_url + ISSN
    res = requests.get(url, headers=headers)
    bs = etree.HTML(res.text)
    journal = bs.xpath('//table[@class="result-table-data"]/tr[2]/td[2]/div/p')[0].text
    print("期刊名：{0}".format(journal))
    IF_2015 = bs.xpath('//table[@class="result-table-data"]/tr[2]/td[3]/div')[0].text
    print("2015年影响因子：{0}".format(IF_2015))
    IF_2015a = {'2015年影响因子': IF_2015}
    IF_2016 = bs.xpath('//table[@class="result-table-data"]/tr[2]/td[4]/div')[0].text
    print("2016年影响因子：{0}".format(IF_2016))
    IF_2016a = {'2016年影响因子': IF_2016}
    IF_2017 = bs.xpath('//table[@class="result-table-data"]/tr[2]/td[5]/div')[0].text
    print("2017年影响因子：{0}".format(IF_2017))
    IF_2017a = {'2017年影响因子': IF_2017}
    time.sleep(2)


def save_to_excel (IF):
    pass

def main():
    Journal_name = input("请输入期刊名：")
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    base_url = "https://www.greensci.net/search?kw="
    issnList = get_ISSN(Journal_name, headers)

    for ISSN in issnList:
        get_IF(ISSN, headers)
        print("="*40)

    print("Finish")


if __name__ == '__main__':
    main()
