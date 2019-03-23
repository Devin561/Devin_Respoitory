#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import threading
import time
from queue import Queue
import requests
from lxml import etree
import json


#用来存放采集线程
g_crawl_list = []
#用来存放解析线程
g_parse_list = []


class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self. headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def run(self):
        print('{}----线程启动' .format(self.name))
        # while 1使线程一直跑
        while 1:
            #判断采集线程何时推出
            if self.page_queue.empty():
                break
            #从队列中取出页码
            page = self.page_queue.get()
            #拼接url，发送请求
            url = self.url.format(page)
            r = requests.get(url, headers = self.headers)
            self.data_queue.put(r.text)
            #将相应内容存放到data_queue中
        print('{0}----线程结束'.format(self.name))





class ParserThread(threading.Thread):
    def __init__(self, name, data_queue, fp, lock):
        super(ParserThread, self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock

    def run(self):
        while 1:

            # 从data_queue中取出一页数据
            data = self.data_queue.get()
            self.parse_content(data)

    def parse_content(self, data):
        tree = etree.HTML(data)
        li_list = tree.xpath('//ul[@class="cont-list"]/li')
        items = []
        for oli in li_list:
            #获取图片标题
            title = oli.xpath('.//h2/a/text()')[0]
            #获取图片
            image_url = oli.xpath('.//div[contains(@class,"cont-list-main")]/p/img/@src')
            item = {
                '标题': title,
                '链接': image_url

            }
            items.append(item)
        #写到文件中
        self.lock.acquire()
        self.fp.write(json.dumps(items,ensure_ascii=False)
                      + '\n')
        self.lock.release()

def creat_queue():
    # 创建页码队列
    page_queue = Queue()
    for page in range(1, 11):
        page_queue.put(page)
    # 创建内容队列
    data_queue = Queue()
    return page_queue, data_queue


# 创建采集线程
def creat_crawl_thread(page_queue, data_queue):
    crawl_name = ['采集1号', '采集2号', '采集3号']
    for name in crawl_name:
        #创建一个采集线程
        tcrawl = CrawlThread(name, page_queue, data_queue)
        #保存到列表中
        g_crawl_list.append(tcrawl)

#创建解析线程
def creat_parse_thread(data_queue, fp, lock):
    parse_name = ['解析1号', '解析2号', '解析3号']
    for name in parse_name:
        #创建一个采集线程
        tparse = ParserThread(name, data_queue, fp, lock)
        #保存到列表中
        g_parse_list.append(tparse)

def main():
    # 创建队列函数
    page_queue, data_queue = creat_queue()
    # 打开文件
    fp = open('jian.json', 'a', encoding='utf-8')
    # 创建锁
    lock = threading.Lock()
    # 创建采集线程
    creat_crawl_thread(page_queue, data_queue)
    # 创建解析线程
    creat_parse_thread(data_queue, fp, lock)
    #启动所有采集线程
    # t1 = threading.Thread(target=creat_crawl_thread, args=(page_queue, data_queue))
    for tcrawl in g_crawl_list:
        tcrawl.start()
    #启动所有解析线程
    for tparse in g_parse_list:
        tparse.start()
    #主线程等待子线程结束
    for tcrawl in g_crawl_list:
        tcrawl.join()
    for tparse in g_parse_list:
        tparse.join()
    #关闭文件
    fp.close()
    print("All finished")

if __name__ == '__main__':
    main()