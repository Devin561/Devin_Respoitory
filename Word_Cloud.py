#!/usr/bin/env python3
#coding:utf-8
#Author: Devin561
#E-Mail: zengzhen561@163.com
import jieba
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from scipy.misc import imread
# from docx import Document

# text = Document(r'E:\Python\Py charm work\test spider\thesis.docx')
text = open(r'E:\Python\Py charm work\test spider\TXF.txt', 'r')
mylist = list(text)
word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
new_text = ' '.join(word_list)
color_mask = imread(r'E:\Python\Py charm work\test spider\heart.jpg')

wordcloud = WordCloud(font_path="STSONG.TTF", background_color='white', mask=color_mask,
                      random_state=30).generate(new_text)
text.close()
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
