# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.
import os
from django.http import HttpResponse

from PttHotIssue import settings 


def web_api_file(requsts):
    

    
    with open( os.path.join( settings.TEMPLATE_DIRS[0] ,'webapi.js' ),'r') as f :
        txt = f.read()
        
    response = HttpResponse(txt, content_type="text/javascript") # mimetype 已作廢 ， 請使用  content_type

    return response 