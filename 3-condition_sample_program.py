
user_name="NIST"
user_pass="nist123"
user_input =int(input("Enter some number:"))

for i in range(user_input):
    l_name =input("Enter your username:")
    l_pass = input("Enter your password:")

    if l_name==user_name and l_pass==user_pass:
        print("Login success")
    else:
        print("Login Failed")