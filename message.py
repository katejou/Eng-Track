from func import FC

#---------------------------------------------------------------------------
def null():
    progress = ""
    return progress
def correct():
    progress = "正確"
    return progress
def wrong():
    progress = "輸入錯誤"
    return progress
def to_main():
    progress = "按Enter回首頁"
    return progress
def enter_to_start():
    progress = "按Enter開始"
    return progress
def done():
    progress = "完成"
    return progress
def fail():
    progress = "出現問題"
    return progress
def repeat():
    progress = "請勿重覆滙入"
    return progress
def toobig():
    progress = '數值太大'
    return progress
def toosmall():
    progress = '數值太小'
    return progress
def pls_enter():
    progress = '請輸入︰'
    return progress
def out_of_range():
    progress = '不在範圍內'
    return progress    
def try_again():
    progress = '再試一次 :'
    return progress 
def Next():
    progress = '按ENTER測下一個'
    return progress     
#---------------------------------------------------------------------------

def main_page():                                            
    title = "\n\n\t英行跡"
    context = "\n\n\n\t\t  你所看過的，必留下痕跡\n\n\n\t\t\t\t\t程式作者  : 周欣"                      
    return title,context 

def idea_page():                                            
    title = '\n設計意念'
    context = '''\n\n
    是否經常遇到不認識的字，不會立刻去查。
    看完整篇，忘記它所在的位置。
    久而久之，那個字在腦海中停留在模糊的印象。
    因為拼不出來，所以閱讀的能力和寫作的能力不成正比。   
    為了解決學習問題，
    希望開發出可以和腦海中的英文詞庫逐漸同步，
    協助溫習的工具。'''
    return title,context

def source_page():
    title = '\n資料來源'
    context = '''\n\n 
    
    所有單詞釋意  來自  劍橋網絡字典
    https://dictionary.cambridge.org/dictionary
    \t\t/english-chinese-traditional/ '''
    return title,context

def limit_page():  
    title = '\n功能說明'
    context = '''     
    ------------------------------
    第一次使用︰
    
    第一次使用必需先'建環境'
    基本資料的滙入，不能缺少三個csv檔案︰
    
    lemma.csv   去變化形資料
    trash.csv   基本詞彙中，屬性不合的
    basic.csv   基本詞彙中，屬性相合的
    
    若日後用戶有更好的資料來源，可以增減這三個資料檔。
    所以資料檔放於程序外。資料庫也不會打包入程序中。

    ------------------------------
    以檔案輸入的文字處理︰
    
    遇到文中所有不是英文字元的地方都會被切開成一個單字。
    例︰don\'t 會被切為 don 和 t。
    因為英文中， \' 或 \" 是開關引號，難以被程式辨別。
    
    同理，無法辨別片語
    例︰Peter Pan(彼得潘)會被切為 Peter 和 Pan。
    ------------------------------
    以查字典輸入的文字處理︰
    
    Peter Pan 能夠被一起辨別。
    但是單查 Kate 等人名，會查不到結果。
    除非該人名有別的意義，例︰
    Mary = （天主教祈禱用語）萬福瑪利亞
    
    更多細節，見劍橋字典官網。
    ------------------------------
    屬性篩選︰
    
    目標屬性︰
    noun,verb,adverb,adjective
    但是如果單字的屬性包含︰
    preposition,determiner,
    auxiliary verb,pronoun,
    article,conjunction,
    interjection,prefix,
    suffix,exclamation
    將歸到垃圾箱(trash)表格，
    並不會出現在可以背的單詞中。
    
    垃圾箱的存在，
    是避免將來會再次浪費爬蟲的時間。
    ------------------------------
    文章名預設︰
    
    以\'從檔案\'輸入的單字，預設為︰
    \'檔名.txt\'
    以\'查字典\'輸入的單字，預設為︰
    dictionary
    以\'滙入基本詞彙\'輸入的單字，預設為︰
    basic
    
    用於\'依文章抽背文字\'
    文章名是依第一次輸入時的設定。
    當單字加入資料庫後，即使再查字典或在其他文章出現。
    單字的文章名依舊不變。
    提醒︰
    單字可以依\'查字典的時間\'或其他方法抽出來。
    ------------------------------
    去變化形功能︰
    
    去變化形功能，不包含所有衍生字，例︰
    輸入 walkings 會化為 walking
    輸入 walking 會化為 walk
    輸入 walks 會化為 walk
    
    只依skywind3000在Github上發布的資料
    作出處理，演化成這個功能。
    目前沒有找到更好的資料來源。
    ------------------------------
    \n

    '''  
    return title,context

#---------------------------------------------------------------------------

def butil_table_page():
    title = '\n建立SQLite表格'
    context = """\n\n
    1. joining     存用戶輸入但未評級的單字
    2. trash        存用戶看過但屬性不重要的單字 
    3. spelling    存用戶評級過，會有機會抽背的
    4. lemma       存變化形對照表
    
    變化形對照資料由skywind3000 提供
    網址︰https://github.com/skywind3000/ECDICT 
    共90,484筆資料。
    """
    return title,context
  

def page7():
    
    title = "\n滙入基本詞彙"
    context = """\n\n
    資料來源︰
    
    1. EF 英語字彙表 
    https://www.ef.com.tw/english-guide/english-vocabulary/
    
    2. 1,000 most common US English words
    https://gist.github.com/deekayen/4148741
    
    處理︰
    
    取以上兩者不重覆共 2,957個單字，
    結合劍橋網絡字典解釋。
    放入可抽背的 spelling 表格，預設評級為 1。
    """
    return title,context

#---------------------------------------------------------------------------

def inputfile():
    title = "\n\n輸入檔案"
    context = """\n
    \t請輸入路徑及檔名，如與此程式同路徑，只要檔名\n
    格式限.txt，路徑及檔名為全英文。(記得打副檔名)
    \n\n\t(平均 1 個新字需要 1 秒。請耐心等候。) 
    """
    return title,context

def inputdict():
    title = '\n\n直接查字典'
    context = "\n\n\t\t請輸入要查的單字 或 片語"
    return title,context

#---------------------------------------------------------------------------

def lv_ascS1():
    title = "\n\n從最<舊>單字開始評分"
    JW = FC.JW()
    if JW :
        context = ' \n\n 現在共有%s個單字等待評級'%JW
        context += '\n  你要評多少個？  '
    else :
        context = '\n\n 現在沒有單字需要評分。'
        context += '\n  請輸入更多新單字。'        
    return title,context,JW

def lv_descS1():
    title = "\n\n從最<新>單字開始評分"
    JW = FC.JW()
    if JW :
        context = ' \n\n 現在共有%s個單字等待評級'%JW
        context += '\n  你要評多少個？  '
    else :
        context = '\n\n 現在沒有單字需要評分。'
        context += '\n  請輸入更多新單字。'   
    return title,context,JW

#---------------------------------------------------------------------------
    
def QLN(lvls):
    
    Q = '\n評級    |{0:^14}|{1:^14}|{2:^14}|{3:^14}|{4:^14}|'.format(1,2,3,4,5)
    a,b,c,d,e =  lvls[0],lvls[1],lvls[2],lvls[3],lvls[4]              
    Q += '\n個數    |{0:^14}|{1:^14}|{2:^14}|{3:^14}|{4:^14}|\n'.format(a,b,c,d,e)  
    Q += '\n 請問第 1 級要抽背多少個 ？\t\t'
    
    return Q

#---------------------------------------------------------------------------

def spell_gra():
    title = "\n\n按分級抽背"
    context = """\n\n
    你需要少個level %d 的單字 ?  :
    """
    return title,context

def by_article():
    title = '\n\n依文章抽背'
    context =  '\n\n以下是\'已評級\'資料庫中所有文章︰\n'
    art = FC.ART()                                          # FC.ART()
    for a in art:
        context += '\n' + str(a)
    context += '\n\n請輸入所選文章名稱︰\t\t'

    return title,context,art         

def page13(): 
    
    title = '\n\n按分級抽背'
    lilv = FC.LV()                                          # FC.LV()
    context = '\n\n資料庫中所有已分級的單字︰\n'
    context += QLN(lilv)                           # another function on this file,up there^

    return title,context,lilv

def page15J():
    
    title = '\n\n按<輸入時間>抽背'
    MAX,MIN = FC.JTE()                                      # FC.JTE()
    context = '\n(*限已分級單字)\n\n <最老> 輸入時間︰ %s '%MIN
    context +='\n <最新> 輸入時間︰ %s '%MAX
    context += '\n\n請問抽背的單字，要<從>何時開始 ？ '

    return title,context,[MIN,MAX]

def page16I():
    
    title = '\n\n按<分級時間>抽背'
    MAX,MIN = FC.ITE()                                      # FC.ITE()
    context = '\n\n <最老> 分級時間︰ %s '%MIN
    context +='\n <最新> 分級時間︰ %s '%MAX
    context += '\n\n請問抽背的單字，要<從>何時開始 ？ '

    return title,context,[MIN,MAX]

def page17U():
    
    title = '\n\n按<溫習時間>抽背'
    MAX,MIN = FC.UTE()                                      # FC.UTE()
    context = '\n\n <最老> 溫習時間︰ %s '%MIN
    context +='\n <最新> 溫習時間︰ %s '%MAX
    context += '\n\n請問抽背的單字，要<從>何時開始 ？\t'

    return title,context,[MIN,MAX]

def page21D():
    
    title = '\n\n按<查字典時間>抽背'
    MAX,MIN = FC.DTE()                                      # FC.DTE()
    context = '\n(*限已分級單字)\n\n <最老> 查字典時間︰ %s '%MIN
    context +='\n <最新> 查字典時間︰ %s '%MAX
    context += '\n\n請問抽背的單字，要<從>何時開始 ？\t'

    return title,context,[MIN,MAX]

#-----------------------------------------------------------------------------------

def fq_Intro():
    
    title = '過去七天的使用頻率' 
    context = ''' 
    
    Inputted :  輸入的總字數，
                \t\t-- 不論是從文章或查字典，已分級或未分級。
    Sorted :    從\'未\'到\'已\'評級的總字數，
                \t\t-- 不包括測驗後的重新評分。             
    Reviewed :  測驗前溫習過的總字數，
                \t\t-- 不論是否完成測驗。
    Consulted : 查字典的總字數，
                \t\t-- 不論該單字分級已否，或由查字典新加入。
                
    *各總字數 :  不包括在trash和lemma表格的單詞。
                \t\t-- 如字數差異過大，如2000比1。
                \t\t-- 線條變化小，會看成2000比0
    '''
    return title,context   

def page18():
    
    title = '各表有多少字\n'
    context = """
    提醒︰
    
    joining     輸入但未評級的單字
    trash       看過但屬性不重要的單字 
    spelling    評級過，會有機會抽背的單字
    
    不會顯示︰
    
    lemma       變化形對照表字數"""
    return title,context 


def page19():
    
    title = '各分級有多少字\n'
    context = """

    \' 評級 \' 簡寫為 \'lv\'  

    圖表只包括 spelling 表格中\'評級過\'的單字。
    
    \'未評級\'的字數，請見上一個功能中 joining 表格的字數。
        
    """ 
    return title,context 

#-----------------------------------------------------------------------------------

if __name__ == '__main__':
    print()








