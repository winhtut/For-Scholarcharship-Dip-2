datas = "NationalInstitute"

some_text = "Hello i am from Heaven"

with open("nist.txt",'w') as winhtut:
    for element in datas:
        winhtut.write(element)
        winhtut.write('\n')

# with open("nist.txt",'w') as file:
#     file.write(some_text)