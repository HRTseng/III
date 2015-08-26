# -*- coding:utf-8 -*-
'''
Created on 2015年7月28日

@author: Cymon Dez
'''

import MySQLdb as sql
import redis  

import threading 
#----------------------------------
class SqlLinker(object):
    
    
    def __init__(self ,host = 'localhost',port = 3306,dbname = 'ptt',user = 'root',password = '',useUnicode = True):
        
        self.link_data = {
                          'host' : host,
                          'port' : port,
                          'dbname': dbname,
                          'user' : user,
                          'password' : password,
                          'useUnicode' : useUnicode,
                          }
        self.locker =  threading.Lock() 
        self.link(**self.link_data)
            
        
        pass
        
        
    
    def __del__(self):
        self.close()
    
    def link(self,host = 'localhost',port = 3306,dbname = 'ptt',user = 'root',password = '',useUnicode = True):
        if useUnicode :
            self._db_conn = sql.connect (host,user,password,dbname,charset='utf8')
        else :
            self._db_conn = sql.connect (host,user,password,dbname)
        
    
    
    def relink(self):
        print 'sql relink'
        self.close()
        self.link(**self.link_data)
        
    
    def close(self):
        if  self._db_conn :
            self._db_conn.close()
    
    def execute(self,cmd):
        def get_res(self):
            cursor = self._db_conn.cursor()
            cursor.execute(cmd)
            res = cursor.fetchall()
            return res
        
        
        self.locker.acquire()
        
        res = None
        cursor = None
        try :
#             cursor = self._db_conn.cursor()
#             cursor.execute(cmd)
#             res = cursor.fetchall()
            res =get_res(self)
        except sql.MySQLError as sql_err : # (errno ,message )
            errno = sql_err[0]
            if errno!= None and errno == 2006 :#lost server
                self.relink() 
                res =get_res(self)
                #retry again
        finally:
            if cursor :
                cursor.close()
                
            self.locker.release()
            return res
    
    def callproc(self,procedur_name,*args):   
        self.locker.acquire()
        ls = []
        cursor = None
        try :
            cursor = self._db_conn.cursor()
            
            cursor.callproc(procedur_name,list(args))
                        
            for res in cursor :
                
                ls.append(res)
        finally:
            if cursor :
                cursor.close()
            self.locker.release()
            return ls
    
#----------------------------------
class RedisLinker(object):
    pass    