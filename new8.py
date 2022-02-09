from tkinter import *
def tt1(eve):
    print("hello"+str(n.get()))
    l.config(text="the updated val= "+str(n.get()))

rt=Tk()
rt.geometry("400x400")
n=DoubleVar()
s=Scale(rt,variable=n,orient=HORIZONTAL,from_=100,to=900,bg="yellow",fg="red",troughcolor="blue")
s.bind("<ButtonRelease>",tt1)
s.place(x=100,y=100,width=200)
l=Label(rt,text="This is scale")
l.place(x=1,y=100)
rt.mainloop()
