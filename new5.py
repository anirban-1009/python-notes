from tkinter import *
from tkinter import ttk
def tt(eve):
    print("this is "+n.get())

rt=Tk()
rt.geometry("400x400")
f=Frame(rt,bg="red",width=200,height=200)
f.pack()
f.pack_propagate(0)
f.config(width=100)
b=Button(f,text="click",bg="blue").pack()
n=StringVar()
c=ttk.Combobox(f,textvariable=n)
c["values"]=("jan","feb","mar")
c.bind("<<ComboboxSelected>>",tt)
c.pack()
rt.mainloop()
