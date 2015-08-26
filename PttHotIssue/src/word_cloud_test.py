#-*- encoding: utf-8 -*-
'''
Created on 2015年8月7日

@author: BigData
'''
# -*- coding: utf-8 -*-
import re,os
import jieba,jieba.analyse
import MySQLdb
import codecs,re
from string import Template
from pytagcloud import *
from operator import itemgetter
from WordCutLibs import wordCloudlib as wc
import uniout

word_collect=""
pushcontent_All=""

sentence = ''
with codecs.open(u'E:/ptt/[Title][問卦] 被告要多久才收得到傳票[Author]l90lT (陸軍1901梯)[Date]Thu Aug  6 21-45-09 2015.txt','r','utf-8') as f :
    sentence = f.read()

wc.get_wordcloud_Tags(sentence, 0, 20, 1, 1)

words = jieba.cut(sentence, cut_all=False)
    #print "Output 精确模式 Full Mode："

wdic = {}
for w in words :
    if re.match('\s|XD{1,}|\.{1,}|…',w) :
        continue
        
    if wdic.get(w) is None :
        wdic[w] = 1
    else :
        wdic[w] += 1
            
swd = sorted(wdic.iteritems(), key=itemgetter(1), reverse=True)
for w in swd :
    if len(w[0]) >= 2and w[1] >= 3  :
        pass
        print w[1],'\t',w[0] 
swd = [w for w in swd[1:30] if len(w[0]) >= 2 and w[1] >= 1]

tags = make_tags(swd, maxsize=75)
create_tag_image(tags, 'E:\\'+'wc.png', size=(600,600), fontname='SimHei')
    
data = create_html_data(tags,
                size=(600, 400),
                layout=3,
                fontname="Droid Sans",#"SimHei",
                rectangular=False)

# template_filename='E:\\templatedweb\\tagcanvas\\'+'tagtemplate.html'
# with open(template_filename) as f:
#         html_template = Template(f.read())
#          
# context = {}
# tags_template = '<li class="cn" style="top: %(top)dpx; left: %(left)dpx; \
#     height: %(height)dpx;"><a class="tag \
#     %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
#     left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; \
#     line-height:%(lh)dpx;">%(tag)s</a></li>'
# context['tags'] = ''.join([tags_template % link for link in data['links']])        
# html_text = html_template.safe_substitute(context)
#     
# txt = html_text
#     #print BeautifulSoup(txt).select('ul')[0];
#     
# with open('E:\\3dcloud.html', 'w') as html_file:
#     html_file.write(html_text.encode('utf-8'))
