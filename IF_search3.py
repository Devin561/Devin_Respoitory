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
    result = pd.DataFrame()
    dataIF = pd.DataFrame()
    base_url = "https://www.greensci.net/search?kw="
    url = base_url + ISSN
    res = requests.get(url, headers=headers)
    bs = etree.HTML(res.text)
    try:
        for i in bs.xpath('//table[@class="result-table-data"]/tr[2]'):
            journal = i.xpath('td[2]/div/p')[0].text
            IF_2015 = i.xpath('td[3]/div')[0].text
            IF_2016 = i.xpath('td[4]/div')[0].text
            IF_2017 = i.xpath('td[5]/div')[0].text
            dataIF = pd.DataFrame({'期刊名': [journal], '2015年影响因子': [IF_2015],
                                   '2016年影响因子': [IF_2016], '2017年影响因子': [IF_2017]})
            result = pd.concat([result, dataIF])
    except:
        pass
    return result

def save_to_excel (IF):
    pass

def main():
    Journal_name = 'insect science' #input("请输入期刊名：")
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    base_url = "https://www.greensci.net/search?kw="
    issnList = get_ISSN(Journal_name, headers)
    IF = pd.DataFrame()
    for ISSN in issnList:
        res = get_IF(ISSN, headers)
        IF = pd.concat([IF, res])
    time.sleep(3)
    IF.to_csv('out.txt',index=False, sep='\t')
    print(IF)


if __name__ == '__main__':
    main()