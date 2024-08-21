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



    
