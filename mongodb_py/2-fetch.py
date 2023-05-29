import pymongo

connection =pymongo.MongoClient("localhost",27017)
database =connection["ncc_dip2"]
collection =database["user_info"]
r_email =input("Enter your email to register:")

for i in collection.find({},{"_id":0,"email":1}):
    if r_email == i["email"]:
        print("Already Register ")
        break


