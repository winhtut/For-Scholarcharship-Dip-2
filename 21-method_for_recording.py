# nistdb = {0:{'email': 'win@gmail.com', 'u_name': 'winpass', 'password': 'winpass', 'phone': 99, 'age': 100},
#
#         1:{'email': '1win@gmail.com', 'u_name': 'winpass', 'password': 'winpass', 'phone': 99, 'age': 100},
#         2:{'email': '2win@gmail.com', 'u_name': 'winpass', 'password': 'winpass', 'phone': 99, 'age': 100},
#         3:{'email': '3win@gmail.com', 'u_name': 'winpass', 'password': 'winpass', 'phone': 99, 'age': 100}
#
#           }

nistdb={}

#print(nistdb)


#print(nistdb.keys())


def recording_all_data():
    with open("nistdb.txt", 'w') as dbfile:
        for i in range(len(nistdb)):
            email = nistdb[i]["email"]
            user_name = nistdb[i]["u_name"]
            password = nistdb[i]["password"]
            phone = nistdb[i]["phone"]
            age = nistdb[i]["age"]
            total_user_data = email + ' ' + user_name + ' ' + password + ' ' + str(phone) + ' ' + str(age) + '\n'

            dbfile.write(total_user_data)
           # print("data:", email, user_name, password, phone, age)
            #print("Recorded")

def loading_data_from_file():


    with open("nistdb.txt",'r') as dbfile:
        datas=dbfile.readlines()
        for one in datas:
            oneData = one.split(" ")

            id = len(nistdb)
            data_form = {id:{"email":oneData[0],"u_name":oneData[1],"password":oneData[2],
                             "phone":oneData[3],"age":oneData[4]
                             }}
            nistdb.update(data_form)


    print(nistdb)






if __name__ =='__main__':

    loading_data_from_file()