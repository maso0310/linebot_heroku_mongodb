import pymongo
import datetime


client = pymongo.MongoClient("自己的mongodb網址")#範例如圖：

#dblist = client.list_databases
#dbnames = client.database_names

db = client['MongoClient']
col = db['Database']

data_list = []

#用來確認key是否有在指定dictionary當中
def dicMemberCheck(key, dicObj):
    if key in dicObj:
        return True
    else:
        return False

#寫入單筆資料，其中data是python的dictionary
def write_one_data(data):
    col.insert_one(data)

#寫入多筆資料函數，其中data是dictionary組成的list
def write_many_datas(data):
    col.insert_many(data)

#讀取所有資料，並且把資料全部放到一個list當中回傳
def read_many_datas():
    for data in col.find():
        data_list.append(str(data))

    return data_list

#檢查所有資料，如果是文字訊息則將該文字加入到list當中，並且回傳
def read_chat_records():
    for data in col.find():
        if dicMemberCheck('events',data):
            if dicMemberCheck('message',data['events'][0]):
                if dicMemberCheck('text',data['events'][0]['message']):
                    data_list.append(data['events'][0]['message']['text'])
        else:
            print('不是LINE的webhook evnet',data)

    print(data_list)
    return data_list

#刪除所有資料
def delete_all_data():
    x = col.delete_many({})

    for x in col.find():
        data_list.append(x)

    if len(data_list)==0:
        return "資料刪除完畢"
    else:
        return "資料刪除出錯"