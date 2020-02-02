# 英行跡

# 你所看過的，必留下痕跡
#


意 念︰

開發協助用戶背英單詞的應用程式。

經常看英文文章，遇到不認識的字，不會立刻去查。看完整篇，忘記它所在的位置。久而久之，那個字在腦海中在模糊的印象，但是因為拼不出來，所以閱讀的能力和寫作的能力不成正比。

希望開發出和腦海中的英文詞庫，可以逐漸同步，並協助溫習的工具。

資料來源 (背境建立) :

__1\.  單詞變化形對照表\(lemma\.en\.txt\)__

https://github\.com/skywind3000/ECDICT

__2\.  單詞釋意及來內來自劍橋網絡字典__

https://dictionary\.cambridge\.org/dictionary/english\-chinese\-traditional/

__3\.  EF 英語字彙表__

https://www\.ef\.com\.tw/english\-guide/english\-vocabulary/

__4\.  1,000 most common US English words__

https://gist\.github\.com/deekayen/4148741

[image] https://github.com/katejou/eng-track/blob/master/introPhoto/01.png

# GUI架構
由eng_track.py 為入口，跳出的GUI窗戶，控制其他檔案中的程式。
如不想更改這APP，從這裡執行就好了。

# 使用說明︰
1. 第一次執行一定要建環境
    sqlite資料庫是建立表格時才產生，再滙入csv檔的基本資料。

2. 以檔案輸入的文字處理︰

    遇到文中所有不是英文字元的地方都會被切開成一個單字。

    例︰don't 會被切為 don 和 t。

    因為英文中， ' 或 " 是開關引號，難以被程式辨別。  同理，無法辨別片語

    例︰Peter Pan\(彼得潘\)會被切為 Peter 和 Pan。

3. 以查字典輸入的文字處理︰ Peter Pan 能夠被一起辨別。

    但是單查 Kate 等人名，會查不到結果。	除非該人名有別的意義，例︰

    Mary = （天主教祈禱用語）萬福瑪利亞

4.  屬性篩選︰        

    目標屬性︰  noun\,verb\,adverb\,adjective

    但是如果單字的屬性包含︰   preposition\,determiner\, auxiliary verb\,pronoun\,
article\,conjunction\, interjection\,prefix\, suffix\,exclamation

    將歸到垃圾箱\(trash\)表格，並不會出現在可以背的單詞中。

    垃圾箱的存在， 是避免將來會再次浪費爬蟲的時間。

5.  文章名預設︰  \(文章名用於 ' 依文章抽背文字 '\)

    5.1 以  ' 從檔案 ' 輸入的單字，預設為︰' 檔名\.txt '   \(不包涵路徑\)

    5.2 以  ' 查字典 ' 輸入的單字，預設為︰  dictionary

    5.3 以  ' 滙入基本詞彙 ' 輸入的單字，預設為︰  basic

    5.4 文章名是依第一次輸入時的設定。當單字加入資料庫後，即使再查字典或在其他文章出現。單字的 ' 文章名 ' 依舊不變。

    5.5 提醒︰ 單字可以依 ' 查字典的時間 '  或其他方法抽出來。

6. 去變化形功能，不包含所有衍生字，例︰   

    6.1 輸入 walkings 會化為 walking

    6.2 輸入 walking 會化為 walk

    6.3 輸入 walks 會化為 walk

    目前只依skywind3000在Github上發布的資料作出處理，演化成這個功能。沒有找到更好的資料來源，如用戶有更好來源，請自行更改。

# 結構解釋 :
# 表格
1. lemma  存變形體和本體的對比
2. joining  存用戶看過但未分類的
3. trash  存用戶看過但屬性不重要的
4. spelling  用戶分類過，會有機會抽背的

# 欄位
trans  變形體

words  單字本體

attribute  單字屬性

transaltion   中文解釋

article  文章名

JOtime    輸入的時間

INtime    評級的時間

UPtime    溫習過的時間

DItime    查過字典的時間

# 輸入流程

1\.文章內部去重覆字

2\.還原變化形

3\.對比資料庫沒有重覆

4\.新單字查字典

5\.按屬性存取字典內容

6\.更新查字典時間

按文章︰
1 > 2 > 3 > 4 > 5

按查字典︰
2 > 4 > 顯示 > 3 >
__\(__  __對比資料庫 有 重覆  > 6__) / 
__\( 對比資料庫 沒 重覆  > 5 \+ 6 \)__


# 評級流程

__轉移表格   \+   紀錄時間__

# 抽背流程

__1. 顯示 文章名__

__2. 顯示 各評級  單字數__

__3. 取得 各評級  所要求的單字__  __個數__

__4. 取得__  __各__  __評級中 所有 id__

__5. 隨機抽 各評級 要求個數 的 id__

__6. 按 id 去拿出單字資料__

__7. 溫習 \+ 記錄時間 \+ 測驗__

__8. 重新評分  >  更新評分等級__


按文章 :      1 \- 8

按評級 :      2 \- 8

按時間 : __\(輸入/評級/抽背過/查字典\)__

a \)  顯示該欄時間的最大最小值

b \)  取用戶所選的範圍

c \)  重覆 2 \- 8

# 圖表流程

取各表的字數  >  圓形圖

取spelling的各等級的字數  >圓形圖

取時間   :    

__1__  __判斷今天的時間，要過去六天日期。

__2__  __在 joining 和 spelling 的__  __輸入時間\(JOtime\)     >__  __七天__  __數據__

__3__  __從 joining 到 spelling 的 \(INtime\) 數據    >    七天數據__

__4 從 spelling 的 \(UPtime\)  >    七天數據__

__5 從 spelling 的\(DItime\)     >    七天數據__

