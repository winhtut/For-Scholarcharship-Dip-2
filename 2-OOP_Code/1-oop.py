#OOP object oriented programming
#method

class Nist:

    def __init__(self,data): #special method class ကိုအခေါ် ခံရတာနဲ့ တန်းပြီးအလုပ်လုပ်တယ်
        print("Special Method!")
        self.someData = data
        print(self.someData)
    def myFun(self):
        print("This is from myFun")

    def myFun2(self):
        print("This is from myFun2")
        print(self.someData)



ux =Nist("ux")

