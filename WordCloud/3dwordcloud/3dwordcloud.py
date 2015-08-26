# -*- coding: utf-8 -*-
import re
import jieba
import os
from bs4 import BeautifulSoup
import codecs,re
from string import Template
from pytagcloud import *
from operator import itemgetter



Files= u'../ptt'
word_collect=""
for line in os.listdir(Files):
    File_List = os.path.join(Files,line)
    with codecs.open(File_List,'r','utf-8') as f:
            
        content=f.read()
        soup = BeautifulSoup(content)
        meta = soup.select('.article-meta-value')
        title = unicode(meta[2].text)
        #print '===================================\n',title,'\n','===================================\n'
        pushcontent_All=""
        for entry in soup.select('.push'):
            pushtag = entry.select('.push-tag')[0].text
            pushid = entry.select('.push-userid')[0].text
            pushcontent = entry.select('.push-content')[0].text
            pushtime = entry.select('.push-ipdatetime')[0].text
            pushcontent_All+=pushcontent
                
        sentence = pushcontent_All
        sentence_new = re.sub(u'[:/\\*?"|<>：\？\！。，,]',' ',pushcontent_All)      
        #print "Input：", sentence_new
        words = jieba.cut(sentence_new, cut_all=False)
        #print "Output 精确模式 Full Mode："
        '''
        for word in words:
            word_collect+=word
            print word
        '''
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
        swd = [w for w in swd[1:50] if len(w[0]) >= 2and w[1] >= 3]
        tags = make_tags(swd, maxsize=75)
        create_tag_image(tags,'wc.png', size=(600,600), fontname='SimHei')
        
        data = create_html_data(tags,
                        size=(600, 400),
                        layout=3,
                        fontname="SimHei",
                        rectangular=False)
        template_filename='tagtemplate.html'
        with open(template_filename) as f:
            html_template = Template(f.read())
            
        context = {}
        tags_template = '<li class="cn" style="top: %(top)dpx; left: %(left)dpx; \
        height: %(height)dpx;"><a class="tag \
        %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
        left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; \
        line-height:%(lh)dpx;">%(tag)s</a></li>'
        context['tags'] = ''.join([tags_template % link for link in data['links']])        
        html_text = html_template.safe_substitute(context)
        
        txt = html_text
        #print BeautifulSoup(txt).select('ul')[0];
        
        with open('3dwordcloud.html', 'w') as html_file:
            html_file.write(html_text.encode('utf-8'))
        


        