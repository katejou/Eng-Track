from func import back_G
from func import inputF
from func import tran
from func import spell
from func import graph        # there will be wraning :  No module named 'func', but still work
                              # cannot remove 'from func' 

#__B_______________________________________________________________________ 

def BT():
    back_G.built_tables()                   # b3+b2 
def FB():
    back_G.fill_basic()                     # b1

#__C_______________________________________________________________________   

def IN(fn):
    show = inputF.input_txtF(fn)            #I1
    return show

def IN2(word):
    show = inputF.input_dict(word)          #I2
    return show
   
#__D_______________________________________________________________________
def JW():
    JW = tran.howManyJW()                   #t1
    return JW

def TA(num):
    TA = tran.takeoutASE(num)               #t2
    return TA
def TD(num):  
    TD = tran.takeoutDESC(num)              #t3
    return TD

def JTSA(num,lv):
    tran.join_to_spellingASC(num,lv)        #t4
def JTSD(num,lv):
    tran.join_to_spellingDESC(num,lv)       #t5

#__E_____1__________________________________________________________________

def ART():
    art = spell.art()                       #s1
    return art
def ALV(article):
    alv = spell.ALV(article)                #s2
    return alv
def TOA(ls,art):
    TwoDls = spell.take_out_by_alv(ls,art)  #s3
    return TwoDls

#__E_____2__________________________________________________________________
    
def LV():
    lilv = spell.allLV()                    #s4
    return lilv
def TOL(ls):
    TwoDls = spell.take_out_by_lv(ls)       #s5
    return TwoDls    

#__E_____3__________________________________________________________________

def JTE():
    MAX,MIN = spell.JotimeR()               #s6
    return MAX,MIN 
def ITE():
    MAX,MIN = spell.IntimeR()               #s7
    return MAX,MIN    
def UTE():
    MAX,MIN = spell.UptimeR()               #s8
    return MAX,MIN 
def DTE():
    MAX,MIN = spell.DitimeR()               #s9
    return MAX,MIN 

def LVBT(Trange,Wtime):
    if Wtime == 'J':
        levels = spell.tO_Jtr(Trange)       #s10
    if Wtime == 'I':
        levels = spell.tO_Itr(Trange)       #s11
    if Wtime == 'U':
        levels = spell.tO_Utr(Trange)       #s12
    if Wtime == 'D':
        levels = spell.tO_Dtr(Trange)       #s13
    return(levels)
    
def TOT(lvs_take,Wtime,Trange):
    if Wtime == 'J':
        TwoDls = spell.totJ(lvs_take,Trange)    #s14
    if Wtime == 'I':
        TwoDls = spell.totI(lvs_take,Trange)    #s15
    if Wtime == 'U':
        TwoDls = spell.totU(lvs_take,Trange)    #s16
    if Wtime == 'D':
        TwoDls = spell.totD(lvs_take,Trange)    #s17   
    return TwoDls   

#__E_____4__________________________________________________________________
    
def ULV(ls):
    spell.ulv(ls)   # user re-leveled TwoDls    #s18
   
#__F_______________________________________________________________________
    
def ETG():
    graph.ET()                          #g1
    
def LVG():
    graph.level()                       #g2

def FQG():
    graph.frequency()                   #g3

#__0_______________________________________________________________________
if __name__ == '__main__':
    print()


