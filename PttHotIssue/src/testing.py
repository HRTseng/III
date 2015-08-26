# -*- coding: utf-8 -*-
'''
Created on 2015年7月16日

@author: Cymon Dez
'''



from PttHotIssue import settings

import re 



# from HotIssue.models import mysqlLinker
# from HotIssue.models import hotIssueManager.

# print settings.TEMPLATE_DIRS
# 
# m  = re.search(r'art_(\d{1,})','127.0.0.1:8000/index/art_140000' )
# print m.group(1)


 

from WordCutLibs import wordCloudlib
import thread

wordCloudlib.get_wordcloud_Tags(u"""
作者Ipanema (blue)看板Gossiping標題[新聞] 八仙塵爆案第7死　萬能科大林芷妘不治時間Thu Jul 16 15:51:29 2015
1.媒體來源: 蘋果即時
 
 
2.完整新聞標題: 八仙塵爆案第7死　萬能科大林芷妘不治
 
 
3.完整新聞內文:
 
2015年07月16日15:44
憾！八仙塵爆案第7死！就讀萬能科大的林芷妘（19歲），全身有百分之81的深二度到三
度灼傷，灼傷範圍包括顏面、四肢及軀幹，且併發吸入性肺灼傷，在6月28日轉到衛福部
桃園醫院治療，因呼吸困難故緊急插管治療。
 
7月2日因呼吸衰竭接受葉克膜治療，狀況逐漸改善；7月7日脫離葉克膜，並進行多次傷口
清創。7月15日因感染導致敗血症，併發多重器官衰竭，再度接受葉克膜治療，經醫療團
隊與家屬討論後，家人不忍讓她再受苦痛，16日下午3時30分移除葉克膜拔管。（突發中
心／桃園報導）
 
 
4.完整新聞連結 (或短網址):
 
http://www.appledaily.com.tw/realtimenews/article/local/20150716/649283/
 
5.備註:
 
""",st= 0,end = 50)

#res = mysqlLinker.callproc('Get_Top','20150731','20150805',300)
#print res



