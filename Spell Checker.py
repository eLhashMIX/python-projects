import tkinter
from tkinter import *
from textblob import TextBlob

root=Tk()
root.title("Spelling Checker")
root.geometry ("600x350")
root.config (background="#dae6f6")

def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct Spelling Is :",font=("poppins",18),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading= Label(root,text="Spelling Checker",font=("Trebuchet Ms",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))
enter_text=Entry(root,justify="center",width=20,font=("poppins",23),bg="white",border=2 )
enter_text.pack(pady=10)
enter_text.focus()

Button=Button(root,text="Check",font=("arial",18,"bold"),fg="white",bg="red",command=check_spelling)
Button.pack()

spell=Label(root,font=("poppins",18),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)
root.mainloop()
