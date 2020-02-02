from datetime import datetime
import sqlite3
#import pymysql
import csv

#__b1_______________________________________________________________________
def fill_basic():
    
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    with open('trash.csv',encoding = 'utf-8-sig') as f :

        cR = csv.reader(f)
        for row in cR: 
            try :
                cur.execute('INSERT INTO trash VALUES("%s","%s")'%(row[0],row[1])) 
            except:
                continue             # in case it already in    

    with open('basic.csv',encoding = 'utf-8-sig') as f :

        cR = csv.reader(f)
        for row in cR:
     
            a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            b = str(row[0])
            c = str(row[1])
            d = str(row[2])
            e = '1'
            f = 'basic'
            
            try :
                sql = '''insert into spelling (JOtime,word,attribute,translation,
                        lv,article) values("%s","%s","%s","%s","%s","%s")'''%(a,b,c,d,e,f)
                cur.execute(sql) 
            except:
                continue
            
    conn.commit()
    cur.close()
    conn.close() 

#__b2_______________________________________________________________________
def fill_lemma():
    
    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    

    with open('lemma.csv',encoding = 'utf-8-sig') as f :
        cR = csv.reader(f)
        for row in cR:
            try:
#                cur.execute('INSERT INTO eng.lemma (trans,word) VALUES (%s, %s)', row)   
                cur.execute('INSERT INTO lemma (trans,word) VALUES ("%s", "%s")'%(row[0],row[1]))
            except:
                continue

    conn.commit()
    cur.close()
    conn.close() 
#__b3_______________________________________________________________________
        
def built_tables():
    

    conn = sqlite3.connect('eng.sqlite')
    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
    
    # sqlite built table :  UNIQUE KEY  > UNIQUE

# joining table    
    #SERIAL is not in SQLite
    sql = '''
    CREATE TABLE IF NOT EXISTS joining (
            "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            "JOtime" datetime default null,
            "DItime" datetime default null,
            "word" VARCHAR(20) NOT NULL UNIQUE, 
            "attribute" VARCHAR(100) NOT NULL,
            "translation" VARCHAR(200) NOT NULL,
            "article" VARCHAR(20) NOT NULL);

    '''
    cur.execute(sql)

    
#trash table   
    sql = '''
    CREATE TABLE IF NOT EXISTS trash (
    word VARCHAR(100) NOT NULL UNIQUE,
    attribute VARCHAR(100) NOT NULL)
    '''
    cur.execute(sql)


#spelling table
    sql = '''
    CREATE TABLE IF NOT EXISTS spelling (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    JOtime datetime default null,
    INtime datetime default null,
    UPtime datetime default null,
    DItime datetime default null,    
    word VARCHAR(20) NOT NULL UNIQUE, 
    attribute VARCHAR(100) NOT NULL,
    translation VARCHAR(200) NOT NULL,
    lv TINYINT(3) NOT NULL,
    article VARCHAR(20) NOT NULL)
    '''
    cur.execute(sql)
    
# build lemma table
    
    sql = '''
    CREATE TABLE IF NOT EXISTS lemma (
    trans VARCHAR(50) UNIQUE, 
    word VARCHAR(50) NOT NULL)
    '''
    cur.execute(sql)
         
    conn.commit()
    cur.close()
    conn.close()
    
    fill_lemma()    #b2

#__b4_______________________________________________________________________    

if __name__ == '__main__':
   print()


