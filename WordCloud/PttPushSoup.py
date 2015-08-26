# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
import codecs
import re

Files= u'/ptt'
Err_msg=""
for line in os.listdir(Files):
    File_List = os.path.join(Files,line)
    try:
        with codecs.open(File_List,'r','utf-8') as f:
            upvotecount=0
            content=f.read()
            soup = BeautifulSoup(content)
            meta = soup.select('.article-meta-value')
            title = unicode(meta[2].text)
            print '===================================\n',title,'\n','===================================\n'
            for entry in soup.select('.push'):
                pushtag = entry.select('.push-tag')[0].text
                pushid = entry.select('.push-userid')[0].text
                pushcontent = entry.select('.push-content')[0].text
                pushtime = entry.select('.push-ipdatetime')[0].text
                NewPushContent=re.sub(r'[:/\\*?"|<>]','',pushcontent)
                if pushtag==u"推 ":
                    upvotecount+=1
                print pushtag,NewPushContent,upvotecount
    except Exception as e:
              
        print Err_msg 
        
        
               
                 
            