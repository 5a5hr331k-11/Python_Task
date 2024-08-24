import pymongo
from bson import ObjectId

connect_pymongo = pymongo.MongoClient("mongodb://localhost:27017")
db_name = connect_pymongo["Office_details"]
col_name = db_name["employees"]

#Inserting data:

employee = [
    {"name":"person a","age":25,"experience":"4 years"},
    {"name":"person b","age":32,"experience":"7 years"},
    {"name":"person c","age":27,"experience":"3 years"},
    {"name":"person d","age":21,"experience":"1 years"},
    {"name":"person e","age":30,"experience":"8 years"},
    {"name":"person f","age":37,"experience":"10 years"},
    {"name":"person g","age":41,"experience":"13 years"},
    {"name":"person h","age":34,"experience":"6 years"},
    {"name":"person i","age":45,"experience":"15 years"},
    {"name":"person j","age":26,"experience":"2 years"},
    ]
def insert_datas(dataIn):
    insertData = col_name.insert_many(dataIn)
    return insertData.inserted_ids
insert_datas(employee)

#get by ID:

def get_by_id(id):
    employeeID = ObjectId(id)
    find_document = col_name.find_one({"_id":employeeID})
    print(find_document)
get_by_id("66c9deeca26ab197ae1f33bd")

#get all:

##def get_all_data():
##    employeeData = col_name.find()
##    for n in employeeData:
##        print(n)
##get_all_data()

#update data:

def update_data(query,new_data):
    update_detail = col_name.update_one(query,new_data)
update_data({"name":"person i"},{"$set":{"age":47}})

#delete data:

def delete_data(data):
    delete_detail = col_name.delete_one(data)
delete_data({"name":"person a"})

#sort data into ascending order:

pipeline = [
    {"$sort":{"experience":1}}
    ]
def sortData(ascending):
    sorting = col_name.aggregate(ascending)
    for document in sorting:
        print(document)
sortData(pipeline)






    
    
