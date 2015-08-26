# -*- coding:utf-8

#from django.db import models

#from django.db import connection

#from __future__ import unicode_literals

from SqlLinker import SqlLinker
#SQL Data Models
# Create your models here.

        
mysqlLinker = SqlLinker(host='localhost',
                        port=3306,
                        dbname='ptt',
                        user='root',
                        password='',
                        useUnicode = True
                        )


def get_News_top10_in_a_week():

    
    return hotIssueManager.get_News_top10_in_a_week()

def get_Article_top1000_in_a_week():

    return hotIssueManager.get_Article_top1000_in_a_week()


def get_OpinionLeader(group_artids):
    
    return hotIssueManager.get_OpinionLeader(group_artids)

class HotIssueManager(object):
    
    def __init__(self,linker):
        self._linker = linker
    
    def get_News_top10_in_a_week(self):

        sqlQurey = "SELECT  title ,push_cnt ,art_id FROM push_Top10_with_title_mem"
        res = self._linker.execute(sqlQurey)
        return [HotIssueItem(title,push_cnt,art_id)  for title ,push_cnt ,art_id in res ]

    def get_Article_top1000_in_a_week(self):

        sqlQurey = """SELECT art_id, author ,title ,post_time ,url ,context 
                        FROM article 
                        WHERE art_id IN (
                                        SELECT art_id 
                                        FROM push_top1000_in_a_week_mem
                                        )
                        ORDER BY post_time"""
        res = self._linker.execute(sqlQurey)
        
        return [ArticleItem(art_id, author ,title ,post_time ,url ,context)  
                for art_id, author ,title ,post_time ,url ,context in res ]
    
    def get_Issue_top10_in_a_week(self):
        #???????
        sqlQurey = """SELECT title, context,art_id
                        FROM article 
                        WHERE art_id IN (
                                        SELECT art_id 
                                        FROM push_top1000_in_a_week_mem
                                        )
                        ORDER BY post_time"""
        res = self._linker.execute(sqlQurey)
        
        
        
        return [HotIssueItem(title,push_cnt,art_id)  for art_id ,title ,push_cnt in res ]
    
    
    
    def get_articles_by_id(self,art_id,with_pushtxt = False):
        pushtxts = None
        if with_pushtxt :
            cmd = """ select  author ,push_type ,post_time ,context
                      from pushtxt 
                      where art_id = {0}
                        
                     """.format(art_id)
            
            res = self._linker.execute(cmd)
            
            pushtxts = [ PushtxtItem(author ,push_type ,post_time ,context ) for author ,push_type ,post_time ,context  in res  ] if res != None else []
        else :
            pushtxts = []
        
        cmd = """ select author ,title ,post_time ,url ,context
                      from article 
                      where art_id = {0}
                        
                     """.format(art_id)
            
        res = self._linker.execute(cmd)
        
        art_item  = ArticleItem(art_id,pushtxts=pushtxts, *(res[0]))
        return art_item    
        
    def get_pushtypes_by_id(self,art_id):
        cmd = """ select count(push_type = 'upvote' or null) as upvote ,
                        count(push_type = 'normal' or null) as normal ,
                        count(push_type = 'downvote' or null) as downvote 
                      from pushtxt 
                      where art_id = {0}
                        
                     """.format(art_id)
            
        res = self._linker.execute(cmd)
        
        return res[0]
        
#取得意見領袖   發文數/推文數 top10
    def get_OpinionLeader(self,keyword):
        
        
        
        #取得發文最多者
        cmd =u"""select  count(p.push_type) as push_cnt,
                          a.author as author ,
                          a.title as title     ,
                          a.art_id as art_id

                from article as a join pushtxt as p on (a.art_id = p.art_id)
                
                where (a.title like '[問卦]%{0}%' or a.title like '[爆掛]%{0}%' or a.title like 'Re:%{0}%' )
                        and( a.post_time between  DATE_SUB( CURDATE(),INTERVAL 30 DAY  )  and DATE_SUB( CURDATE(),INTERVAL 1 DAY  ) )
                group by p.art_id
                order by push_cnt desc
                limit 5;        
        """.format(keyword)
        #print cmd
            
        res = self._linker.execute(cmd)
        
        
        return res
#時間軸
    def get_TimeLine(self,keyword):
        
        least_cnt = 750
        
        cmd =u"""
        
                
        select DATE_FORMAT(min(s.dayofmonth),'%Y-%m-%d') as st ,DATE_FORMAT(max(s.dayofmonth),'%Y-%m-%d') as end
        from 
            (SELECT     DATE(a.post_time) as dayofmonth
            FROM article as a join pushtxt as p on (a.art_id = p.art_id)
            WHERE  (a.title like '%{0}%'  )
                   and ( a.post_time between  DATE_SUB( CURDATE(),INTERVAL 30 DAY  )  and DATE_SUB( CURDATE(),INTERVAL 1 DAY  ) ) 
            GROUP BY Date(a.post_time)
            having COUNT(p.push_type!='normal' or null) > {1}
             ) s
        ;      
        """.format(keyword,least_cnt)
        #print cmd
            
        res = self._linker.execute(cmd)
        
        
        return res

#取得議題熱度指數 ex :
#     issueHeatIndex = {'name' : '八仙',
#                       heats :[
#                               {date : '08/09' ,pushtypes:[217,113] },
#                               
#                               ]
#                       }  
    
    def get_heatIndex(self,keywords ,columnName = u'title'):
        cmd=u"""
        select * from  (SELECT DATE_FORMAT(a.post_time,'%m/%d') as dayofmonth,
        COUNT(p.push_type= 'upvote' or null) as upvote,
        COUNT(p.push_type= 'downvote' or null) as downvote, 
        COUNT(p.push_type!='normal' or null) as 'total'
        FROM article as a join pushtxt as p on (a.art_id = p.art_id)
        WHERE  {0}
               and ( a.post_time between  DATE_SUB( CURDATE(),INTERVAL 30 DAY  )  and DATE_SUB( CURDATE(),INTERVAL 1 DAY  ) ) 
        GROUP BY Date(a.post_time)
        order by dayofmonth desc limit 7) as tmp
        order by tmp.dayofmonth
        ;
        """.format(self._create_qurey_kws(keywords+u" ^公告",u'a.title'))
        
        res = self._linker.execute(cmd)
        eles = []
        for woy ,up ,down ,total in res :
            eles.append([str(woy),int(up),int(down),int(total)])
        
        return eles
    
    
    
    
    def _create_qurey_kws(self,keywords ,columnName = u'title'):
        words = keywords.split()
        l = len(words)
        res = u' ( '
        for i in xrange(0,l) :
            s = words[i]
            
                   
            not_str = u''
            if s.startswith(u'^') :
                not_str = u'not'
                s = s[1:]
            if s == '' :
                continue    
            res += u" {0} {1} like '%{2}%'  ".format(columnName,not_str,s)
            if i != l-1 :
                res+=u" and " 
        
        res+= u' )'
        return res

    def search(self,keyword,columnName):
        
        sql = ( u"""SELECT art_id , title FROM article Where  """ 
                + self._create_qurey_kws(keyword,columnName) )
        
        res = self._linker.execute(sql)
        return res



#------- Hot Issue Item ---------------


class HotIssueItem(object):
    def __init__(self ,title ,push_cnt ,art_id):
        self.title = title
        self.push_cnt = push_cnt
        self.art_id = long(art_id)

#end Class HotIssueItem

class HotIssueGroup(object):
    def __init__(self ,keyword ,issuses):
        self.keyword = keyword
        self.issuses = issuses
        pass 
    pass
#end class HotIssueGroup

#------- ArticleItem --------------- 
class ArticleItem(object):
    def __init__(self,art_id,  author ,title ,post_time ,url ,context ,pushtxts=[]):
        self.art_id = long(art_id)
        self.author = author
        self.title = title
        self.post_time = post_time
        self.url = url
        self.context = context
        
        if pushtxts :
            self.pushtxts = pushtxts
        else :
            self.pushtxts = []
    def __unicode__(self):
        s =  self.context+u'\n    ------推文-----    \n'
        
        for p in self.pushtxts :
            #(pushid ,push_type,pushtime ,pushcontext)
            s+=  unicode(p)+u'\n'
            
        
        return s
#end class ArticleItem

class PushtxtItem(object):
    pushTypeSwitch = {
                       u'推':'upvote',
                       u'噓':'downvote',
                       u'→':'normal'
                      }
    convertToPushTypeSwitch = {
                       'upvote':u'推',
                       'downvote':u'噓',
                       'normal':u'→'
                      }
    def __init__(self,  author ,push_type ,post_time ,context ):
        self.author = author
        self.push_type = push_type
        self.post_time = post_time
        self.context = context
        
    def convert_pushtype(self):
        return     PushtxtItem.convertToPushTypeSwitch.get(self.push_type)
    
    def __unicode__(self):
        s = self.convert_pushtype()+u'　' + unicodeAlign( self.author,15) +  u'　\t\t'  +unicodeAlign( self.context ,5) #+ u'\t　'  +unicodeAlign(unicode( self.post_time),5)
        return s

#end class PushtxtItem       

def unicodeAlign(string, length=0):  
    if length == 0:  
        return string  
    slen = len(string)  
    re = string  
    if isinstance(string, str):  
        placeholder = ' '  
    else:  
        placeholder = u' ' # u'　'  
    while slen < length:  
        re += placeholder  
        slen += 1  
    return re         


hotIssueManager = HotIssueManager(mysqlLinker)