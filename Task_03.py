from tkinter import *
import re

root=Tk()
root.geometry("400x400")
root.title("SecurePass")
var=StringVar()

regex=re.compile("[!@#$%^&*~]")
def password_checker():
    word=entry.get(1.0,"end-1c")
    if len(word)<8:
        var.set("Password must be atleast 8 characters!!")
    elif not re.search("[A-Z]", word):
        var.set("Password must contain atleast one Uppercase letter!!")
    elif not re.search("[a-z]", word):
        var.set("Password must contain atleast one Lowercase letter!!")
    elif not re.search("[0-9]", word):
        var.set("Password must contain atleast one Number!!")
    elif not regex.search(word):
        var.set("Password must contain atleast one special Character!!")
    else:
        var.set("                          Password is Strong!!            ")
    
lf=Label(root, text="Enter the PassWord")
lf.place(x=140,y=10)

entry=Text(root,height=1,width=10)
entry.place(x=150,y=40)

b1=Button(root,text="check", command=password_checker)
b1.place(x=170,y=70)

l=Label(root, textvariable=var)
l.place(x=70,y=100)

