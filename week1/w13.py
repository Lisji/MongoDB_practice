import pymongo

#建立連線
client = pymongo.MongoClient(
"mongodb+srv://B10723059:lisji1030@cluster0.r36j1.mongodb.net/TRY?retryWrites=true&w=majority"
)

#創建名為tempratures的DB，及temp59的collection
db = client.tempratures
w13 = db.temp59

#插入資料
def insertdata():
    w13.insert_many([{ "_id" : 1, "date" : "2021-04-23", "tempsF" : [ 78, 77, 82 ] },{ "_id" : 2, "date" : "2021-05-07", "tempsF" : [ 84, 86, 88 ] },{ "_id" : 3, "date" : "2021-05-24", "tempsF" : [ 90, 91, 95 ] }])

#列印資料
def printdata():
    print("==========================目前資料==========================")
    for x in w13.find():
        print(x)

#華氏轉攝氏
def transC(F):
    C = (F - 32) * 5/9
    return C

#更新資料
def datatranstoC():
    w13.update_many( {}, { "$rename": { "tempsF": "tempsC" } } )
    for i in range(w13.count_documents({})):
        num = i + 1
        new = []
        array = w13.find_one( {"_id" : num})
        for j in range(3):
            new.append(transC(array['tempsC'][j]))
            w13.update_one( { "_id": num},[{ "$set": { "tempsC": new }}])

#以下為主程式
insertdata()
print("更改前")
printdata()
datatranstoC()
print("更改後")
printdata()


