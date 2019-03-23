#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
from twilio.rest import Client
import requests
from lxml import etree
import pandas as pd

def sina_weather():
    url = 'http://weather.sina.com.cn/zhenjiang'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    res = requests.get(url, headers=headers)
    xp = etree.HTML(res.content, etree.HTMLParser(encoding='UTF-8'))  # 将text换成content  乱码小时
    date = xp.xpath('//div[@class="slider_ct"]/p')[0].text
    tom_tept = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[1]/p[5]')[0].text
    tom_tept1 = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[1]/p[3]/img/@title')
    tom_tept1 = '转'.join(tom_tept1)
    tep = xp.xpath('//div[@class="slider_degree"]')[0].text
    tom = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[1]')[0].text
    tom_tep = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[5]')[0].text
    tom_tep1 = xp.xpath('//div[@class="blk_fc_c0_scroll"]/div[2]/p[3]/img/@title')
    tom_tep1 = '转'.join(tom_tep1)
    clothes = xp.xpath('//div[@class="blk5_c clearfix png24"]/div[1]/p')[0].text
    # df = {}
    # df['日期'] = date
    # df['当前温度'] = tep
    df = ["\n",date,"\n", "镇江实时温度:", tep, "\n","天气:",tom_tept1,"\n", "今日温度为:",tom_tept,"\n","\n","明天",tom, "\n","天气：" , tom_tep1,"\n", '温度为: ',tom_tep, "\n","\n",'今天土豆助手推荐我的秀秀穿:',clothes]

    print(df)
    return df


def send_sms(to, text):
    account = "AC7a17da2b5961bb13fd0fee8d6b186f50"
    token = "f5eb48e2743f6473fa3bb47042d9a925"
    client = Client(account, token)
    text = text
    print(text)
    body1 = ' '.join(text) + '\n祝秀秀考得开心~~\n天天有个好心情~.~' # join和split 列表与字符串转换
    message = client.messages.create(to= to, from_="+16572208580",
                                    body= body1)
    print(message.sid)

def get_text():
    sina_weather()

    return text

if __name__ == '__main__':
    tel = "+8618352864716"
    text = sina_weather()


    send_sms(tel, text)