#-*- encoding: utf-8 -*-
'''
Created on 2015年8月3日

@author: BigData
'''
from django.http import JsonResponse

from HotIssue.models import hotIssueManager

from WordCutLibs.wordCloudlib import create_word_cloud
from django.http import HttpResponse

def up_down_chart(request):
    
    art_id = None
    if request.method == 'GET':
        art_id = request.GET['art_id']
        
    
    up ,nor ,down = hotIssueManager.get_pushtypes_by_id(art_id)
    data = {
            'upvote':up ,
            'normal':nor,
            'downvote':down
            }
    
    response =JsonResponse(data)
    
#     response["Access-Control-Allow-Origin"] = "*"
#     response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
#     response["Access-Control-Max-Age"] = "1000"
#     response["Access-Control-Allow-Headers"] = "*"
#     response['content-type']="text/javascript"
    

    return response


def _gethik():
    datas = []
    


    datas.append((u'颱風',33))
    datas.append((u'宋楚瑜',30))
    datas.append((u'微調',29))
    datas.append((u'教育部',26))
    datas.append((u'吳思華',21))
    datas.append((u'蔡英文',21))
    datas.append((u'教科書',20))
    datas.append((u'賴清德',18))
    datas.append((u'歷史',16))
    datas.append((u'洪秀柱',12))
    datas.append((u'女友',12))
    datas.append((u'活動',12))
    datas.append((u'年輕人',10))
    
    return datas

def hotIssuesKeywordCloud(request):
    
    datas = _gethik()

   
    html_text = create_word_cloud(datas,wdsize = (500,250),style_3d=False)
    response = HttpResponse(html_text, content_type="html")
    return response


heatIndexCache = {}

def heatIndex(request):
    kw = None
    if request.method == 'GET':
        kw = request.GET['keyword']
    
    eles = hotIssueManager.get_heatIndex(kw) if kw not in heatIndexCache else heatIndexCache[kw]
    heatIndexCache[kw] = eles;
    json = {}
    
    json['datas'] = ([ [u'near 30 days', u'正向', u'反向', u'全部']  ])
    
    for e in eles :
        json['datas'].append(e)
    
    json['title'] = kw + u'議題    熱度指數'
    
    
    
    response =JsonResponse(json)
    return response
    pass

OpinionLeaderCache = {}

def OpinionLeader(request):
    keyword = None
    if request.method == 'GET':
        keyword = request.GET['keyword']
        
    authors = []
    
    res = hotIssueManager.get_OpinionLeader(keyword) if keyword not in OpinionLeaderCache   else OpinionLeaderCache[keyword]
    if res is not None :
        OpinionLeaderCache[keyword] = res
    #cnt ,author_name ,title 
    
    for cnt ,author ,title ,art_id in res :
        authors.append([cnt,author,title,art_id])

    json = {'authors':authors}
    response =JsonResponse(json)
    return response


TimeLineCache = {}

def getTimeLine(request):
    kw = None
    if request.method == 'GET':
        kw = request.GET['keyword']
    
    eles = hotIssueManager.get_TimeLine(kw) if kw not in TimeLineCache else TimeLineCache[kw]
    if eles is not None :
        TimeLineCache[kw] = eles;
    
    json = {'timeLine':[eles[0][0] , eles[0][1]]}
    
    
    
    
    
    response =JsonResponse(json)
    return response
    


def _getdwk(kw):
    
    json = {}
    
    
    #熱度指數
    hi = hotIssueManager.get_heatIndex(kw) if kw not in heatIndexCache else heatIndexCache[kw]
    heatIndexCache[kw] = hi;
    
    
    hidatas = [ [u'near 30 days', u'正向', u'反向', u'全部']  ]
    
    for e in hi :
        hidatas.append(e)
    
    json['heatIndexes'] = {'title' :kw + u'議題    熱度指數',
                           'datas':hidatas                           
                           }
    
    
    #意見領袖
    ol = hotIssueManager.get_OpinionLeader(kw) if kw not in OpinionLeaderCache   else OpinionLeaderCache[kw]
    if ol is not None :
        OpinionLeaderCache[kw] = ol
    #cnt ,author_name ,title 
    authors = []
    for cnt ,author ,title ,art_id in ol :
        authors.append([cnt,author,title,art_id])
    
    json['opinionLeaders'] = {'authors':authors}
    
    #時間軸
    eles = hotIssueManager.get_TimeLine(kw) if kw not in TimeLineCache else TimeLineCache[kw]
    if eles is not None :
        TimeLineCache[kw] = eles;
    
    json['timeLine'] =[eles[0][0] , eles[0][1]]
    
    return json


def getDataWithKeyword(request):
    kw = None
    if request.method == 'GET':
        kw = request.GET['keyword']
    
    json = {}
    
    
    #熱度指數
    hi = hotIssueManager.get_heatIndex(kw) if kw not in heatIndexCache else heatIndexCache[kw]
    heatIndexCache[kw] = hi;
    
    
    hidatas = [ [u'near 30 days', u'正向', u'反向', u'全部']  ]
    
    for e in hi :
        hidatas.append(e)
    
    json['heatIndexes'] = {'title' :kw + u'議題    熱度指數',
                           'datas':hidatas                           
                           }
    
    
    #意見領袖
    ol = hotIssueManager.get_OpinionLeader(kw) if kw not in OpinionLeaderCache   else OpinionLeaderCache[kw]
    if ol is not None :
        OpinionLeaderCache[kw] = ol
    #cnt ,author_name ,title 
    authors = []
    for cnt ,author ,title ,art_id in ol :
        authors.append([cnt,author,title,art_id])
    
    json['opinionLeaders'] = {'authors':authors}
    
    #時間軸
    eles = hotIssueManager.get_TimeLine(kw) if kw not in TimeLineCache else TimeLineCache[kw]
    if eles is not None :
        TimeLineCache[kw] = eles;
    
    json['timeLine'] =[eles[0][0] , eles[0][1]]
    
    
    
    response =JsonResponse(json)
    return response