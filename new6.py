from tkinter import *
rt=Tk()
rt.geometry("400x400")
s=Scale(rt,orient=HORIZONTAL, from_=100,to=900,bg="yellow",fg="red",troughcolor="blue")
s.pack()
rt.mainloop()
