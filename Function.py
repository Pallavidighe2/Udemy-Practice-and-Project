# def Add(x,y):
#     print(x+y)
#
# Add(2,3)

# def add(x , y):
#     c = x+y
#     return c
#
# result=add(2,3)
# print(result)


# def add(a,b):
#     return a+b
# c=add(2,4)
# print(c)


# def add(a,b):
#     return a+b
#
# def square (c):
#     return c * c
#
# result=square(add(2,4))
# print(result)

# def square (c):
#     return c * c
# def add (a,b):
#     return a+b
# result=add(square(2),2)
# print(result)

# def add(x):
#     return x+10
# def org (func, arg):
#     return func(func(arg))
# print(org(add,2))

# def add(x):
#     return x+10
# def mult(add,arg):
#     return add (add(arg))
# print(mult(add,2))

# print((lambda x: x*2)(10))
# print((lambda a: a+10) (2) )

# def add(x):
#     return x+2
# print(add(2))

def add(x):
     return x+2
a=[10,20,30,40,50,60,13,75,35]
#
result=list(map(add,a))
print(result)

print(list(map((lambda x : x+2),a)))

result=list(filter(lambda x: x%2 ==1, a))
print(result)
# result=list(map(add, a))
# print(result)


# def number(x):
#     for x in range (21):
#         if x%2==0:
#             yield x
# print(list(number(20)))

###ASSIGNMENT:

# print((lambda x: x*(x+5)**2) (5))

# def discount(x):
#     return int(x-(x*10)/100)
#
# price=[100,200,300,400,500,600,700]
#
# result=list(map(discount,price))
# print(result)

# print((lambda x: x**2)(5))

# def square(x):
#     return x**2
# a = [1,2,3,4,5,6,7,8,9,10]
#
# print(list(map(square,a)))

# a=[1,2,3,4,5,6,7,8,9,10]
#
# print(list(filter((lambda x: x%2==0), a)))



# def function1(price):
#
#     price=int(price-(price*(10/100)))
#     return price
# result=function1(100)
# print(result)


# def function1(price):
#
#     price=int(price-(price*(10/100)))
#     return price
# result=function1(100)
# print(result)

# def function2(xprice):
#     new_price=xprice-(xprice*(5/100))
#     return new_price
# result=function2(function1(100))
# print(result)

# print((lambda x:x+2)(5))
# a=[1,2,2,3,8,3,8,6,4,5,6,7,8]
# def add(x):
#     return x+2
# print(list(map(add,a)))
#
# print(list(filter((lambda x: x%2==0),a)))
#
# b=(set(a))
# print(b)

# def function(x):
#     return x+10
# result=function(10)
# print(result)

