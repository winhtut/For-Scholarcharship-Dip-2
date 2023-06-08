import pymongo

import random
connection = pymongo.MongoClient("localhost", 27017)
database = connection["ncc_dip2"]
collection = database["candidate"]

if __name__ == '__main__':

    for i in range(10):
        user_id = random.randint(10, 10000)
        name: str = "ncc"+str(i)
        email: str = "win"+str(i)+"@gmail.com"

        phone: int = 94537
        vote_point:int=0

        info:str = "Candidate Info "+str(i)+"id : "+str(user_id)

        data_form = {"_id": user_id,"name":name ,"email": email, "phone": phone,"info":info,"vote_point":vote_point}

        ids = collection.insert_one(data_form)
        print("inserted id :", ids.inserted_id)