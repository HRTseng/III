#-*- encoding: utf-8 -*-
'''
Created on 2015年7月21日

@author: BigData
'''

import re
import jieba
from pytagcloud import make_tags
from pytagcloud import create_html_data
from pytagcloud.colors import COLOR_SCHEMES

from string import Template

from operator import itemgetter
import WordCutLibs

import random
import uniout


tags_template = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; \
    height: %(height)dpx;"><a class="tag \
    %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
        left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; \
    line-height:%(lh)dpx;" onclick = "clickKeywordAction(\'%(tag)s\')" >%(tag)s</a></li>'

tags_template_3d = '<li class="cnt" style="top: %(top)dpx; left: %(left)dpx; \
    height: %(height)dpx;"><a class="tag \
    %(cls)s" href="#%(tag)s" style="top: %(top)dpx;\
        left: %(left)dpx; font-size: %(size)dpx; height: %(height)dpx; \
    line-height:%(lh)dpx;">%(tag)s</a></li>'

html_template =Template( '''
        
        <style type="text/css">
            a.tag{
                font-family: 'PMingLiU', 'Sans';
                text-decoration: none;
            }
            li.cnt{
                overflow: hidden;
                position: absolute;
                display: block;
            }
            ul.cloud{
                position: relative;
                display: block;
                width: ${width}px;
                height: ${height}px;
                overflow: hidden;
                margin: 20 20;
                padding: 10;
                list-style: none;
            }
            $css
        </style>

        <ul class="cloud">
            $tags
        </ul>
''')
html_template_3d =Template( '''
        
        <style type="text/css">
            a.tag{
                font-family: 'PMingLiU', 'Sans';
                text-decoration: none;
            }
            li.cnt{
                overflow: hidden;
                position: absolute;
                display: block;
            }
            ul.cloud{
                position: relative;
                display: block;
                width: ${width}px;
                height: ${height}px;
                overflow: hidden;
                margin: 20 20;
                padding: 10;
                list-style: none;
            }
            $css
        </style>

        <div id="myCanvasContainer">
            <canvas width="450" height="300" id="myCanvas">
                <p>Anything in here will be replaced on browsers that support the canvas element</p>
            </canvas>
    
        
            <ul class="cloud" id="cloud">
                $tags
            </ul>
    
        </div>
''')

def wordCount(words ,ignore_pattern =u'\s|XD{1,}|\.{1,}|…'):
    wdic = {}
    for w in words :
        if re.match(ignore_pattern,w) :
            continue
            
        if w not in wdic:
            wdic[w] = 1
        else :
            wdic[w] += 1
    
    return wdic
    
def cut_content( content ) :
                    
    words = jieba.cut(content, cut_all=False)
    
    for word in words:
        if word not in WordCutLibs.stopwords:
            yield word    
    
 

def create_word_cloud(swd,fontName = "PMingLiU",wdsize = (600,400),style_3d = True):
    tags = make_tags(swd,
                      minsize= 15,
                      maxsize= 75,
                      #colors=random.choice(COLOR_SCHEMES.values())
                      #colors=COLOR_SCHEMES['oldschool']
                      #colors=COLOR_SCHEMES['citrus']
                      
                      #colors=COLOR_SCHEMES['goldfish']
                      #colors=COLOR_SCHEMES['audacity']
                      
                      )

    data = create_html_data(tags,
                    size = wdsize,
                    layout=3,
                    fontname=fontName,
                    rectangular=False) 

    tag_tmp = tags_template_3d if style_3d else tags_template
    
    context = {}
    context['tags'] = ''.join([tag_tmp % link for link in data['links']])
    context['width'] = data['size'][0]
    context['height'] = data['size'][1]
    context['css'] = "".join("a.%(cname)s{color:%(normal)s;}\
                         a.%(cname)s:hover{color:%(hover)s;}" %
                         {'cname': k,
                          'normal': v[0],
                          'hover': v[1]}
                         for k, v in data['css'].items())
    
    html_text =  html_template_3d.safe_substitute(context) if style_3d else  html_template.safe_substitute(context)
    
    return html_text
    

def get_wordcloud_Tags(content,st = 0,end = 20,min_word_len = 2,min_count = 1,ignore_pattern =u'[:/\\*?"|<>：\？\！。，,]'):
    
    content = re.sub(ignore_pattern,u' ',content)
    
    words = cut_content(content)
    
    wc = wordCount(words)
    
    swd = sorted(wc.iteritems(), key=itemgetter(1), reverse=True)
    
    
    swd = [w for w in swd if len(w[0]) >= min_word_len and w[1] >= min_count]
    
    #print swd
    
    maxIndex= len(swd) -1
    end = end if end <= maxIndex else maxIndex
    swd = swd[st:end]
    return create_word_cloud(swd)
    