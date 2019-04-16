file=open("demo.txt",'r')

# we ave to done something with file
content=file.read()
print(content)

# content1=file.read(10)
# print(content1)

# content2=file.readlines()
# print(content2)
# file.close()

# file.write("This is a python programm")
# file.close()

# file=open("demo.txt",'a')
# file.write("\nthis is new line in programm")
# file.close()

file=open("demo.txt",'a')
# file.write("pallavi")
# file.close()
file.write("good girl")
file.close()