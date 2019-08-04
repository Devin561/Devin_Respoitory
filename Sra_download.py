#!/usr/bin/env python3
#coding: utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import requests
from lxml import etree
from time import perf_counter
import os

class SRR_Download():
    def __init__(self, id):
        self.id = id
        self.path = ""

    def get_download_url(self):
        print("worker 1 " + self.id)
        url = "https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=" + self.id
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        res = requests.get(url, headers=headers)
        print("+++")
        xp = etree.HTML(res.text)
        download_link = xp.xpath('//table[@class="zebra"]/tr[1]/td[3]/a/@href')  # 删掉了原有的tbody后成功匹配，原来为//table[@class="zebra"]/tbody/tr[1]/td[3]/a/@href
        print("1111")
        download_link = "".join(download_link)  # 将列表转换为字符串
        return download_link

    # def get_download_pic_url(self):
    #     print("worker 2 ")
    #     url = "https://trace.ncbi.nlm.nih.gov/Traces/sra/?run=" + self.id
    #     headers = {
    #         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #     res = requests.get(url, headers=headers)
    #     xp = etree.HTML(res.text)
    #     download_link = xp.xpath(
    #         '//table[@class="zebra"]/tr[1]/td[3]/a/@href')  # 删掉了原有的tbody后成功匹配，原来为//table[@class="zebra"]/tbody/tr[1]/td[3]/a/@href
    #     download_link = "".join(download_link)  # 将列表转换为字符串
    #     return download_link

    def download_file(self):
        print("worker 3 ")
        url = self.get_download_url()
        # url = "http://upload-images.jianshu.io/upload_images/4131789-b956230070725f1e.png"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
        print("Downloading file: {0}".format(url))
        res = requests.get(url, headers=headers, stream=True)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
        filename = self.id
        f = open(r".\Download SRR\{}".format(filename), "wb")
        for chunk in res.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
        # print(type(res))

    def download_begin(self):
        print("worker 4 ")
        folder_path = "Download SRR"
        if not os.path.exists(folder_path):
            print("Selected folder not exist, try to create it.")
            os.makedirs(folder_path)
        # 获得图片后缀
        # file_suffix = os.path.splitext("//upload-images.jianshu.io/upload_images/4131789-b956230070725f1e.png")[1]
        # # 拼接图片名（包含路径）
        # filename = '{}{}{}{}'.format("E:\Python\Py charm work\\bio_python_1\Download SRR", os.sep, "jianshu", file_suffix)
        # f = open("//" + folder_path + "/" + self.path, "wb")
        self.download_file()


if __name__ == '__main__':
    id = input("请输入SRR号：")
    t = SRR_Download(id)
    # t.get_file_by_url()
    t.download_begin()
    print(t.get_download_url())
    print(perf_counter())