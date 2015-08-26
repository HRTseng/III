#-*- encoding: utf-8 -*-
'''
Created on 2015年8月4日

@author: BigData
'''
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^webapi.js$','WebApi.views.web_api_file') ,   # Web Api js file
)