import pymongo

import random
connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["user_info"]

if __name__ == '__main__':



    for i in range(10):
        user_id = random.randint(10, 10000)
        email: str = "win"+str(i)+"@gmail.com"
        password: str = "12345"
        phone: int = 94537

        info:str = "User data is Win"+str(i)+"id : "+str(user_id)

        data_form = {"_id": user_id, "email": email, "password": password, "phone": phone,"info":info}

        ids = collection.insert_one(data_form)
        print("inserted id :", ids.inserted_id)