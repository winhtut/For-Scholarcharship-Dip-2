user_name = "NIST"
user_pass = "nist123"

counter = 0

while True:
    l_name = input("Enter your username:")
    l_pass = input("Enter your password:")

    if l_name == user_name and l_pass == user_pass:
        print("Login success")
    else:
        counter = counter + 1
        print("Login Failed")
        if counter == 3:
            print("Wait a time")
            break
