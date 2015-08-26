#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response


import random

from HotIssue import models as mdl 
from HotIssue.models import hotIssueManager
from WordCutLibs import wordCloudlib as wdlib
from WordCutLibs import HotIssueGroup as hotGroup
# Create your views here.


#----------------------------------------------------------


def IssueIndex(request):

     
    hotIssues = mdl.get_News_top10_in_a_week()

    return render_to_response('index.html',locals())

#-------------------------------------------------------------
def _get_index_by_artId(articles,art_id):
    
    for idx in xrange(0,len(articles)) :
        
        if long(articles[idx].art_id) == long(art_id) :
            
            return idx
    return -1


def NewsContext(requests,art_id):
        
    article = hotIssueManager.get_articles_by_id(art_id, with_pushtxt = True) 
    content =u''.join([ item.context  for item in article.pushtxts])
    
    wds = wdlib.get_wordcloud_Tags(content)   
    
    articles = mdl.get_Article_top1000_in_a_week()
    
    base_art_index = _get_index_by_artId(articles,art_id)
    
    
    #關聯新聞
    related_news = hotGroup.get_related_news(articles, base_art_index)[0:5]
    
    
    
    ls = mdl.get_News_top10_in_a_week()
    crntIdx = _get_index_by_artId(ls,art_id)
    rg =  range(0,10);
    if  crntIdx in rg :
        rg.remove( crntIdx )

    randIndex = random.sample(rg, 5)
    randIndex.sort()
    
    

    
    #
    hotIssues = [ ls[i] for i in randIndex  ]
    return render_to_response('Issue.html',locals())

    pass

