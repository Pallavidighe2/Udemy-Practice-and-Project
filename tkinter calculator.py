from tkinter import *

import parser
i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1


def get_operator(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length


def calculator():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        all_clear()
        display.insert(0,result)

    except EXCEPTION:
        all_clear()
        display.index(0,"ERROR")





def all_clear():
    display.delete(0,END)

def delete():
    variable=display.get()
    if len(variable)>0:
        newvariable=variable[:-1]
        all_clear()
        display.insert(0,newvariable)

    else:
        all_clear()
        display





root = Tk()
root.title("CALCULATOR")

display=Entry(root)
display.grid(row=0,columnspan=9,sticky=W+E,)

Button(root,text="1",command=lambda:get_variable(1)).grid(row=1,column=0)
Button(root,text="2",command=lambda:get_variable(2)).grid(row=1,column=1)
Button(root,text="3",command=lambda:get_variable(3)).grid(row=1,column=2)

Button(root,text="4",command=lambda:get_variable(4)).grid(row=2,column=0)
Button(root,text="5",command=lambda:get_variable(5)).grid(row=2,column=1)
Button(root,text="6",command=lambda:get_variable(6)).grid(row=2,column=2)

Button(root,text="7",command=lambda:get_variable(7)).grid(row=3,column=0)
Button(root,text="8",command=lambda:get_variable(8)).grid(row=3,column=1)
Button(root,text="9",command=lambda:get_variable(9)).grid(row=3,column=2)

Button(root,text="AC",command=lambda:all_clear()).grid(row=4,column=0)
Button(root,text="0",command=lambda:get_variable(0)).grid(row=4,column=1)
Button(root,text="=",command=lambda:calculator()).grid(row=4,column=2)

Button(root,text="+",command=lambda:get_operator("+")).grid(row=1,column=3)
Button(root,text="-",command=lambda:get_operator("-")).grid(row=2,column=3)
Button(root,text="*",command=lambda:get_operator("*")).grid(row=3,column=3)
Button(root,text="/",command=lambda:get_operator("/")).grid(row=4,column=3)

Button(root,text="PI",command=lambda:get_operator("*3.14")).grid(row=1,column=4)
Button(root,text="%",command=lambda:get_operator("%")).grid(row=2,column=4)
Button(root,text="^2",command=lambda:get_operator("**2")).grid(row=3,column=4)
Button(root,text="(",command=lambda:get_operator("(")).grid(row=4,column=4)

Button(root,text="EXP",command=lambda:get_operator("**")).grid(row=1,column=5)
Button(root,text="Del",command=lambda:delete()).grid(row=2,column=5)
Button(root,text="X!").grid(row=3,column=5)
Button(root,text=")",command=lambda:get_operator(")")).grid(row=4,column=5)
root.mainloop()

