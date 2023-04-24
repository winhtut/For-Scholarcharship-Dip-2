def age_checking(age):
    if age<18:
        print("You cannot play game")
    elif age>=18 and age<40:
        print("you can play game")
    else:
        print("Invalid")


def home_page():
    user_name = input("Enter your name:")
    user_age = int(input("Enter your age:"))

    age_checking(user_age)




home_page()