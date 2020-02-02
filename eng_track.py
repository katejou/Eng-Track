from func import FC
import tkinter as tk
from tkinter import StringVar
import message as m
import random as r
import datetime
from PIL import Image, ImageTk

#---------------------for window-----------
global no,progress,v1
no = 1
progress  = m.null()

#---------------------for grading-----------
global ws,it,lv_of_ws,order
ws = []          # words
lv_of_ws = []    # grading 1-5
order = ''       # (Ase/Desc) 
it = 0           # for iterate index

#--------------------for spelling-----------------
global artls,lvs_take,HM_lv,TwoDls,AN,Wtime,Trange,TO   
artls = []       # all articles name
lvs_take = []    # take how many words in that lv
HM_lv = []       # total words in that lv
TwoDls = []      # spelling info
AN = ''          # article name
Wtime = 0        # Wtime stand for Wrong times or What time? (IN/JO/UP/DI)
Trange = []      # Time Range
TO = ''          # take out by (Article+LV / levels / time+LV)

#----------------------------------------------------------------
def lvBYuser(num,ws):

    lv = []
    for w in ws:   
        text.config(state='normal')   
        text.insert('end',w,'context')  
        while 1:
            break   
        text.config(state='disabled')            
        text.see('end')                  
        
    return lv
                # lv = lvBYuser(ws)         # grading start
                # FC.JTSA(num,lv)           # transfer
def show(run_info):
    
    text.config(state='normal')                    # unlock text
    text.insert('end','\n\n','context')            # \n
    text.insert('end','-'*50,'context')
    text.insert('end','\n','context')              # \n   
    for i in run_info:
        text.insert('end',i,'context')             # add text
        text.insert('end','\n','context')          # \n
    text.insert('end','-'*50,'context')
    text.config(state='disabled')                  # lock text       
    text.see('end')                                # drag down scrollbar
    
            
#------------------------------------------------------------------    
# 轉頁改文字
def turn_page():
    
    global lvs_take,artls,HM_lv,it,Trange,no,Wtime,context,progress,order,TO      
    # context need to be global, or graph will not show?   
    
    text.config(state='normal')                    # unlock text
    text.delete(1.0,tk.END)                        # clean all text
    
    if no == 1:
        title,context = m.main_page()
    elif no == 2:
        title,context = m.idea_page()
        progress = m.to_main()
        no = 1      
    elif no == 3:
        title,context = m.source_page()
        progress = m.to_main()
        no = 1
    elif no == 4:
        title,context = m.limit_page()
        progress = m.to_main()
        no = 1
#------------------------------------------------------------------
    elif no == 6: 
        title,context = m.butil_table_page() 
        progress = m.enter_to_start()
    elif no == 7:
        title,context = m.page7()
        progress = m.enter_to_start()
#------------------------------------------------------------------
    elif no == 9:
        title,context = m.inputfile()
        progress = m.pls_enter()
    elif no == 10:
        title,context = m.inputdict()
        progress = m.pls_enter()
#------------------------------------------------------------------
    elif no == 11:
        title,context,JW = m.lv_ascS1()
        if JW :
            progress = m.pls_enter()        
            order = 'A'
        else :
            progress = m.to_main()
            no = 1
            
    elif no == 12:
        title,context,JW = m.lv_descS1() 
        if JW :
            progress = m.pls_enter()
            order = 'D'
            no = 11           # do the same thing as 11, divide by order
        else :
            progress = m.to_main()
            no = 1        
#------------------------------------------------------------------
    elif no == 13:
        
        HM_lv = []                      # clear data when open this page 
        it = 0
        lvs_take = []
        Wtime = 0

        title,context,HM_lv = m.page13()
        
        progress = m.pls_enter() 
        TO = 'L'
        
    elif no == 14:

        artls = []                      # clear data when open this page 
        HM_lv = []                       
        it = 0
        lvs_take = []
        Wtime = 0
        
        title,context,art = m.by_article()
        progress = m.pls_enter() 
        artls = art                     # save art to artls
        TO = 'A'
        
#-------------------------------- 
        
    elif no == 15:

        HM_lv = []                      # clear data when open this page 
        it = 0
        lvs_take = []

        title,context,Trange = m.page15J()    
        progress = m.pls_enter()
        Wtime = 'J'
        TO = 'T'
        
    elif no == 16:
        
        HM_lv = []                      # clear data when open this page 
        it = 0
        lvs_take = []
        
        title,context,Trange = m.page16I()    
        progress = m.pls_enter()
        no = 15
        Wtime = 'I'
        TO = 'T'

    elif no == 17:
        
        HM_lv = []                      # clear data when open this page 
        it = 0
        lvs_take = []
        
        title,context,Trange = m.page17U()
        progress = m.pls_enter()
        no = 15  
        Wtime = 'U'                                 # Wtime will tell the diffrence
        TO = 'T'  

    elif no == 21:
        
        HM_lv = []                      # clear data when open this page 
        it = 0
        lvs_take = []
        
        title,context,Trange = m.page21D()
        progress = m.pls_enter()
        no = 15
        Wtime = 'D' 
        TO = 'T' 

#------------------------------------------------------------------   
        
    elif no == 18:
        
        FC.ETG()
        title,context = m.page18()
        
        load = Image.open('ET.png')
        render = ImageTk.PhotoImage(load)

        w = tk.Toplevel(root,width=228,height=228)
        img = tk.Label(w, image=render)
        img.image = render
        img.place(x=0,y=0)
        w.resizable(False, False)

        progress = m.to_main()
        no = 1
    
    elif no == 19: 
        
        FC.LVG()
        title,context = m.page19()
        
        load = Image.open('LV.png')
        render = ImageTk.PhotoImage(load)

        w = tk.Toplevel(root,width=228,height=228)
        img = tk.Label(w, image=render)
        img.image = render
        img.place(x=0,y=0)
        w.resizable(False, False)
        
        progress = m.to_main()
        no = 1
    
    elif no == 20:
        FC.FQG()
        title,context = m.fq_Intro()
        load = Image.open('FQ.png')
        render = ImageTk.PhotoImage(load)

        w = tk.Toplevel(root,width=350,height=350)
        img = tk.Label(w, image=render)
        img.image = render
        img.place(x=0,y=0)
        w.resizable(False, False)

        progress = m.to_main()
        no = 1
        
#------------------------------------------------------------------        
    text.insert('insert',title,'title')            # 因為不想複製這4行，所以開這個涵式。
    text.insert('insert',context,'context')        #
    text.config(state='disabled')                  #
    l.config(text = progress)
    
    
# 轉頁改文字    
#------------------------------------------------------------------
# 當按ENTER時去做的事
def but_sw():

    global no,progress,v1
    
    global ws,index_of_ws,lv_of_ws,order
    
    global artls,HM_lv,lvs_take,it,TwoDls,AN,Wtime,Trange,TO
    
    text.config(state='normal')
    
    
    if no == 1:              # 1~4,18~20
        
        turn_page()                        # back to main page
        progress = m.null()

    elif no == 6 :                         # built table + fill lemma
        try:
            FC.BT()

            info = ['建資料庫及去變化形功能 完成']
            show(info)
            
            progress = m.to_main()
            no = 1
        except:
            progress = m.fail()
      
        
    elif no == 7:                          # fill basic
        try:
            FC.FB()

            info = ['基本詞彙滙入 完成']
            show(info)
            
            progress = m.to_main()
            no = 1
        except:
            progress = m.fail()

#-------------------------------- 
            
    elif no == 9: 
                                              # input file
        fn = v1.get()
        try:
            run_info = FC.IN(fn)
            progress = m.pls_enter()
            show(run_info)
        except:
            progress = m.fail()

    elif no == 10: 
                                              # input dict
        word = v1.get()
        word = [[word]]
        try:
            run_info = FC.IN2(word)
            progress = m.pls_enter()
            show(run_info)
        except:
            progress = m.fail()

#-------------------------------- grading -----------------------------------------
            
    elif no == 11:
                                            # grading 1
        ws = []                             # clean old record
        lv_of_ws = []                       # for 110
        it = 0
        
        num = v1.get()
        try:
            num = int(num)
            if num < 1 or num > FC.JW():
                    progress = m.out_of_range()
            else:
                text.config(state='normal')   
                text.insert('end',num,'context')        # show input num
                text.insert('end',' 個','context')    
                text.insert('end','\n','context')
                progress = m.pls_enter()                  
                
                if order == 'A':
                    ws = FC.TA(num)                     # get words
                if order == 'D':
                    ws = FC.TD(num)
                    
                no = 110                                # 改enter的用途            
                
                Q = '\n從 1-5, 1最易, 5最難，以下這個字是？\n'
                text.insert('end',Q,'context')
                text.insert('end','\n','context')                   
                text.insert('end',ws[it],'context')     # print the first word
                text.insert('end','\t\t','context')   
                progress = m.pls_enter()
                
                it += 1                                 # 下次印下一個字
                
        except:
            progress = m.fail()

    
    elif no == 110:                                     # grading 2
        
            num = v1.get()   
            try:
                num = int(num)                
                if num < 1 or num > 5:                  # if out of range
                    progress = m.out_of_range()

                else:
                    lv_of_ws.append(num)                #saved for 111
                    text.insert('end',num,'context')    # show input lv
                    text.insert('end',' 級','context')  # show input lv
                    text.insert('end','\n','context')
                    progress = m.pls_enter()
                    
                    if it == len(ws):                   # if it is last one of ws
                        no = 111 
                        Q = '\n評分完成，確定評分？\t (ENTER = 確定 , 跳出頁面=取消評分)'
                        text.insert('end',Q,'context')   
                        progress = m.enter_to_start()
                        text.see('end')                 # drag down scrollbar                                                
                    else:
                        text.insert('end',ws[it],'context')
                        text.insert('end','\t\t','context')   
                        it += 1                         # 下次印下一個字 
                        text.see('end')                 # drag down scrollbar 
                        progress = m.pls_enter()
            except:
                progress = m.wrong()
                
    elif no == 111:                                     # grading 3
        try:             
            if order == 'A':
                FC.JTSA(len(ws),lv_of_ws)               # transfer start
            if order == 'D':
                FC.JTSD(len(ws),lv_of_ws)

            info = ['評分完成']
            show(info)
            progress = m.to_main()                      # to main page
            no = 1

            order = ''                                  # clear data
            ws = []
            lv_of_ws = []            
        except:
            progress = m.fail()       

#----------------------------------- spelling by level ---------------------------------------- 
    elif no == 13:                                      # + spelling how many levels stage

        num = v1.get()
        try:
            num = int(num)            
            if 0 <= num <= HM_lv[it]:     
                 it += 1                                # next input, next level
                 lvs_take.append(num)
                 Q = '%d 個'%(num)
                 text.insert('end',Q,'context')
                 progress = m.pls_enter()
                 
                 if it == 5:                        
                     Q = '\n\n開始抽背 ？\t(ENTER = 確定 , 跳出頁面=取消抽背)'
                     text.insert('end',Q,'context') 
                     progress = m.enter_to_start()
                     text.see('end')  
                     
                     no = 141                           # change button function 141####################
                 else:
                     a = it+1
                     Q = '\n 請問第 %d 級要抽背多少個 ？\t\t'%(a)
                     text.insert('end',Q,'context')              
                     text.see('end')
                     progress = m.pls_enter()

            else:
                progress = m.out_of_range()
                
        except:
            progress = m.wrong()                        # not a number
            
#--------------------------------------- spelling by article -----------------------------        
    elif no == 14:
        
        HM_lv = []
        lvs_take = [] 
        it = 0
        
        art = v1.get()

        if art in artls:                                # this artls is updated at turn_page()

            artls = []                                  # clear data
            no = 13                                     # change funtion of button = 13 (by levels)
            AN = art                                    # save for later use
            
            HM_lv = FC.ALV(art)                         # save how many words in that lv

            Q = art
            Q += '\n\n該文章的單字︰'
            text.insert('end',Q,'context')
                       
            Q = m.QLN(HM_lv)
            text.insert('end',Q,'context')              
            text.see('end')            

            progress = m.pls_enter()             
        else:    
            progress = m.out_of_range()
            
#------------------------------------- speling by time  ---------------------------------    
            
    elif no == 15:         # get min time
                       
        MIN = datetime.datetime.strptime(Trange[0],'%Y-%m-%d %H:%M:%S') # got when turn page
        MAX = datetime.datetime.strptime(Trange[1],'%Y-%m-%d %H:%M:%S') # or when inputed v
        
        Smin = v1.get()       
        try :
            Smin = datetime.datetime.strptime(Smin,'%Y-%m-%d %H:%M:%S')

            if Smin >= MIN and Smin <=MAX:
                Q = str(Smin)+'\n'
                Q += '請問抽背的單字，要<到>何時結束 ？\t' 
                text.insert('end',Q,'context')
                progress = m.pls_enter()
                Trange[0] = str(Smin)
                no = 150
                    
            else:
                progress = m.out_of_range()               
                
        except:
            progress = m.wrong()

  
    elif no == 150:        # get max time + jump to take how many level stage
               
        MIN = datetime.datetime.strptime(Trange[0],'%Y-%m-%d %H:%M:%S')
        MAX = datetime.datetime.strptime(Trange[1],'%Y-%m-%d %H:%M:%S')
        
        Smax = v1.get()
        try :
            Smax = datetime.datetime.strptime(Smax,'%Y-%m-%d %H:%M:%S')
            if Smax >= MIN and Smax <=MAX:
                Q = str(Smax)+'\n'
                text.insert('end',Q,'context')                                                
                Trange[1] = str(Smax)

                HM_lv = FC.LVBT(Trange,Wtime)
                Q = '\n以下是這個時間內的單字︰\n'
                Q += m.QLN(HM_lv)
                text.insert('end',Q,'context')
                                                  
                progress = m.pls_enter()
                no = 13
       
            else:
                progress = m.out_of_range()  
                            
        except:
            progress = m.wrong()  

#----------------------------------- take out spelling info ----------------------------------- 

    elif no == 141:
        
        if sum(lvs_take) != 0:                  # lvs_take from 140, AN from 14
            if  TO == 'T':
                TwoDls = FC.TOT(lvs_take,Wtime,Trange)
                Trange = []                     # clear Trange

            if  TO == 'A':                
                TwoDls = FC.TOA(lvs_take,AN)    # TwoDls are wors with its info <- no need to clean replace every time
                AN = ''                         # clear AN
                
            if  TO == 'L':
                TwoDls = FC.TOL(lvs_take)
                
            lvs_take = []                       # all clear lvs_take
            TO = ''                             # all clear TO
                                            
            info = ['開始溫習 : ']               # print spelling info
            show(info)            
            for i in TwoDls:
                info = i
                info.insert(1,'')               # for good-looking 
                show(info)
    
            info = ['開始測試 ？ ']
            show(info)   
            no = 142                            # change function
            Wtime = 0                           # set to int 0 , to be wrong Time
            it = 0                              # ready to be use
            r.shuffle(TwoDls)                   # shuffle the order of words
            progress = m.enter_to_start()        
            
        else:
            no = 1                              # if [0,0,0,0,0] == lvs_take
            info = ['不抽背']
            show(info)
            progress = m.to_main()

#------------------------------------- doing the test  ---------------------------------  
        
    elif no == 142:                                    #### start and finsh of test
 
        if it == 0:                               ### start of test
            text.delete(1.0,tk.END)                # clean all text
            Wtime = 0                              # clear data
            progress = m.pls_enter()
            
            info = ['測試開始']
            show(info)
                                       
        if it == len(TwoDls):                     ### end of test
            info = ['測試結束, 是否更新評級？\n(ENTER = 更新 , 跳出頁面 = 不更新)']
            show(info)            
            no = 144                               # jump to regrading
            progress = m.enter_to_start()
            it = 0                                 # for regrading
            Wtime = 0                              # clear data
            
            l.config(text = progress)              # skip following
            v1.set('')
            return
        
        info =  TwoDls[it][1:]                   ### middle of test
        show(info)

        Q = '\n這個單字是？\n'
        text.insert('end',Q,'context') 
        progress = m.pls_enter()
        text.see('end') 
        no = 143                      

#------------------------------------- check answer  ---------------------------------     

    elif no == 143:                                       # see if answer is right
        w = v1.get()
        if w == TwoDls[it][0]:                            # if right
            it += 1
            info = [w +'  答案正確']
            show(info)
            
            Wtime = 0                                     # jump to next word ^
            no = 142 
            progress = m.Next()
                 
        else:                                             # if wrong    
            Q = '\n%s  錯誤\n'%(w)
            text.insert('end',Q,'context')                # show wrong answer
            text.see('end')             
            Wtime += 1
            progress = m.try_again()

            if Wtime == 3:                                # if 3 time already
                info = ['正確答案  : '+TwoDls[it][0]]    
                show(info)
                Wtime = 0
                
                it += 1                
                no = 142
                progress = m.pls_enter()                  # jump to next word, show answer

#------------------------------------- regrading  --------------------------------- 

    elif no == 144:                                      
               
        if it == 0:                                           ###   start of regrading
            text.delete(1.0,tk.END)
            info = ['開始更新評級\n\n  1 最易，5 最難，以下的單字是？']
            show(info) 
            text.config(state='normal')       # after show, state = disable, turn up again

            Q = '\n\n'+TwoDls[it][0]+'\t\t'
            text.insert('end',Q,'context')
            text.see('end')
            it += 1

        else:                                                 ###   middle of regrading
                try:
                    num = v1.get()
                    num = int(num)
                    if num < 1 or num > 5:                        # if out of range
                        progress = m.out_of_range()
                    else:                                         
                        text.insert('end',num,'context')          # show input lv
                        text.insert('end',' 級\n','context')    
                        progress = m.pls_enter()
                        
                        TwoDls[it-1].append(num)                  # the current it is next it
                                          
                        if it == len(TwoDls):                 ###   end of regrading
                            info = ['\n評分完成，確定評分？\n\t(ENTER = 確定, 跳出頁面 = 取消更新評分 )']
                            show(info)   
                            progress = m.enter_to_start()
                            it = 0                                # clear it
                            no = 145                              # jump to next fc                            
                        
                        else:                                     # if not the last one
                            Q = TwoDls[it][0]+'\t\t'
                            text.insert('end',Q,'context')
                            text.see('end')
                            it +=1          
                except:
                     progress = m.wrong()

    elif no == 145:
        try:
            FC.ULV(TwoDls)
            no = 1
            progress = m.to_main()
            info = ['更新評分完成，按ENTER返回主頁']
            show(info)
            TwoDls = []                    # clear TwoDls
        except:
            progress = m.wrong() 
                  
      
#----------------------------------------

    v1.set('')               # clear the entry box
    # e.config(textvariable = v1)
    l.config(text = progress) 
    text.config(state='disabled')    
    text.see('end')
    
# 當按ENTER時去做的事
#------------------------------------------------------------------
# 轉頁改參數，進度(指引)
    
def turn_page_button2():        # idea_page
    global no
    no = 2  
    turn_page()
    
def turn_page_button3():        # source_page
    global no
    no = 3 
    turn_page()
    
def turn_page_button4():        # intro_page
    global no
    no = 4 
    turn_page()

def turn_page_button6():        # built table
    global no
    no = 6 
    turn_page()  

def turn_page_button7():        # fill lemma
    global no
    no = 7 
    turn_page()  

def turn_page_button8():        # fill basic words , not finish
    global no
    no = 8 
    turn_page()  

def turn_page_button9():        # input .txt
    global no
    no = 9 
    turn_page()  
 
def turn_page_button10():        # input by dict
    global no
    no = 10 
    turn_page()  

def turn_page_button11():        # 評十個新字舊asc
    global no
    no = 11 
    turn_page()   

def turn_page_button12():        # 評十個新字新desc
    global no
    no = 12 
    turn_page()  
    
def turn_page_button13():        # 按分級
    global no
    no = 13 
    turn_page()  

def turn_page_button14():        # 按文章
    global no
    no = 14 
    turn_page()  

def turn_page_button15():        # 按輸入時間
    global no
    no = 15 
    turn_page()  

def turn_page_button16():        # 按評級時間
    global no
    no = 16 
    turn_page()  

def turn_page_button17():        # 按抽背時間
    global no
    no = 17 
    turn_page()  

def turn_page_button18():        # ET graph
    global no
    no = 18 
    turn_page()  
    
def turn_page_button19():        # LV graph
    global no
    no = 19 
    turn_page()  
    
def turn_page_button20():        # FQ graph
    global no
    no = 20 
    turn_page()  
    
def turn_page_button21():        # 按查字典時間
    global no
    no = 21 
    turn_page()  
    
#------------------------------------------------------------------ window start--------------------------
# open the window
root = tk.Tk()
root.title('英行跡')
root.geometry('500x300') 
root.configure(bg ='white')
root.resizable(False, False)
root.tk.call('tk', 'scaling', 1.35)
# arrage the widow
frame1 = tk.Frame(root, height=270, bg = 'white')
frame2 = tk.Frame(root, height = 30, bg = "white")
frame1.pack(fill = 'x', anchor="n")
frame2.pack(fill = 'x' ,anchor="s")
# fill the arrage with widget
# ----------------------------------------------------------------  upper part
text = tk.Text(frame1, height=21, width=68, bg ='black')
scroll = tk.Scrollbar(frame1, command=text.yview)
text.configure(yscrollcommand=scroll.set)                     # connect scroll and text
                                                              # set text font
text.tag_configure('title', foreground='#ffffff',font=('Verdana', 20, 'bold'))
text.tag_configure('context', foreground='#ffffff', font=('Tempus Sans ITC', 12, 'bold'))
                                                              # insert real text
global title,context
title,context = m.main_page()           # at the begining
text.insert('insert',title, 'title')  
text.insert('insert',context, 'context') 
                                                              # locate the text and scroll
text.pack(anchor = 'nw', side = 'left')
scroll.pack(anchor = 'nw',side = 'right', fill='y')
text.config(state='disabled')  
# ---------------------------------------------------------------- lower part                      
# button (right)
b = tk.Button(frame2, text='Enter',font = ('Arial',12), width = 10,command = but_sw)    
b.pack(side = 'right' , fill = 'both', expand=False)
# entry box (middle)
v1 = StringVar()
e = tk.Entry(frame2,textvariable = v1,width = 18, font="Arial 14 bold")
e.pack(side = 'right',fill = 'both',expand=True) 
# lable of progress
l = tk.Label(frame2,width = 20, text = progress, bg ='#ffffff',font = ('Arial',12) ,justify = 'left')
l.pack(side = 'right',fill = 'both',expand=False) 
# ---------------------------------------------------------------- menubar
menubar = tk.Menu(root,font = ('Arial',50))

A = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='說明', menu=A)
A.add_command(label='設計意念', command= turn_page_button2)
A.add_separator()    
A.add_command(label='資料來源', command= turn_page_button3)
A.add_separator()  
A.add_command(label='功能說明', command= turn_page_button4)

B = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='建環境', menu=B)
B.add_command(label='建表', command= turn_page_button6) 
B.add_separator()  
B.add_command(label="滙入基本詞彙", command= turn_page_button7) 

C = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='輸入', menu=C)
C.add_command(label='從檔案', command= turn_page_button9)
C.add_separator() 
C.add_command(label='查單字', command= turn_page_button10)

D = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='評級', menu=D)
D.add_command(label='從最舊開始', command= turn_page_button11) 
D.add_separator() 
D.add_command(label='從最新開始', command= turn_page_button12) 

E = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='抽背', menu=E)
E.add_command(label='按分級', command= turn_page_button13) 
E.add_separator() 
E.add_command(label='按文章', command= turn_page_button14) 
E.add_separator() 
E.add_command(label='按輸入時間', command= turn_page_button15) 
E.add_separator() 
E.add_command(label='按分級時間', command= turn_page_button16) 
E.add_separator() 
E.add_command(label='按溫習時間', command= turn_page_button17) 
E.add_separator() 
E.add_command(label='按查字典時間', command= turn_page_button21)


F = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='圖表', menu=F)
F.add_command(label='各表有多少字', command= turn_page_button18)
F.add_separator()   
F.add_command(label='各分級有多少字', command= turn_page_button19) 
F.add_separator()   
F.add_command(label='過去七天的使用頻率', command= turn_page_button20) 

root.config (menu = menubar)

# ---------------------------------------------------------------- loop start
root.mainloop()