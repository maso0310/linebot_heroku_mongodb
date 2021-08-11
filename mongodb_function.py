'''
這個是基於python程式碼與MongoDB互動的範例，其中包括了：
1.資料庫(Database)的建置
2.集合(Collection)的建置
3.文檔(Document)的CRUD(建立、閱讀、修改、刪除)
↑上面三者的關係為：

MongoClient的資料庫(Database)裡面，可以擁有多個集合(Collection)，相當於關聯式資料庫裡面的資料表(Table)，
每個集合當中，存在取多筆資料，每一筆資料被稱作為一個文檔(Document)，這是屬於在MongoDB資料庫當中最末端的價值單元
因此如果我們希望可以進行資料存取操作，首先要先建立一個資料庫與集合，才能把資料寫入其中

client: 一個透過pymongo建立的MongoDB連線

dbnames: 用來列出目前有的database_names

db: 讀取clinet當中，名為MongoClient的Database
col: 讀取db當中，名為Database的Collection


'''
import pymongo

# 要獲得mongodb網址，請至mongodb網站申請帳號進行資料庫建立，網址　https://www.mongodb.com/
# 獲取的網址方法之範例如圖： https://i.imgur.com/HLCk99r.png
client = pymongo.MongoClient("自己的mongodb連線網址")


#dblist = client.list_databases
#dbnames = client.database_names


#第一個db的建立
db = client['MongoClient']
col = db['Database']

print(client.database_names())#列出client中的資料庫名稱
print(db.collection_names())#列出db中的集合名稱
print(col.count_documents())#計算col中的文檔(資料)數量

data_list = []

#判斷key是否在指定的dictionary當中，若有則return True
def dicMemberCheck(key, dicObj):
    if key in dicObj:
        return True
    else:
        return False

#寫入資料data是dictionary
def write_one_data(data):
    col.insert_one(data)

#寫入多筆資料，data是一個由dictionary組成的list
def write_many_datas(data):
    col.insert_many(data)

#讀取所有LINE的webhook event紀錄資料
def read_many_datas():
    for data in col.find():
        data_list.append(str(data))

    print(data_list)
    return data_list

#讀取LINE的對話紀錄資料
def read_chat_records():
    for data in col.find():
        if dicMemberCheck('events',data):
            if dicMemberCheck('message',data['events'][0]):
                if dicMemberCheck('text',data['events'][0]['message']):
                    print(data['events'][0]['message']['text'])
                    data_list.append(data['events'][0]['message']['text'])
        else:
            print('非LINE訊息',data)

    print(data_list)
    return data_list

#刪除所有資料
def delete_all_data():
    for x in col.find():
        data_list.append(x)   

    datas_len = len(data_list)

    col.delete_many({})

    if len(data_list)!=0:
        return f"資料刪除完畢，共{datas_len}筆"
    else:
        return "資料刪除出錯"

#找到最新的一筆資料
def col_find(key):
    for data in col.find({}).sort('_id',-1):
        if dicMemberCheck(key,data):
            data = data[key]
            break
    print(data)
    return data