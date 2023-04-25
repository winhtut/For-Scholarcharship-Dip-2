# def adding(a,b):
#     c = a+b
#     return c
#
#
# if __name__ == '__main__':
#     result =adding(1,2)
#     print(result)

# သွားခေါ်တဲ့ function သည် return ပြန် ပေးရင် ခေါ်တဲ့ နေရာကလည်း ပြန်လက်ခံ ပေးရမယ်



#test_program

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
        user_password = input("Enter your password:")

        id = len(db)

        to_insert = {id: {"email": user_email, "password": user_password}}
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
        user_profile(l_user_email)
    else:
        print("Not Found ")

def user_profile(info):
    print("Welcome:",info)


def Email_exit(email):

    lenght = len(db)
    for i in range(lenght):
        if db[i]["email"] == email:

            return i

if __name__ == '__main__':

   while True:
       main_sector()