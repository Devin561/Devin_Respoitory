#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
from PIL import Image, ImageDraw, ImageFont
import numpy as np

num = np.random.randint(1000, 99999)
im1 = Image.open("ccc.png").convert('RGBA')
txt = Image.new('RGBA', im1.size, (0,0,0,0))
fnt = ImageFont.truetype('C:/Windows/Fonts/simhei.ttf', 18)
d = ImageDraw.Draw(txt)
d.rectangle((220,72,250,102), fill= 'white')
d.text((220, 72),"{0}".format(num), font = fnt, fill="black")

out = Image.alpha_composite(im1, txt)
out.save(r'ccc4.png')


