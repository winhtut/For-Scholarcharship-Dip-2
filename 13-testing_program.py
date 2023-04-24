#test_program

db={}

def insertion():

    user_email = input("Enter your email:")
    user_password = input("Enter your password:")
    id = len(db)

    to_insert ={id: {"email":user_email,"password":user_password}}
    db.update(to_insert)

if __name__ == '__main__':
   for i in range(3):
       insertion()

   print(db)