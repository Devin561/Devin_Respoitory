#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
from lxml import etree
import re
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageDraw, ImageFont

from selenium.webdriver.support.select import Select
import numpy as np
import os
def picture():
    num = np.random.randint(1000, 99999)
    im1 = Image.open("ccc.png").convert('RGBA')
    txt = Image.new('RGBA', im1.size, (0, 0, 0, 0))
    fnt = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 18)
    d = ImageDraw.Draw(txt)
    d.rectangle((220, 72, 250, 102), fill='white')
    d.text((220, 72), "{0}".format(num), font=fnt, fill="black")

    out = Image.alpha_composite(im1, txt)
    out.save(r'ccc5.png')

num = np.random.randint(1000, 9999)
num2 = np.random.randint(1000, 9999)
num1 = num+num2*1000000
baseurl = 'http://u.paperok.com/user/register.jsp'
email = str(num1) + '@qq.com'
# password = 'zzxiaoxiao'
# qq = "1561651651"
password='aa66666'
name='xa'
tel='18566669852'
qq='1561651651'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
prefs = {
        'profile.default_content_setting_values' :
            {
                'notifications' : 2
            }
        }
options.add_experimental_option('prefs',prefs)
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get(baseurl)
time.sleep(2)



driver.find_element_by_name('email').send_keys(u'{0}'.format(email))
driver.find_element_by_name('password').send_keys(u'{0}'.format(password))
driver.find_element_by_name('passwordConfirm').send_keys(u'{0}'.format(password))
S = Select(driver.find_element_by_id("type")).select_by_value('DOCTOR')
driver.find_element_by_name('name').send_keys(u'{0}'.format(name))
driver.find_element_by_name('tel').send_keys(u'{0}'.format(tel))
driver.find_element_by_name('qq').send_keys(u'{0}'.format(qq))
driver.find_element_by_css_selector("[class='btn-submit']").click()
time.sleep(5)
# html=driver.page_source
# soup=BS(html,'lxml')
driver.find_element_by_css_selector("[class='btn-normal']").click()

url1 = "http://u.paperok.com/user/activity/"
driver.get(url1)
time.sleep(3)

# js="var q=document.documentElement.scrollTop=50"
# driver.execute_script(js)
# driver.find_element_by_css_selector('[type="file"]').click()
# driver.find_element_by_xpath("/html/body/div[last()]/div[2]/div[1]/ul/li[3]/form/p[1]/input[@type=[file]]").click()
# time.sleep(1)
# # driver.find_element_by_css_selector("input[type='file']").click()
driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[4]/h2").click()
time.sleep(2)
picture()
driver.find_element_by_name("file").send_keys(r"E:\Python\Py charm work\test spider\Some_Intersting\ccc5.png")
driver.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)
# Keys.ENTER()
alert = driver.switch_to.alert
alert.accept()
# driver.find_element_by_css_selector('[class="ui-button-icon ui-icon ui-icon-closethick"]').click()


time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[5]/h2").click()
time.sleep(2)
picture()
driver.find_element_by_name("file").send_keys(r"E:\Python\Py charm work\test spider\Some_Intersting\ccc5.png")
driver.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
# driver.find_element_by_name("file").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector('[class="ui-button-icon ui-icon ui-icon-closethick"]').click()


time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div/ul/li[6]/h2").click()
time.sleep(2)
picture()
driver.find_element_by_name("file").send_keys(r"E:\Python\Py charm work\test spider\Some_Intersting\ccc5.png")
time.sleep(2)
driver.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
# driver.find_element_by_name("file").send_keys(Keys.ENTER)
# driver.find_element_by_css_selector('[class="ui-button-icon ui-icon ui-icon-closethick"]').click()