## 這個是基於python程式碼與MongoDB互動的範例，詳細內容請見mongodb_function.py，其中包括了：

1.資料庫(Database)的建置\n
2.集合(Collection)的建置\n
3.文檔(Document)的CRUD(建立、閱讀、修改、刪除)\n
↑上面三者的關係為：

MongoClient的資料庫(Database)裡面，可以擁有多個集合(Collection)，相當於關聯式資料庫裡面的資料表(Table)，\n
每個集合當中，存在取多筆資料，每一筆資料被稱作為一個文檔(Document)，這是屬於在MongoDB資料庫當中最末端的價值單元\n
因此如果我們希望可以進行資料存取操作，首先要先建立一個資料庫與集合，才能把資料寫入其中\n


client: 一個透過pymongo建立的MongoDB連線\n
db: 讀取clinet當中，名為MongoClient的Database\n
col: 讀取db當中，名為Database的Collection