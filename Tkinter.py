### hellow world

"""
from tkinter import *

root =Tk()

label1 = Label(root, text="Pallavi")

label1.pack()
root.mainloop()

"""

### FRAMES:

"""
from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack()
# label = Label(root,text="pallavi",fg="blue")
# label.pack()
otherframe = Frame(root )
otherframe.pack(side=BOTTOM)

button1 = Button(newframe ,text="cartoon",fg="red")
button1.pack()
button2 = Button(otherframe, text="sony",fg ="green")
button2.pack()

root.mainloop()

"""

### GRID LAYOUT :

"""

from tkinter import *
root = Tk()

label1 = Label(root, text="first_name")
label2 = Label(root, text ="last_name")
# label2.pack() (use either pack or grid)

entry1 = Entry(root)
entry2 = Entry(root)
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

root.mainloop()

"""

### SELF ADJUSTIING WIDGETS :

"""
from tkinter import *

root = Tk()

label1=Label(root, text = "Start",bg="red",fg="white")
# label1.pack(fill=X)
label2=Label(root, text="STOP",bg="black",fg="white")
label2.pack(side=TOP,fill=Y)


root.mainloop()

"""

### BUTTON CLICKS :

"""
from tkinter import *

root = Tk()

def functiona():
    print("Hellow World")
    print("Pallavi")

button = Button(root, text = "click here" ,bg="green",fg="red",command=functiona)
button.pack()
root.mainloop()

"""

# from tkinter import *
# 
# root = Tk()
# 
# label1=Label(root, text="Addition")
# label1.pack()
# 
# def Add():
# 
#     a=input("enter number")
#     b=input("enter namber")
#     c=int(a)+int(b)
#     print(c)
# button =  Button(root,text="start",command=Add)
# button.pack()
# button2 = Button(root, text ="Exit",command=root.quit)
# button2.pack()
# root.mainloop()


### TKINTER USING CLASS :

"""
from tkinter import *
class mybutton:

    def __init__(self,root):

        frame=Frame(root)
        frame.pack()

        self.button1 = Button(frame , text =" Start" ,command =self.function1)
        self.button1.pack()

        self.button2 = Button(frame , text ="exit" , command = frame.quit)
        self.button2.pack()

    def function1(self):
        print("Hello World")
root1 = Tk()

object = mybutton(root1)

root1.mainloop()

"""

### TKINTER USING DROP DOWN :

"""
from tkinter import *

def function1():
    print("clicked on new file")

def function2():
    print("clicked on  SAVE")

def function3():
    print("clicked on UNDO")

root = Tk()

mymenu = Menu(root)

root.config(menu=mymenu)

firstmenu = Menu(mymenu)

mymenu.add_cascade(label ="FILE", menu=firstmenu)
firstmenu.add_command(label="NEW FILE", command=function1)
firstmenu.add_command(label="SAVE",command=function2)

firstmenu.add_separator()
firstmenu.add_command(label="Exit",command=root.quit)

secondmenu = Menu(mymenu)

mymenu.add_cascade(label="EDIT",menu=secondmenu)

secondmenu.add_command(label="UNDO",command=function3)

thirdmenu= Menu(mymenu)

mymenu.add_cascade(label="VIEW",menu=thirdmenu)

fourthmenu = Menu(mymenu)

mymenu.add_cascade(label="Navigate",menu=fourthmenu)

root.mainloop()


"""

### TKINTER TOOLBAR :

"""
from tkinter import *

def function1():
    print("clicked on new file")


root = Tk()

toolbar = Frame(root, bg="yellow")

button1 = Button(toolbar,text="start",command=function1)
button1.pack(side=LEFT,padx=2,pady=2)
button2 =Button(toolbar,text="STOP",command=function1)
button2.pack(side=LEFT)

toolbar.pack(side=TOP,fill=X)

root.mainloop()

"""

### TKINTER STATUS BAR

"""
from tkinter import *

root =Tk()

status=Label(root,text="this is status bar",bd=1,fg="red",bg="black",relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()

"""

### TKINTER MESSAGEBOX:

"""
from tkinter import *

import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("message box","are you sure")

response = tkinter.messagebox.askquestion("message box", "do you like programming")
if response == "Yes":
    print("good")

"""

### TKINTER DRAWING:

from tkinter import *

root = Tk()

canvas=Canvas(root,width=200,height=200,bg="pink")
canvas.pack()

line1=canvas.create_line(0,0,10,120,fill="black")
rectangle=canvas.create_rectangle(105,105,190,190)
root.mainloop()