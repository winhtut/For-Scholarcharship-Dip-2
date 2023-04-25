datas = ["candc++","national","institute","of science"]

some_text = "Hello i am from Heaven"

with open("nist.txt",'w') as file:
    for element in datas:
        file.write(element)
        file.write('\n')

# with open("nist.txt",'w') as file:
#     file.write(some_text)