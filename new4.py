from tkinter import *
from tkinter import messagebox
from tkinter import ttk
rt=Tk()
rt.title("BOX")
rt.geometry("400x400")
f=Frame(rt,bg="blue",width=200,height=200)
f.pack()
f.pack_propagate(0)
b1=Button(f, text="click").pack()
rt.mainloop()
