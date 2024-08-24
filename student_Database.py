import pymongo

connect_mongo = pymongo.MongoClient("mongodb://localhost:27017")

my_database = connect_mongo["student_details"]

studentCol = my_database["details"]

#insert_one:

def insert_name(Name,Class,Mark):
    stud_data = {"name": Name, "class": Class, "mark": Mark}
    insertCol = studentCol.insert_one(stud_data)
    return insertCol.inserted_id

insert_name("Sashreeik",11,425)

#insert_many:

students = [
    {"name" : "Abishek", "class" : 11, "mark" : 407},
    {"name" : "Davesh", "class" : 11, "mark" : 440},
    {"name" : "Additya", "class" : 11, "mark" : 465},
    {"name" : "Kamaleshvar", "class" : 11, "mark" : 489},
    {"name" : "Sooriya", "class" : 11, "mark" : 483},
    {"name" : "Kritheesh", "class" : 11, "mark" : 415}
    ]

def insert_multiple(usersData):
    insertData = studentCol.insert_many(usersData)
    return insertData.inserted_ids

insert_multiple(students)

#getting all data from a collection:

def get_all_student():
    all_student = studentCol.find()
    for all_studentdata in all_student:
        print(all_studentdata)

get_all_student()

#getting specific data:

def get_specific_student(id):
    studentID = ObjectId(id)
    myDocument = studentCol.find_one({"_id":studentID})
    print(myDocument)

get_specific_student("66c540033b4b0e936c81767d")

#updating data:

def updateData(query, newData):
    updateRecord = studentCol.update_one(query, newData)
updateData({"name":"Davesh"},{"$set":{"mark":439}})

#$limit:

pipeline = [{"$limit":3}]

def getDataLimit(count_limit):
    limitedData = studentCol.aggregate(count_limit)
    for document in limitedData:
        print(document)
getDataLimit(pipeline)

#$sort:

pipeline = [{"$sort":{"mark":1}}]

def sortData(ascending):
    sorting = studentCol.aggregate(ascending)
    for document in sorting:
        print(document)
sortData(pipeline)

#Queries:

query = {"mark" : {"$gt":450}}

def getData(queryData):
    result = studentCol.find(queryData)
    for doc in result:
        print(doc)
getData(query)





    
