
"""
class student:

    def __init__(self ,name , contact):
        self.name=name
        self.contact=contact

    def getdata(self):
        print("accept the data")
        self.name=input("enter name")
        self.contact=input("entaer contact")

    def putdata(self):

        print("the name of student is :"+self.name ,"and contact is : " +self.contact)

john=student("blank",0)
john.getdata()
john.putdata()
"""
"""
class student:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
    def pallavi(self):
        print("accept data ")
        self.name=input("enter name: ")
        self.contact=input("enter contact: ")
    def sonali(self):
        print("name is : "+self.name,"contact is : "+self.contact)

dighe=student("blank",0)
dighe.pallavi()
dighe.sonali()

"""

### INHERITANCE : (accept method from other class )

"""
class student:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact

    def getdata(self):
        print("ACCEPT THE DATA")
        self.name=input("enter name: ")
        self.contact=input("enter conntact : ")
    def putdata(self):
        print("name is : "+self.name,"contact is : " +self.contact)

class science_student(student):
    def __init__(self,age):
        self.age=age
    def takedata(self):
        self.age=input("enter age: ")
        print("ege is:"+self.age)


john=science_student(2)
john.takedata()
john.getdata()
john.putdata()

"""

### RECURSION (function call itself )

"""
def factorial(x):
    if (x==1):
        return 1
    else:
        return x*(factorial(x-1)) # function call itself
# result=factorial(5)
print(factorial(8))

"""
### ENCAPSULATION :


"""
class myclass:
    __abc=4

    def add(self,x):
        self.__abc += x
        print(self.__abc)

ans = myclass()
ans.add(7)
# print(ans.__abc)

"""

### Assignment: code challenge 12:

class computer:

    def __init(self, company, harddisk):

        self.company = company
        self.harddisk = harddisk

    def getspec(self):
        print("get specification")
        self.company = input("enter name of computer company : ")
        self.harddisk = input("enter capacity of harddisk : ")

    def putspec(self):

        print("computer name is : " +self.company ," and hardisk size is : "+ self.harddisk )

class laptop(computer):

    def __init__(self,color):

        self.color=color

    def getcolor(self):

        self.color = input("enter color name: ")

    def putcolor(self):

        print("clor of laptop is :"+self.color)

class desktop(laptop):

    def __init(self,prise):

        self.prise=prise
    def display(self):
        self.prise = input("enter prise: ")
        print("prise of desktop is :"+self.prise)

pallavi=desktop("")
pallavi.getspec()
pallavi.getcolor()
pallavi.putspec()
# pallavi.putcolor()
pallavi.display()
