#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from HotIssue.views import IssueIndex
from HotIssue.views import NewsContext

from WebApi.Ajaxes import up_down_chart
from WebApi.Ajaxes import hotIssuesKeywordCloud
from WebApi.Ajaxes import heatIndex 
from WebApi.Ajaxes import OpinionLeader
from WebApi.Ajaxes import getTimeLine

from WebApi.Ajaxes import getDataWithKeyword
#for Dajax




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PttHotIssue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
    

    
    url(r'^index/$',IssueIndex) ,#首頁 ，熱門議題排行
    url(r'^index/art_(\d{1,})$',NewsContext) ,#熱門新聞
    
    
    url(r'^dajax/emotion$',up_down_chart) ,#推虛文
    url(r'^dajax/keywordcloud$',hotIssuesKeywordCloud) ,#熱議關鍵字雲
    
    url(r'^dajax/keywordHeatIndex$',heatIndex) ,#熱議指數折線圖
    url(r'^dajax/OpinionLeader$',OpinionLeader) ,#熱議意見領袖
    url(r'^dajax/TimeLine$',getTimeLine) ,#熱議意見領袖
    
    url(r'^dajax/data_with_keyword$',getDataWithKeyword) ,#熱議意見領袖
    
    url(r'^dajax/webapi/',include('WebApi.urls')) ,#Web Api
    #/dajax/OpinionLeader
    
)

