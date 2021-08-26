# 簡易的聊天機器人資料庫 Heroku / MongoDB / LINE BOT
### 操作步驟：<br>

1.下載程式碼
~~~
git clone https://github.com/maso0310/linebot_heroku_mongodb.git
~~~
<br><br>
2.修改程式當中的三個地方：LINEBOT Channel Access Token、Channel Secret以及MongoDB的資料庫連結網址，如下圖<br>


![要改的地方](https://i.imgur.com/7auNd6C.png)
<br><br>
3.[進入 MongoDB官網 並註冊帳號](https://www.mongodb.com/)<br>

4.在MongoDB官網註冊帳號之後，依照官網指示的五個步驟逐漸建立資料庫<br>
5.在建立資料庫之後，點選Connect，選擇Python環境，獲取MongoDB串聯網址，如下圖：<br>


![mongodb網址的位置](https://i.imgur.com/HLCk99r.png)<br>
<br><br>
6.[進入LINE Developer官網建立LINE BOT帳號](https://developers.line.biz/)<br>
7.進入LINE Developer官網，將LINE@帳號的Channel Access Token、Channel Secret置換成自己的，位置如下圖<br>
<br>

![LINE的Access Token跟Secret](https://i.imgur.com/6QmQNpe.png)
<br><br>

### MongoDB的資料庫架構步驟<br>
1.讀取資料庫(Database)<br>
2.讀取集合(Collection)<br>
3.文檔(Document)的CRUD(建立、閱讀、修改、刪除)<br>
#### **↑上面三者的關係為：**<br>

1.MongoDB資料庫，皆以**JSON格式**，寫入與讀取資料<br>
2.MongoClient的資料庫(Database)裡面，可以擁有多個集合(Collection)，相當於關聯式資料庫裡面的資料表(Table)<br>
3.每個集合當中，存在取多筆資料，每一筆資料被稱作為一個文檔(Document)<br>
4.首先要先建立一個資料庫與集合，才能把資料寫入其中<br>
<br><br>

### mongodb_function.py中的變數與函數<br><br>
**client**: 一個透過pymongo建立的MongoDB連線<br>
**db**: 讀取clinet當中，名為MongoClient的Database<br>
**col**: 讀取db當中，名為Database的Collection<br>
**dicMemberCheck()**: 判斷key是否在指定的dictionary當中，若有則return True<br>
**write_one_data()**: 寫入資料data是dictionary<br>
**write_many_datas()**: 寫入多筆資料，data是一個由dictionary組成的list<br>
**read_many_datas()**: 讀取所有LINE的webhook event紀錄資料<br>
**read_chat_records()**: 讀取LINE的對話紀錄資料<br>
**delete_all_data()**: 刪除所有資料<br>
**col_find()**: 找到最新的一筆資料<br>
<br><br>

### 儲存所有webhook event到MongoDB資料庫
1.範例當中已經將LINE webhook event所傳送的JSON資料直接儲存於MongoDB資料庫<br>
2.寫入指令與資料範例如下所示<br>
![寫入的資料庫的指令](https://i.imgur.com/E8bN7bO.jpg)
<br><br>

### 寫入的webhook event範例
~~~
{'_id': ObjectId('611293ef5d5e8a3922ce442c'), 'destination': 'U454e24915d621f68d70b9a509e195d93', 'events': [{'type': 'message', 'message': {'type': 'text', 'id': '14549285734851', 'text': '@讀取'}, 'timestamp': 1628607470353, 'source': {'type': 'user', 'userId': 'U64fcb80364ac73bb9a86f41826e9399a'}, 'replyToken': '9854eb2cc31b43179f27c2a8ca4519ee', 'mode': 'active'}]}
~~~
<br><br>
### 內建指令
**@讀取**: 將目前以放入MongoDB資料庫的資料以字串型式回傳到LINE對話框<br>
**@查詢**: 查詢一筆最新的資料，並以字串型式回傳到LINE對話框<br>
**@對話紀錄**: 查詢透過webhook event傳送到LINEBOT的文字訊息紀錄，整理後回傳至對話框<br>
**@刪除**: 將目前所儲存的資料刪除，並回傳刪除的資料筆數於對話框<br>

<br><br>
====================================<br>
如果喜歡這個教學內容<br>
歡迎訂閱Youtube頻道<br>
[Maso的萬事屋](https://www.youtube.com/playlist?list=PLG4d6NSc7_l5-GjYiCdYa7H5Wsz0oQA7U)<br>
或加LINE私下交流 LINE ID: mastermaso<br>
![LOGO](https://yt3.ggpht.com/ytc/AKedOLR7I7tw_IxwJRgso1sT4paNu2s6_4hMw2goyDdrYQ=s88-c-k-c0x00ffffff-no-rj)<br>


====================================<br>
