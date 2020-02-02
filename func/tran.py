#import pymysql
import sqlite3
from datetime import datetime


#___t1_______________________________________________________________________ 

def howManyJW():
    
     conn = sqlite3.connect('eng.sqlite')
#     conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
     cur = conn.cursor()
     
     sql = 'select count(*) from joining'
     cur.execute(sql)       
     JW = cur.fetchone()[0]
          
     conn.commit()
     cur.close()
     conn.close()  
     
     return JW
 
#___t2_______________________________________________________________________ 
     
def takeoutASE(num):
    
     conn = sqlite3.connect('eng.sqlite')
#     conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
     cur = conn.cursor()    

     sql = 'select word from joining order by id asc limit "%s"'%(num)
     cur.execute(sql)
       
     Ws = []
     for row in cur.fetchall():
          Ws.append(row[0])

     conn.commit()
     cur.close()
     conn.close()  
     
     return Ws     

#___t3_______________________________________________________________________     
     
 
def takeoutDESC(num):

     conn = sqlite3.connect('eng.sqlite')
#     conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
     cur = conn.cursor()    

     sql = 'select word from joining order by id desc limit "%s"'%(num)
     cur.execute(sql)       
     Ws = []
     for row in cur.fetchall():
          Ws.append(row[0])

     conn.commit()
     cur.close()
     conn.close()  
     
     return Ws   
 
#__t4_______________________________________________________________________ 
    
def join_to_spellingASC(num,lv):
     
     conn = sqlite3.connect('eng.sqlite')
#     conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
     cur = conn.cursor()
     
     sql = 'select * from joining order by id asc limit "%s"'%(num)
     cur.execute(sql)  
     
     J = []

     for row in cur.fetchall():
         J.append(list(row)[1:7]) 
     
     for i in range(num):
         try:
             a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             sql = '''insert into spelling 
                     (JOtime,word,attribute,translation,lv,article,INtime) 
                     values("%s","%s","%s","%s","%s","%s","%s")'''%(J[i][0],J[i][2],J[i][3],J[i][4],str(lv[i]),J[i][5],a)
             cur.execute(sql) 
             
  
             if J[i][1]:
                 sql = 'update spelling set DItime = "%s" where word = "%s"'%(J[i][1],J[i][2])  
                 cur.execute(sql)
  
                 
         except:
             sql = 'update spelling set lv = "%s" where word = "%s"'%(str(lv[i]),J[i][2])
             cur.execute(sql)               # 'basic' may already inputed word to spelling
                                                                  #  skiped joining
           
     sql = '''
         delete from joining where id <= (
         select max(id) from (
         select id from joining order by id limit 0, "%s"));'''%(num)
     cur.execute(sql)    
     
     conn.commit()
     cur.close()
     conn.close()  

#__t5_______________________________________________________________________ 
     
def join_to_spellingDESC(num,lv):
    
     conn = sqlite3.connect('eng.sqlite')
#     conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
     cur = conn.cursor()
     
     sql = 'select * from joining order by id desc limit "%s"'%(num)
     cur.execute(sql)  
              
     J = []

     for row in cur.fetchall():
         J.append(list(row)[1:7])    
         
         
     for i in range(num):
         try:
             a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
             sql = '''insert into spelling 
                     (JOtime,word,attribute,translation,lv,article,INtime) 
                     values("%s","%s","%s","%s","%s","%s","%s")'''%(J[i][0],J[i][2],J[i][3],J[i][4],str(lv[i]),J[i][5],a)
             cur.execute(sql) 
             
        
             if J[i][1]:
                 sql = 'update spelling set DItime = "%s" where word = "%s"'%(J[i][1],J[i][2])  
                 cur.execute(sql)
   
                 # or sqlite will insert none, (default null) , and think it is max value in DItime
         except:
             sql = 'update spelling set lv = "%s" where word = "%s"'%(str(lv[i]),J[i][2])
             cur.execute(sql)               # 'basic' may already inputed word to spelling
                                                                  #  skiped joining
                                                                
     sql = '''
         delete from joining where id >= (
         select min(id) from (
         select id from joining order by id  desc limit 0, "%s"));'''%(num)       
        
#     sql = 'delete from joining order by id desc limit "%s"'%num    #< sqlite cannot do this
     cur.execute(sql) 
     
     conn.commit()
     cur.close()
     conn.close()  
     
    
#___0_______________________________________________________________________     
if __name__ == '__main__':
    print()

