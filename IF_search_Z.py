#!/usr/bin/env python3
#coding: utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import tkinter as tk
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
                                   '2016年影响因子': [IF_2016], '2017年影响因子': [IF_2017]})#.sort_index(by='2017年影响因子')
            result = pd.concat([result, dataIF])
    except:
        pass
    return result

def save_to_excel (IF):
    pass

def reg(self):
    Journal_name = en1.get()
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    base_url = "https://www.greensci.net/search?kw="
    issnList = get_ISSN(Journal_name, headers)
    IF = pd.DataFrame()
    for ISSN in issnList:
        res = get_IF(ISSN, headers).set_index(['期刊名'])
        IF = pd.concat([IF, res])
    time.sleep(1.5)

    # IF.to_csv('out.txt',index=False, rsep='\t')
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    lb3 = tk.Label(base, text= IF)
    lb3.grid(row=6, column=0,sticky=tk.W)



base = tk.Tk()
base.geometry("600x700")
base.wm_title("Impact Factor Search")

lb1 = tk.Label(base, text= "请填写以下信息", font=("Arial", 20), width=30, height=1,bg="red")
lb1.grid(row=0, sticky= tk.W)
lb2 = tk.Label(base, text="期刊名：", font=("Arial", 17))
lb2.grid(row=1, column=0, sticky= tk.W)
en1 = tk.Entry(base, width=30)
en1.grid(row=2, column=0, sticky=tk.W)


btn = tk.Button(base, text="开始查询", command=reg)
btn.grid(row=5, column=0, sticky=tk.W)
btn.bind_all("<Return>", reg)



base.mainloop()


