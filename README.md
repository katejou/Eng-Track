# 英行跡

你所看過的，必留下痕跡

# 意 念︰

開發協助用戶背英單詞的應用程式。

經常看英文文章，遇到不認識的字，不會立刻去查。看完整篇，忘記它所在的位置。

久而久之，那個字在腦海中在模糊的印象，但是因為拼不出來，所以閱讀的能力和寫作的能力不成正比。

希望開發出和腦海中的英文詞庫，可以逐漸同步，並協助溫習的工具。

# 程式結構

![image](https://github.com/katejou/eng-track/blob/master/introPhoto/06.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/07.png)

# 資料庫結構︰

表格

1. lemma  存變形體和本體的對比

2. joining  存用戶看過但未分類的

3. trash  存用戶看過但屬性不重要的

4. spelling  用戶分類過，會有機會抽背的

欄位

trans  變形體

words  單字本體

attribute  單字屬性

transaltion   中文解釋

article  文章名

![image](https://github.com/katejou/eng-track/blob/master/introPhoto/02.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/01.png)

# 主要程式流程︰

![image](https://github.com/katejou/eng-track/blob/master/introPhoto/03.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/04.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/05.png)

# 主要使用畫面︰

![image](https://github.com/katejou/eng-track/blob/master/introPhoto/08.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/09.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/10.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/11.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/12.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/13.png)
![image](https://github.com/katejou/eng-track/blob/master/introPhoto/14.png)


# 運行環境︰

下載個 anacond ，當我開發的時候是以

    conda version : 4.8.1
    
    conda-build version : 3.18.9
    
    python version : 3.7.4.final.0

和 其他套件運行︰

requests                      2.22.0

selenium               		  3.141.0  <-- 這個套件要自己加

beautifulsoup4	              4.8.0	

PIL 	                      7.0.0

numpy                         1.18.1

matplotlib                    3.1.1


# 使用說明︰

由 eng_track.py 為入口，跳出的GUI窗戶可以控制其他檔案中的程式。如不想更改這應用程式，從這裡單純執行就好了。

(我已經試過打包它成為一個執行檔，但是pyinstaller這工具打包了太多anaconda中用不到的東西進去了，所以檔案太大，不好放上來。)

1. 第一次執行一定要做「建環境」(選單之一):

    sqlite資料庫是「建環境」時才產生，它會建好表格再滙入三個csv檔為基本資料。
    
    lemma.csv   存變化形對照表資料
    
    trash.csv   存基本詞彙中，屬性不需要背誦的
    
    basic.csv   存基本詞彙中，屬性應該背誦的
    
    如果你有更好的資料來源︰如你認為基本單字量不夠，變化詞對換表不夠精準等。
    
    可以自行參悟CVS檔中的資料格式，整理好你的資料，替代原檔，然後再進行「建環境」。
    
    建環境只需要進行一次，資料庫出現之後就可以保存所有操作的紀錄。
    
2. 以「檔案輸入」的文字處理︰

    遇到文中所有不是英文字元的地方都會被切開成一個單字。

    例︰don't 會被切為 don 和 t。

    因為英文中， ' 或 " 是開關引號，難以被程式辨別。  同理，無法辨別片語

    例︰Peter Pan\(彼得潘\)會被切為 Peter 和 Pan。

3. 以「查字典輸入」的文字處理︰ Peter Pan 能夠被一起辨別。

    但是單查 Kate 等人名，會查不到結果。	除非該人名有別的意義，例︰

    Mary = （天主教祈禱用語）萬福瑪利亞

4.  屬性篩選︰        

    目標屬性︰  noun\,verb\,adverb\,adjective

    但是如果單字的屬性包含︰   
    
    preposition\,determiner\, auxiliary verb\,pronoun\,article\,conjunction\, interjection\,prefix\, suffix\,exclamation

    將歸到垃圾箱\(trash\)表格，並不會出現在可以背的單詞中。

    垃圾箱的存在， 是避免將來會再次浪費爬蟲的時間。

5.  文章名預設︰  \(文章名用於「依文章抽背單字」\)

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
    
    (詳見第一項使用說明。)
