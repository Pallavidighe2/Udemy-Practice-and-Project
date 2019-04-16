# List = [ "Pallavi","Babasaheb","Shinde",1 ,2,3]

# Properties of List

# print(List)
# print(List[1][4])
# List[2]="dighe"
# print(List)
# List2=[1,2,4,8,10,"Pallavi"]
# print(List+List2)
# print(List2*4)
# print("Pallavi" in List2)

#  Function of List



# print(len(List))
# List.append("Dighe")
# print(List)
# List.append("Hello")
# print(List)
# List.insert(1,"World")
# print(List)
# print(List.index(2))

# numbers=list(range(10))
# print(numbers)
# numbers1=list(range(10,20))
# print(numbers1)
# numbers2=list(range(10,20,2))
# print(numbers2)

# numbers = [0,10,20,30,40,50,60,70]
# print(numbers)
# print(numbers[1])
# print(numbers[1:])
# print(numbers[:5])
# print(numbers[1:5])
# print(numbers[2:6])
# print(numbers[2:6:2])

list = [x**2 for x in range(1,5)]
print(list)
list= [x**2 for x in range(5) if x**2 %2 ==0]
print(list)

# ASSIGNMENT:

# List=[x for x in range(1,100,2)  ]
# print(List)
#
# List =[x for x in range(1,100) if x%2==1 ]
# print(List)
#
#

# TUPLES

# fruits = ("Mango" , "apple" , "Orange")
# print(fruits)
# print(fruits[2])


### SET:

# number={1,2,3,4,5,6,7}
# print(number)
# number.add(9)
# print(number)
# number.remove(4)
# print(number)
#
# seta={1,2,3,4,5,6}
# setb={5,6,7,8,9}
# print(seta | setb ) #union of set
# print(seta & setb ) # intersection of set
# print(seta - setb ) # substraction of set
