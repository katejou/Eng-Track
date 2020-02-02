import datetime 
import sqlite3
#import pymysql
from matplotlib import pyplot as plt
import numpy as np
import os
import matplotlib as mpl
from matplotlib.ticker import FormatStrFormatter
  
    
#__G3_______________________________________________________________________ 

def frequency():
    
    conn = sqlite3.connect('eng.sqlite')    
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
 
    JTS = []
    for i in range(0,7):
        today = datetime.date.today()
        d = str(today - datetime.timedelta(days= i)) 
        start = d+' 00:00:00'
        end = d+' 23:59:59'
        sql = "SELECT count(*) FROM `spelling` where JOtime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)
        JW = cur.fetchone()[0]
        sql = "SELECT count(*) FROM `joining` where JOtime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)  
        JW += cur.fetchone()[0]
        JTS.append(JW)  

    DTS = []
    for i in range(0,7):
        today = datetime.date.today()
        d = str(today - datetime.timedelta(days= i)) 
        start = d+' 00:00:00'
        end = d+' 23:59:59'
        sql = "SELECT count(*) FROM `spelling` where DItime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)
        DW = cur.fetchone()[0]
        sql = "SELECT count(*) FROM `joining` where DItime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)  
        DW += cur.fetchone()[0]
        DTS.append(DW)  
       
    ITS = []
    for i in range(0,7):
        today = datetime.date.today()
        d = str(today - datetime.timedelta(days= i)) 
        start = d+' 00:00:00'
        end = d+' 23:59:59'
        sql = "SELECT count(*) FROM `spelling` where INtime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)
        ITS.append(cur.fetchone()[0])
    
    UTS = []
    for i in range(0,7):
        today = datetime.date.today()
        d = str(today - datetime.timedelta(days= i)) 
        start = d+' 00:00:00'
        end = d+' 23:59:59'
        sql = "SELECT count(*) FROM `spelling` where UPtime BETWEEN '%s' AND '%s'"%(start,end)
        cur.execute(sql)
        UTS.append(cur.fetchone()[0])
       
    conn.commit()
    cur.close()
    conn.close()  
    
    JTS.reverse()
    ITS.reverse()
    UTS.reverse()
    DTS.reverse()
    
    D_ago = [i for i in range (7)]
    
    plt.rcParams["figure.facecolor"] = 'w'
    ymajorFormatter = FormatStrFormatter('%d')
    
    mpl.use('TkAgg')
    
    fig, ax = plt.subplots(nrows=4, ncols=1, sharex=True, sharey=True, figsize=(7,7))
    fig.text(0.5, 0.03, 'days ago', ha='center',size = 25)
    fig.text(0.01, 0.5, 'words', va='center', rotation='vertical',size =25)
    fig.suptitle("Frequency",size = 30)
    plt.subplots_adjust(hspace=0.7)    
    
    a = plt.subplot(412)
    a.tick_params(labelsize=15)
    plt.plot(D_ago, ITS,'tab:cyan')
    plt.xticks(np.arange(7),('6','5','4','3','2','Yesterday','Today'), rotation=20)
    a.yaxis.set_major_formatter(ymajorFormatter)
    a.set_title('Sorted',size = 20,loc = 'left')

    b = plt.subplot(413)
    b.tick_params(labelsize=15)
    plt.plot(D_ago, UTS,'tab:blue')
    plt.xticks(np.arange(7),('6','5','4','3','2','Yesterday','Today'), rotation=20)
    b.yaxis.set_major_formatter(ymajorFormatter)
    b.set_title('Reviewed',size = 20,loc = 'left')
   
    c = plt.subplot(411)
    c.tick_params(labelsize=15)
    plt.plot(D_ago, JTS,'tab:blue')
    plt.xticks(np.arange(7),('6','5','4','3','2','Yesterday','Today'),rotation=20)
    c.yaxis.set_major_formatter(ymajorFormatter)             #   y的度，設個位數，如遇0化為小數，會和ylabel 重疊。
    c.set_title('Inputted',size = 20,loc = 'left')    

    d = plt.subplot(414)
    d.tick_params(labelsize=15)
    plt.plot(D_ago, DTS,'tab:cyan')
    plt.xticks(np.arange(7),('6','5','4','3','2','Yesterday','Today'), rotation=20)
    d.yaxis.set_major_formatter(ymajorFormatter)
    d.set_title('Consulted',size = 20,loc = 'left')
       
    my_path = os.getcwd()
    fn = 'FQ.png'
    plt.savefig(os.path.join(my_path,fn),pad_inches = 0,dpi = 50)
    
#__G2_______________________________________________________________________ 

def level():
    
    conn = sqlite3.connect('eng.sqlite')        
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
           
    sql = 'select count(*) from spelling where lv = 1'
    cur.execute(sql)
    lv1 = cur.fetchone()
          
    sql = 'select count(*) from spelling where lv = 2'
    cur.execute(sql)
    lv2 = cur.fetchone()
    
    sql = 'select count(*) from spelling where lv = 3'
    cur.execute(sql)
    lv3 = cur.fetchone()
    
    sql = 'select count(*) from spelling where lv = 4'
    cur.execute(sql)
    lv4 = cur.fetchone()
    
    sql = 'select count(*) from spelling where lv = 5'
    cur.execute(sql)
    lv5 = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()  

    mpl.use('TkAgg')
    
    labels = ['lv1 : %d'%lv1,'lv2 : %d'%lv2,'lv3 : %d'%lv3,'lv4 : %d'%lv4,'lv5 : %d'%lv5]
    colors = ['#FEE5E5', '#FEAAAD', '#FE7A7A', '#FE5E63','#FE3535']
    #https://rgbcolorcode.com/color/FEF3F5
    fig, ax = plt.subplots(figsize=(4.5,4.5))

    mpl.rcParams['font.size'] = 18.0  
    size = 0.5              # how width is the colored part. according to radius
    vals = np.array([lv1,lv2,lv3,lv4,lv5])
    patches, texts = plt.pie(vals.sum(axis=1),radius=1.6,colors = colors,wedgeprops=dict(width=size, edgecolor='w'))
#    plt.legend(patches, labels,loc = 'lower center')
    plt.legend(patches, labels,bbox_to_anchor=(0.8,0.5))
    
    plt.text(0, 0, 'Levels Of Words', ha='center',size = 26)

    my_path = os.getcwd()
    fn = 'LV.png'
    plt.savefig(os.path.join(my_path,fn),bbox_inches="tight",dpi = 50)
    
#__G1_______________________________________________________________________ 

def ET():
    
    conn = sqlite3.connect('eng.sqlite')        
#    conn = pymysql.connect(host='localhost',port=3306,db='eng',user='eng',passwd='123456789',charset='utf8')
    cur = conn.cursor()
         
    sql = 'select count(*) from joining'
    cur.execute(sql)
    jw = cur.fetchone()
          
    sql = 'select count(*) from spelling'
    cur.execute(sql)
    sw = cur.fetchone()
    
    sql = 'select count(*) from trash'
    cur.execute(sql)
    tw = cur.fetchone()
    
    conn.commit()
    cur.close()
    conn.close()  
    
    mpl.use('TkAgg')
    
    labels = [ 'joining : %d'%jw,'spelling : %d'%sw,'trash : %d'%tw ]
    colors = ['#D5FFCC', '#78FAAC', '#0FFA27']
    fig, ax = plt.subplots(figsize=(4.5,4.5))
#    https://medium.com/python4u/hello-matplotlib-8ffe04355ebf

    plt.rcParams['font.size'] = 18.0
    size = 0.5
    vals = np.array([jw,sw,tw])
    patches, texts = plt.pie(vals.sum(axis=1), radius=1.6,colors = colors,wedgeprops=dict(width=size, edgecolor='w'))
    plt.text(0, 0, 'Words In Tables', ha='center',size = 26)
    plt.legend(patches, labels,loc = 'lower center')
    
    # https://stackoverflow.com/questions/29698701/resizing-a-plot-in-tkinter
    my_path = os.getcwd()
    fn = 'ET.png'
    plt.savefig(os.path.join(my_path,fn),bbox_inches="tight",dpi = 50)

    # tkinter window shink!! at console or cmd running
    # > because i hvn't open tkagg, even if it is use for embeding to tkinter, it still have to open!
    # mpl.use('TkAgg') will pop when in spyder only
   
#__0_______________________________________________________________________ 
    
if __name__ == '__main__':
    print()



    