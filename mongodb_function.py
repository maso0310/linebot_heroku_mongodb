import pymongo

# 要獲得mongodb網址，請至mongodb網站申請帳號進行資料庫建立，網址　https://www.mongodb.com/
# 獲取的網址方法之範例如圖： https://i.imgur.com/HLCk99r.png
client = pymongo.MongoClient("自己的mongodb連線網址")

#第一個db的建立
db = client['MongoClient']
col = db['Database']

#print(client.database_names())#列出client中的資料庫名稱
#print(db.collection_names())#列出db中的集合名稱
print(col.count_documents({}))#計算col中的文檔(資料)數量


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
    data_list = []
    for data in col.find():
        data_list.append(str(data))

    print(data_list)
    return data_list

#讀取LINE的對話紀錄資料
def read_chat_records():
    data_list = []
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
    data_list = []
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
