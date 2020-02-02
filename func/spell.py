import random as r
import sqlite3
#import pymysql
from datetime import datetime

#___1______________________________________________________________________  
               
def pick(li,hm):
    
    re = set()                
    for i in range(hm) :
            a = r.choice(li)
            li.remove(a)           # no chance to pick what is already picked
            re.add(a)
            
    return list(re)

#___2_______________________________________________________________________  

def tot(seled_id):

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
    
    TwoDls = []
    for Id in seled_id:
            sql = 'select * from spelling where id = "%s"'%(Id)
            cur.execute(sql) 
            row = list(cur.fetchone())
            TwoDls.append(list(row[5:8]))
            t = sptime()                                    # 3
            sql = 'update spelling set UPtime = "%s" where id = "%s"'%(t,Id)
            cur.execute(sql)
            
    conn.commit()                     
    cur.close()
    conn.close()  
    
    return TwoDls    

#____3_______________________________________________________________________  
    
def sptime():
    a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return  a



#____s1_______________________________________________________________________    
      
def art():

    conn = sqlite3.connect('eng.sqlite')        
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor() 
    
    sql = 'SELECT article FROM `spelling` group by article'
    cur.execute(sql)

    art = []     
    for row in cur.fetchall():
            art.append(str(row[0]))   
     
    conn.commit()                     
    cur.close()
    conn.close()      
 

    return art    

#____s2_____________________________________________________________________  

def ALV(article):

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    alv = []     
    for i in range(1,6):
        sql = 'SELECT count(*) FROM `spelling` where article = "%s" and lv = "%s"'%(article,str(i))
        cur.execute(sql)
        a = cur.fetchone()
        a = a[0]
        if a:
            alv.append(a) 
        else:                  #--- if null, fill 0
            a = 0
            alv.append(a)    
      
    conn.commit()                     
    cur.close()
    conn.close()      

    return alv

#____s3_____________________________________________________________________  

def take_out_by_alv(ls,art):

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
       
    TwoDls = [[],[],[],[],[]]
    for i in range(5):

        ALLid = []
        if ls[i] :                                        # if not != 0
            a = i+1
            sql = 'select id from spelling where lv = "%s" and article = "%s"'%(str(a),art)
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))              
            TwoDls[i] = pick(ALLid,ls[i])                 # 1 

        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id

    conn.commit()                     
    cur.close()
    conn.close()      
    
    TwoDls = tot(seled_id)                                # 2

    return TwoDls 


#____s4_____________________________________________________________________ 
    
def allLV():

    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()  
    
    lilv = []
    for i in range(1,6):
        sql = 'select count(*) from spelling where lv = "%s"'%(i)
        cur.execute(sql)
        a = cur.fetchone()
        lilv.append(int(a[0]))
        
    conn.commit()                     
    cur.close()
    conn.close() 
    
    return lilv

#____s5_____________________________________________________________________     

def take_out_by_lv(ls):

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
      
    TwoDls = [[],[],[],[],[]]
    for i in range(5):
        ALLid = []
        if ls[i] :  # if not != 0
            a = i+1
            sql = 'select id from spelling where lv = "%s"'%(str(a))
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))                 # ls[i] = how many id we need
            TwoDls[i] = pick(ALLid,ls[i])           # 1 
        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id

    conn.commit()                     
    cur.close()
    conn.close()      
    
    TwoDls = tot(seled_id)                          # 2

    return TwoDls  
      
#_____s6____________________________________________________________________  
    
def IntimeR():

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    sql = 'SELECT max(INtime) FROM `spelling`'
    cur.execute(sql) 
    a = cur.fetchone()
    a = str(a[0])
    
    sql = 'SELECT min(INtime) FROM `spelling`'
    cur.execute(sql) 
    b = cur.fetchone()
    b = str(b[0])    
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    return a,b

#_____s7____________________________________________________________________
    
def JotimeR():

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    sql = 'SELECT max(JOtime) FROM `spelling`'
    cur.execute(sql) 
    a = cur.fetchone()
    a = str(a[0])
    
    sql = 'SELECT min(JOtime) FROM `spelling`'
    cur.execute(sql) 
    b = cur.fetchone()
    b = str(b[0])    
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    return a,b    

#_____s8_____________________________________________________________________  
    
def UptimeR():

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    sql = 'SELECT max(UPtime) FROM `spelling`'
    cur.execute(sql) 
    a = cur.fetchone()
    a = str(a[0])
    
    sql = 'SELECT min(UPtime) FROM `spelling`'
    cur.execute(sql) 
    b = cur.fetchone()
    b = str(b[0])    
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    return a,b 

#_____s9____________________________________________________________________

def DitimeR():
    
    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    sql = 'SELECT max(DItime) FROM `spelling`'
    cur.execute(sql) 
    a = cur.fetchone()
    a = str(a[0])
    
    sql = 'SELECT min(DItime) FROM `spelling`'
    cur.execute(sql) 
    b = cur.fetchone()
    b = str(b[0])    
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    return a,b 

#____s10____________________________________________________________________

def tO_Jtr(Trange): 
    
    lv = []
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor() 
    
    n = Trange[0]
    x = Trange[1]
    
    for i in range(1,6):
        sql = "select count(*) from spelling where lv = '%s' and JOtime between '%s' and '%s'"%(str(i),n,x)
        # i don't know why column name cannot %s, or else it will return (0,) only
        cur.execute(sql)
        a = cur.fetchone()
        lv.append(int(a[0]))
           
    conn.commit()                     
    cur.close()
    conn.close() 

    return lv

#____s11_____________________________________________________________________

def tO_Itr(Trange): 
    
    lv = []
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor() 
    
    n = Trange[0]
    x = Trange[1]
    
    for i in range(1,6):
        sql = "select count(*) from spelling where lv = '%s' and INtime between '%s' and '%s'"%(str(i),n,x)
        # i don't know why column name cannot %s, or else it will return (0,) only
        cur.execute(sql)
        a = cur.fetchone()
        lv.append(int(a[0]))
           
    conn.commit()                     
    cur.close()
    conn.close() 

    return lv    

#____s12_____________________________________________________________________
    
def tO_Utr(Trange): 
    
    lv = []
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor() 
    
    n = Trange[0]
    x = Trange[1]
    
    for i in range(1,6):
        sql = "select count(*) from spelling where lv = '%s' and UPtime between '%s' and '%s'"%(str(i),n,x)
        # i don't know why column name cannot %s, or else it will return (0,) only
        cur.execute(sql)
        a = cur.fetchone()
        lv.append(int(a[0]))
           
    conn.commit()                     
    cur.close()
    conn.close() 

    return lv  

#____s13_____________________________________________________________________

def tO_Dtr(Trange):
    
    lv = []
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor() 
    
    n = Trange[0]
    x = Trange[1]
    
    for i in range(1,6):
        sql = "select count(*) from spelling where lv = '%s' and DItime between '%s' and '%s'"%(str(i),n,x)
        # i don't know why column name cannot %s, or else it will return (0,) only
        cur.execute(sql)
        a = cur.fetchone()
        lv.append(int(a[0]))
           
    conn.commit()                     
    cur.close()
    conn.close() 

    return lv  

#_____s14____________________________________________________________________
    
def totJ(ls,Trange):
    
    n = Trange[0]
    x = Trange[1]

    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
      
    TwoDls = [[],[],[],[],[]]
    for i in range(5):
        ALLid = []
        if ls[i] :  # if not != 0
            a = i+1
            sql = 'select id from spelling where lv = "%s" and JOtime between "%s" and "%s"'%(str(a),n,x)
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))                 # ls[i] = how many id we need
            TwoDls[i] = pick(ALLid,ls[i])                 # 1
        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id
            
    conn.commit()                     
    cur.close()
    conn.close()  
    
    TwoDls = tot(seled_id)                                # 2
    
    return TwoDls 

#_____s15____________________________________________________________________

def totI(ls,Trange):
    
    n = Trange[0]
    x = Trange[1]
    
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()

    TwoDls = [[],[],[],[],[]]
    for i in range(5):
        ALLid = []
        if ls[i] :  # if not != 0
            a = i+1
            
            
            sql = 'select id from spelling where lv = "%s" and INtime between "%s" and "%s"'%(str(a),n,x)
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))                 # ls[i] = how many id we need
            TwoDls[i] = pick(ALLid,ls[i])                 # 1 
        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id
    
    conn.commit()                     
    cur.close()
    conn.close()      
    
    TwoDls = tot(seled_id)                                # 2
    
    return TwoDls  

#_____s16____________________________________________________________________
   
def totU(ls,Trange):
    
    n = Trange[0]
    x = Trange[1]
    
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
    
    TwoDls = [[],[],[],[],[]]
    for i in range(5):
        ALLid = []
        if ls[i] :  # if not != 0
            a = i+1
            sql = 'select id from spelling where lv = "%s" and UPtime between "%s" and "%s"'%(str(a),n,x)
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))                 # ls[i] = how many id we need
            TwoDls[i] = pick(ALLid,ls[i])                 # 1 
        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    TwoDls = tot(seled_id)                                # 2
    
    return TwoDls 

#_____s17____________________________________________________________________
    
def totD(ls,Trange):
    
    n = Trange[0]
    x = Trange[1]

    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
    
    TwoDls = [[],[],[],[],[]]
    for i in range(5):
        ALLid = []
        if ls[i] :  # if not != 0
            a = i+1
            sql = 'select id from spelling where lv = "%s" and DItime between "%s" and "%s"'%(str(a),n,x)
            cur.execute(sql)
            for row in cur.fetchall():
                ALLid.append(int(row[0]))                 # ls[i] = how many id we need
            TwoDls[i] = pick(ALLid,ls[i])                 # 1 
        else:
            TwoDls[i] = []

    seled_id = TwoDls[0]+TwoDls[1]+TwoDls[2]+TwoDls[3]+TwoDls[4]    # gether picked id
    
    conn.commit()                     
    cur.close()
    conn.close()  
    
    TwoDls = tot(seled_id)                                # 2
    return TwoDls

#_____s18____________________________________________________________________ 
    
def ulv(ls):   

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    for i in ls:  
        sql = 'update spelling set lv = "%s" where word = "%s"'%(i[4],i[0]) 
        cur.execute(sql)      

    conn.commit()                     
    cur.close()
    conn.close() 

#___0______________________________________________________________________
    
if __name__ == '__main__':
    print()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

