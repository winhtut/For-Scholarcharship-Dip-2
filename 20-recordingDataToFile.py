
db={}

global email_exit
email_exit=-1

def main_sector():
    main_option =int(input("Press 1 to Register:\nPress 2 to Login\nPress 3 Exit:"))
    if main_option== 1:
        registration()
    elif main_option==2:
        login()
    elif main_option==3:
        recording_all_data()
        exit(1)
    else:
        print("Invalid Option")
        main_sector()

def registration():

    user_email = input("Enter your email:")
    email_get = Email_exit(user_email)

    if email_get!=None:
        print("Email already exit:")
        registration()
    else:
        user_name = input("Enter your username:")
        user_password = input("Enter your password:")
        user_phone = int(input("Enter your phone:"))
        user_age = int(input("Enter your age:"))

        id = len(db)

        to_insert = {id: {"email": user_email,"u_name":user_name, "password": user_password,"phone":user_phone,"age":user_age}}
        db.update(to_insert)


def login():
    user_found=-1;
    print("This is login sector")
    l_user_email = input("Enter your email to login:")
    l_user_password = input("Enter your password to login:")


    for i in range(len(db)):
        if db[i]["email"] == l_user_email and db[i]["password"]==l_user_password:

            user_found=i
    if user_found!=-1:
        print("Login Success!")
        user_profile(user_found)
    else:
        print("Not Found ")

def user_profile(user_found):
    print("Welcome:",db[user_found]["u_name"])

    option =int(input("Press 1 to exit"))
    if option == 1:
        recording_all_data()


def Email_exit(email):

    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:

            return i

def recording_all_data():
    with open("nistdb.txt", 'w') as dbfile:
        for i in range(len(db)):
            email = db[i]["email"]
            user_name = db[i]["u_name"]
            password = db[i]["password"]
            phone = db[i]["phone"]
            age = db[i]["age"]
            total_user_data = email + ' ' + user_name + ' ' + password + ' ' + str(phone) + ' ' + str(age)

            dbfile.write(total_user_data)


def loading_all_data():
    with open("nistdb.txt",'r') as dbfile:
        datas=dbfile.readlines()
        for one in datas:
            oneData = one.split(" ")

            id = len(db)
            data_form = {id:{"email":oneData[0],"u_name":oneData[1],"password":oneData[2],
                             "phone":oneData[3],"age":oneData[4]
                             }}
            db.update(data_form)

if __name__ == '__main__':
   loading_all_data()
   print(db)
   while True:
       main_sector()