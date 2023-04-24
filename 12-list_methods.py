import copy
mylist = [1,2,3,['a','b','c']]

mylist2 = ['d','e','f']
# mylist.append(mylist2)
# print(mylist)

mylist3 = copy.copy(mylist)
mylist.append('here')
print("mylist id",id(mylist) , mylist)
print("mylist3 id",id(mylist3),mylist3)


mydlist =  [1,2,3,['a','b','c']]

mydlist2 = copy.deepcopy(mydlist)
mydlist.append("dcopy")
print("mydlist",id(mydlist),mydlist)
print("mydlist2",id(mydlist2),mydlist2)


print("#######################")

testList = [1,2,3,4]
testlist2 = testList
testList.append("hello")
print(testList,id(testList))
print(testlist2,id(testlist2))

