
import time
from datetime import datetime
import re
import sqlite3
#import pymysql
import requests
from bs4 import BeautifulSoup as bs
import random as r
import os

#__1_______________________________________________________________________
def DItime(word):
    
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    
    
    a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    sql = 'select count(*) from joining where word = "%s"'%(word)
    cur.execute(sql)
    result1 = cur.fetchall()[0]

    if result1:
        sql = 'update joining set DItime = "%s" where word = "%s"'%(a,word)
        cur.execute(sql)

    sql = 'select count(*) from spelling where word = "%s"'%(word)
    cur.execute(sql)
    result2 = cur.fetchall()[0]

    if result2:
        sql = 'update spelling set DItime = "%s" where word = "%s"'%(a,word)
        cur.execute(sql)
    
    conn.commit()
    cur.close()
    conn.close() 

#__2_______________________________________________________________________
    
def no_lemma(str1):

    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()    
       
    for i in range (len(str1)):
            sql = '''select word from lemma where trans = "%s"'''%(str1[i])
            cur.execute(sql) 
            result = cur.fetchone()
            if result :
                a = list(result)
                str1[i] = str(a[0])
        
    conn.commit()
    cur.close()
    conn.close()     
        
    str1 = set(str1)
    str1  = list(str1)           # no repeat
   
    return str1

#__3_______________________________________________________________________
    
def insert_to_joining(join_words,article):
    
    conn = sqlite3.connect('eng.sqlite')
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()

    for i in join_words:
        try:
            a = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql='''insert into joining 
                (word,attribute,translation,article,JOtime) 
                values("%s","%s","%s","%s","%s")'''%(str(i[0]),str(i[1]),str(i[2]),article,a)
            cur.execute(sql)
        except: 
            print()           

    conn.commit()
    cur.close()
    conn.close()

#__4_______________________________________________________________________  
    
def insert_to_trash(trash_words):

    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()

    for i in trash_words:
        try:
            sql = 'insert into trash (word,attribute) values ("%s","%s")'%(str(i[0]),str(i[1]))
            cur.execute(sql)
        except: 
            print()

    conn.commit()
    cur.close()
    conn.close()  

#___5______________________________________________________________________  
    
def trash_or_join(dict_result):
    
#    wanted =  ['noun','verb','adverb','adjective']
    unwanted = ['preposition','determiner','auxiliary verb','pronoun',
               'article','conjunction','interjection','prefix','suffix','exclamation']
  
    trash_words = []
    join_words = []
        
    for d in dict_result :
        dump = False

        if not d[1] :
             dump = True   #except empty list
        else:    
            for i in d[1]:  #each element in attribute
                if i in unwanted:
                    dump = True   #even it is a verb or noun
                
        if dump == True:
            tra = dict_result[dict_result.index(d)]
            trash_words.append([tra[0],tra[1]])     # reduce content in trash
        else:
            join_words.append(d)
       
    return trash_words,join_words    

#__6_______________________________________________________________________
    
def online_dictionary(NEWs):
    
    words = []
    attributes = []
    translations = []

    for w in NEWs:

        url = 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/'+ w      
        header = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 "
                  "Safari/537.36"}

        proxy_ips = ['119.41.236.180:8010',
                     '183.146.213.157:80',
                     '101.231.104.82:80',
                     '101.95.115.196:8080',
                     '36.25.245.51:80',
                     '101.95.115.196:80',
                     '101.37.118.54:8888',
                     '39.137.69.10:8080',
                     '139.9.113.234:443',  
                     '139.9.113.234:8080',
                     '39.137.107.98:8080',
                     '101.4.136.34:81',
                     '39.137.107.98:80',
                     '116.114.19.211:443',
                     '116.114.19.204:443']                     

        ip = r.choice(proxy_ips)
        response = requests.get(url,headers = header,proxies = {'http':'http://'+ip})

        t = 0
        while response.status_code != 200:       # if proxy ips is blocked , pick other
            ip = r.choice(proxy_ips)
            response = requests.get(url,headers = header,proxies = {'http':'http://'+ip}) 
            if response.status_code == 200:  
                break
            t += 1
            if t > 10:                         # give up, show error 
                return ['need new proxies ip','','']               
                
        soup = bs(response.text, 'lxml')

        t = soup.find('meta',{'name':'description'})
        t = t.get('content')
        t = t[(t.find(':')+2):]
        rless = 'Learn more in the Cambridge English-Chinese traditional Dictionary.'
        t = t.rstrip(rless)
        translations.append(list(str(t).split(',')))

        A = soup.find_all('span',{'class':'pos dpos'})
        a = set()
        for i in range(len(A)):
            a.add(A[i].text)            
        attributes.append(list(a))

        words.append(w)
    
    New_results = []
    for i in range(len(words)):
        New_results.append([words[i],attributes[i],translations[i]])  
        
    return New_results

#__7_______________________________________________________________________

def checkIn(words):
    
    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
    
    NEW = []
    for w in words:
        sql = 'select count(*) from joining where word = "%s"'%(w)
        cur.execute(sql)
        result1 = cur.fetchall()[0]

        sql = 'select count(*) from spelling where word = "%s"'%(w)
        cur.execute(sql)
        result2 = cur.fetchall()[0]

        sql = 'select count(*) from trash where word = "%s"'%(w)
        cur.execute(sql)
        result3 = cur.fetchall()[0]
    
        results = result1[0] + result2[0] + result3[0]    # two layer tuple = ((0,),)
        
        if not results:
            NEW.append(w)
    
    conn.commit()
    cur.close()
    conn.close() 
    
    return NEW

#__8_______________________________________________________________________
    
def txt_to_list (fn)  :
    str1 = ''
    with open (fn,'r',encoding='utf-8-sig')as f:
        str1 = f.read()
        str1 = re.split("[^a-zA-Z]", str1)

    A = set()
    for i in str1:
        if i :
            i = i.lower()
            A.add(i)
    return A

#__I1_______________________________________________________________________ 
    
def input_txtF(fn):
    
    show = []
    show.append('\ninput start :'+ str(time.asctime(time.localtime(time.time()))))
                                                                    #------return show
    Alltext = txt_to_list(fn)                                       # 8
    Alltext = no_lemma(list(Alltext))                               # 2
    
    show.append('\nAll words in article:'+ str(len(Alltext)))       #------return show
    
    NEWs = checkIn(Alltext)                                         # 7
    
    show.append('NEW words to database:'+ str(len(NEWs)))           #------return show
    show.append('\n online dictionary start :'+ str(time.asctime(time.localtime(time.time()))))
                                                                    #------return show
                                                                    
    dict_result = online_dictionary(NEWs)                           # 6
    
    show.append(' online dictionary finish :'+ str(time.asctime(time.localtime(time.time()))))
                                                                    #------return show
                                                                    
    trash_words,join_words = trash_or_join(dict_result)             # 5   
    
    show.append('\nwords goto trash:'+ str(len(trash_words)))       #------return show
    show.append('words goto joining:'+ str(len(join_words)))        #------return show
    
    insert_to_trash(trash_words)                                    # 4
    head, tail = os.path.split(fn)                                  # get file name only, no path
    insert_to_joining(join_words,tail)                              # 3
    
    show.append('\ninput finish :'+ str(time.asctime(time.localtime(time.time())))) 
                                                                    #------return show   
    return show

#__I2_______________________________________________________________________ 
    
def input_dict(word):

    TF = no_lemma(word[0])                                          # 2
    NEWs = checkIn(TF)                                              # 7

    if NEWs :                                                      
                            
        dict_result = online_dictionary(NEWs)                       # 6   
        trash_words,join_words = trash_or_join(dict_result)         # 5   >4/3

        if trash_words:
            insert_to_trash(trash_words)                            # 4
        if join_words:
            article = 'dictionary'     
            insert_to_joining(join_words,article)                   # 3 
        if dict_result[0][2][0] ==  'sing one of our 22 bilingual dictionaries':
            dict_result[0][2] = '線上字典查不到該字'

        dict_result[0].insert(1,'')                                 # '' ,for good-looking when show
        dict_result[0].append('\n已加入資料庫')

        DItime(dict_result[0][0])                                   # 1 

        return dict_result[0]

    else:                                                           # if not new, no insert to any table
        
        dict_result = online_dictionary(TF)                         # 6    

        if dict_result[0][2][0] ==  'sing one of our 22 bilingual dictionaries':
            dict_result[0][2] = '線上字典查不到該字'
            
        dict_result[0].insert(1,'') 
        dict_result[0].append('\n本已在資料庫')
        
        DItime(dict_result[0][0])                                   # 1

        return dict_result[0]   

#__0_______________________________________________________________________ 
    
if __name__ == '__main__':
    print()




