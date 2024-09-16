import string
from tkinter import *
import re

root=Tk()
root.geometry("400x400")
root.title("SecurePass")
var=StringVar()

regex=re.compile("[!@#$%^&*~]")
def password_checker():
    word=entry.get(1.0,"end-1c")
    upper_case=any([1 if c in string.ascii_uppercase else 0 for c in word])
    lower_case=any([1 if c in string.ascii_lowercase else 0 for c in word])
    special=any([1 if c in string.punctuation else 0 for c in word])
    digits=any([1 if c in string.digits else 0 for c in word])
    characters=[upper_case,lower_case, special, digits]
    #print(sum(characters))
    length=len(word)
    score=0
    if length>8:
        score+=1
    if length>12:
        score+=1
    if length>17:
        score+=1
    if length>20:
        score+=1
    if sum(characters)>1:
        score+=1
    if sum(characters)>2:
        score+=1
    if sum(characters)>3:
        score+=1
    if score<4:
        var.set("WEAK PASSWORD")
    elif score==4:
        var.set("MODERATE PASSWORD")
    elif score>4:
        var.set("STRONG PASSWORD")
    
    
lf=Label(root, text="Enter the Password")
lf.place(x=140,y=10)

entry=Text(root,height=1,width=20)
entry.place(x=100,y=40)

b1=Button(root,text="check", command=password_checker)
b1.place(x=170,y=70)

l=Label(root, textvariable=var)
l.place(x=130,y=150)

root.mainloop()
