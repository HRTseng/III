#-*- encoding: utf-8 -*-
'''
Created on 2015年8月12日

@author: BigData
'''

from WebApi import Ajaxes
from HotIssue.models import hotIssueManager
from WordCutLibs.HotIssueGroup import get_related_news

# import thread
# 
# 
# def thread_fun(arts,range):
#     for i in range :
#         print u'\t',arts[i].title
#         get_related_news(arts,i)

def loadCache():
    
    print 'cache loading !'
   
    
    datas = Ajaxes._gethik()
    
    
    for kw ,cnt in datas:
        print '\t loading...... ',kw
        Ajaxes._getdwk(kw)
    
    
    print 'cache finished !'
    #-------------------------------
#     print 'loading relative news '
    
#     arts = hotIssueManager.get_Article_top1000_in_a_week()
#     max_b = 10
#     for i in xrange(0,max_b) :
#         print u'\t',arts[i].title
#         get_related_news(arts,i)
#     
#     
#     for i in xrange(0,max_b):
#         thread.start_new_thread(thread_fun, (arts,range(0*i,100*i))) 
    
#     
#     print 'load relative news finished !'
    
loadCache()