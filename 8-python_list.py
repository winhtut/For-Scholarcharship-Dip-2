


my_data=[10,20,30,40,50,60]  #list
        # 0  1  2  3  4 5

print(len(my_data))
print("Before",my_data)
my_data[0]=100 #update

print("After",my_data)
my_data.append(200)
print(my_data.insert(5,"WinHtut"))
print("After Append",my_data)

my_reversed = reversed(my_data)

for i in my_reversed:
    print(i)

print(None)