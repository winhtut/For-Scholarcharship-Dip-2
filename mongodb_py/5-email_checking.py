def email_checking(r_email):
    name_counter =0
    for i in range(len(r_email)):
        if r_email[i]=='@':
            #print("Name End Here")
            break
        name_counter +=1
    
    print("Name counter: ",name_counter)
    
    email_name = r_email[0:name_counter]
    email_form = r_email[name_counter:]
    
    #print(email_name)
    print(email_form)
    
    #checking for name 
    name_flag=0
    email_flag=0
    for i in range(len(email_name)):
        aChar = email_name[i]
        if (ord(aChar) >31 and ord(aChar) < 48 ) or ( ord(aChar) >57 and ord(aChar) < 65) or ( ord(aChar) >90 and ord(aChar)<97) or (ord(aChar) >122 and ord(aChar) < 128 ):
               
           name_flag = -1
           break

    domain_form=["@facebook.com","@ncc.com","@mail.ru","@yahoo.com","@outlook.com","@apple.com","@zoho.com","@gmail.com"]
    
    for i in range(len(domain_form)):
        
        if domain_form[i] == email_form:
            email_flag= 1
            break
    
    
    if name_flag == -1 or email_flag== 0 :
        return -1
        
    else: 
        return 1



if __name__ == '__main__':
    
    
       
       
    while True:
        email =input("Enter valid email ")
        flag =email_checking(email)
        if flag==1:
            print("Email form valid")
        else :
            print("Not valid!")